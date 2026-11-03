# Text Summarization Using T5

## Overview

A web-based text summarization application that generates short and meaningful summaries from lengthy conversations using a fine-tuned T5 Transformer model.

The model is fine-tuned on the SAMSum dataset using Hugging Face Transformers and deployed using FastAPI.

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* T5 Transformer
* SAMSum Dataset
* FastAPI
* HTML & CSS

## Features

* Automatic text summarization
* Fine-tuned T5 model
* FastAPI backend
* Simple and user-friendly interface

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python -m uvicorn app:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000
```

