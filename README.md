# Text Summarization Using T5

## Overview

A text summarization application that converts lengthy conversations into short, meaningful summaries using a fine-tuned T5 Transformer model.

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

* Automatic conversation summarization.
* Fine-tuned T5 model.
* FastAPI-based web application.
* Simple user interface.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python -m uvicorn app:app --reload
```

Open in your browser: `http://127.0.0.1:8000`













