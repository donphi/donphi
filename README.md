# 🚀 Research Engineer (AI, Large-Scale Data Systems)

Survivor of a combined double-lung and liver transplant (141st globally at Penn Medicine). This experience reshaped my priorities: I now build infrastructure and tooling that strengthen scientific reliability and accelerate discovery.

My background spans design, high-stakes operations, and 12 years of leadership in finance. Today, I focus on **AI systems engineering**: large-scale multimodal pipelines, reproducible ML workflows, and research-enabling infrastructure for biomedical science. I am completing an MSc in **Artificial Intelligence & Digital Health** while developing this high-throughput research system.

I thrive on hard technical problems, high ambiguity, and complex data flows. My focus is the **system**: building the foundations that make scientific and ML workflows robust, scalable, and trustworthy.

---

## 🔭 Core Project: (MSc) End-to-End Scientific Data System

I am currently building a single, cohesive system to process, index, and validate the UK Biobank research corpus. It is composed of three primary layers:

### 1. The Ingestion Layer: 23-Stage Multimodal Pipeline
A GPU-aware orchestration pipeline (Prefect, RabbitMQ) to convert raw PDFs into structured JSON. It integrates Docling, Marker, LayoutLMv3, and PaddleOCR and is built with hardware-aware profiles for DGX B200 and RTX 6000-class GPUs.

### 2. The Knowledge Base Layer: Ontology & Indexing
A data engineering pipeline that builds a searchable knowledge base. It parses raw MONDO/HPO/EFO ontology files into a DuckDB graph, and a parallel-processing ETL script indexes semantically-chunked documents into Elasticsearch.

### 3. The Application Layer: HITL Alias Miner & Validation
An ML-driven Flask application that validates scientific features. It uses SapBERT embeddings to find and score potential aliases from the corpus, then presents them to a human reviewer. The result is a high-quality, verified `feature_cards.jsonl` dataset for downstream model training.

---

## 🛠️ Technical Focus & Tooling

### Core Areas
- Large-scale multimodal data systems
- Distributed compute & GPU-optimised pipelines
- Deterministic research workflows
- Ontology-driven feature extraction
- Human-in-the-Loop (HITL) validation pipelines
- Reproducible ML infrastructure

### Technologies
- **Python**, R
- **PyTorch**, **vLLM**, **Hugging Face**, **Lifelines**, **SHAP**
- **Docling**, **Marker**, **PaddleOCR**, **LayoutLMv3**
- **FAISS**, **Elasticsearch**, **PostgreSQL**, **DuckDB**
- **Polars**, Pandas, NumPy
- **Prefect**, **RabbitMQ**, **Flask**
- **Docker (GPU)**, **CUDA 12.x**, **Linux**
- **React**, **D3.js**, CI/CD

---

## 🌱 Currently Deepening
- Low-rank adaptation (LoRA) and domain-specific fine-tuning
- Analyzing research on latent space dimensionality and its connection to model capabilities (e.g., language context vs. multi-modal world modeling).
- ML systems design for biomedical automation
- Advanced statistical modelling (Statistics II)

---

## 🌐 Website
[https://donphi.work](https://donphi.work)

## 📫 Connect
LinkedIn: [https://www.linkedin.com/in/donphi](https://www.linkedin.com/in/donphi)
