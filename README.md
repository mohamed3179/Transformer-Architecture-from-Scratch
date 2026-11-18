# 🚀 Transformer from Scratch using PyTorch

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?logo=pytorch)
![NLP](https://img.shields.io/badge/Domain-NLP-green)
![Transformer](https://img.shields.io/badge/Architecture-Transformer-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

This project focuses on understanding, implementing, and training a **Transformer architecture from scratch using PyTorch**, based on the research paper:

**"Attention Is All You Need" (Vaswani et al., 2017).**

The main objective is to understand how Transformers work internally, from tokenization and embeddings to self-attention, encoder-decoder architecture, and neural machine translation.

The project uses an English-to-Italian translation task to explore the practical application of Transformer models.

## 🎯 Objectives

- Understand the original Transformer architecture.
- Implement the main components using PyTorch.
- Understand Self-Attention and Multi-Head Attention.
- Implement Encoder and Decoder blocks.
- Train a Transformer model for machine translation.
- Explore the training and inference processes.
- Understand how attention mechanisms process sequential data.

## 🧠 Transformer Architecture

The Transformer architecture consists of two main components:

### 1. Encoder

The encoder processes the input sequence and generates contextual representations.

Main components:
- Input Embedding
- Positional Encoding
- Multi-Head Self-Attention
- Feed Forward Neural Network
- Residual Connections
- Layer Normalization

### 2. Decoder

The decoder generates the translated output sequence using the encoder representations.

Main components:
- Target Embedding
- Positional Encoding
- Masked Multi-Head Self-Attention
- Cross-Attention
- Feed Forward Neural Network
- Residual Connections
- Layer Normalization
- Linear Projection

### Architecture Diagram

![Transformer Architecture](https://raw.githubusercontent.com/SirawitC/Transformer_from_scratch_pytorch/main/img/transformer.png)

## ⚙️ Core Concepts

| Component | Description |
|---|---|
| Tokenization | Converts text into tokens |
| Embedding | Converts tokens into numerical vectors |
| Positional Encoding | Adds positional information |
| Self-Attention | Captures relationships between tokens |
| Multi-Head Attention | Learns different attention patterns |
| Feed Forward | Processes token representations |
| Layer Normalization | Stabilizes training |
| Residual Connections | Helps information and gradients flow |
| Encoder | Processes source sequences |
| Decoder | Generates target sequences |

## 📂 Project Structure

```text
Transformer_from_scratch_pytorch/
│
├── config.ipynb
├── dataset.ipynb
├── model.ipynb
├── train.ipynb
│
├── requirements.txt
├── README.md
│
└── .gitignore
```

## 📊 Dataset

**Dataset:** OPUS Books

**Source:** Hugging Face Datasets

https://huggingface.co/datasets/Helsinki-NLP/opus_books

| Parameter | Value |
|---|---|
| Task | Neural Machine Translation |
| Source Language | English |
| Target Language | Italian |
| Dataset | OPUS Books |
| Framework | PyTorch |

The dataset contains parallel English and Italian sentences used to train the Transformer model.

## 🛠️ Technologies Used

- Python
- PyTorch
- NumPy
- Hugging Face Datasets
- Tokenizers
- Matplotlib
- Jupyter Notebook
- Google Colab

## 💻 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Transformer_from_scratch_pytorch.git

cd Transformer_from_scratch_pytorch
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook

```bash
pip install notebook
jupyter notebook
```

## 🚀 Training

The project is organized into notebooks:

1. **config.ipynb:** Configure model and training parameters.
2. **dataset.ipynb:** Load and preprocess the dataset.
3. **model.ipynb:** Implement the Transformer architecture.
4. **train.ipynb:** Train and evaluate the model.

Open the notebooks in Jupyter Notebook or Google Colab and execute their cells in the appropriate order.

For GPU training, Google Colab with a CUDA-compatible GPU is recommended.

## 📚 Research Paper

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017).

**Attention Is All You Need.**

[Read the original research paper](https://arxiv.org/abs/1706.03762)

## 🎓 Learning Outcomes

Through this project, I explore:

- Deep Learning fundamentals.
- Natural Language Processing (NLP).
- Transformer architecture.
- Attention mechanisms.
- Sequence-to-sequence learning.
- Neural Machine Translation.
- Model training and evaluation using PyTorch.

## 👨‍💻 Author

**Mohamed**

Computer Science & Artificial Intelligence Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Natural Language Processing
- Large Language Models (LLMs)
- Generative AI


