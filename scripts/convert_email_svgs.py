#!/usr/bin/env python3
"""
Convert the canonical SVG email-signature icons in assets/ to PNG.

Mappings:
    assets/email_phone.svg      -> assets/email_phone.png      (40x40)
    assets/email_mail.svg       -> assets/email_mail.png       (40x40)
    assets/email_linkedin.svg   -> assets/email_linkedin.png   (40x40)
    assets/email_whatsapp.svg   -> assets/email_whatsapp.png   (40x40)

The PNGs are rendered at 2x the intended HTML display size
"""

from __future__ import annotations

import re
import struct
from pathlib import Path

import cairosvg


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

ICONS = {
    "email_phone.svg": (80, 80),
    "email_mail.svg": (80, 80),
    "email_linkedin.svg": (80, 80),
    "email_whatsapp.svg": (80, 80),
}


def normalise_svg(svg_bytes: bytes) -> bytes:
    """
    Force CSS currentColor to black.

    Iconoir SVGs commonly contain stroke="currentColor".
    In a normal webpage this inherits the surrounding CSS colour.

    When CairoSVG renders the file by itself there is no surrounding email
    CSS, so we explicitly convert currentColor to black.
    """

    text = svg_bytes.decode("utf-8")

    text = re.sub(
        r"currentColor",
        "#000000",
        text,
        flags=re.IGNORECASE,
    )

    return text.encode("utf-8")


def png_dimensions(png_bytes: bytes) -> tuple[int, int]:
    """
    Read PNG dimensions directly from the PNG IHDR header.
    This avoids requiring Pillow or another dependency.
    """

    png_signature = b"\x89PNG\r\n\x1a\n"

    if not png_bytes.startswith(png_signature):
        raise ValueError("Renderer did not return a valid PNG.")

    return struct.unpack(">II", png_bytes[16:24])


def convert_one(
    svg_path: Path,
    width: int,
    height: int,
) -> bool:
    """
    Convert one SVG to PNG.

    Returns True when the PNG file changed.
    Returns False when the generated file is identical.
    """

    if not svg_path.exists():
        raise FileNotFoundError(
            f"Missing required SVG: {svg_path.relative_to(ROOT)}"
        )

    png_path = svg_path.with_suffix(".png")

    svg_bytes = svg_path.read_bytes()
    svg_bytes = normalise_svg(svg_bytes)

    png_bytes = cairosvg.svg2png(
        bytestring=svg_bytes,
        output_width=width,
        output_height=height,
    )

    actual_width, actual_height = png_dimensions(png_bytes)

    if (actual_width, actual_height) != (width, height):
        raise RuntimeError(
            f"{png_path.name}: "
            f"expected {width}x{height}, "
            f"got {actual_width}x{actual_height}"
        )

    if png_path.exists():
        existing_bytes = png_path.read_bytes()

        if existing_bytes == png_bytes:
            print(
                f"unchanged  {png_path.relative_to(ROOT)}"
            )
            return False

    png_path.write_bytes(png_bytes)

    print(
        f"rendered   "
        f"{svg_path.relative_to(ROOT)} "
        f"-> "
        f"{png_path.relative_to(ROOT)} "
        f"({width}x{height})"
    )

    return True


def main() -> None:
    changed = 0

    for filename, (width, height) in ICONS.items():
        svg_path = ASSETS / filename

        if convert_one(svg_path, width, height):
            changed += 1

    print()
    print(f"Done. {changed} PNG file(s) changed.")


if __name__ == "__main__":
    main()