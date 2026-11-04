# Text Summarization Using T5 Transformer

## Overview

An AI-powered text summarization application that converts lengthy conversations into short, meaningful summaries.

The project uses a fine-tuned **T5 (Text-to-Text Transfer Transformer)** model trained on the **SAMSum dataset**. The model is integrated with FastAPI to provide an interactive web application.

## Project Demo

The application allows users to enter a conversation and automatically generate a concise summary.

## Features

* Automatic conversation summarization.
* Fine-tuned T5 Transformer model.
* Trained on the SAMSum dataset.
* FastAPI-based backend.
* Simple and user-friendly web interface.
* Real-time summary generation.

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* T5 Transformer
* SAMSum Dataset
* FastAPI
* HTML
* CSS
* JavaScript

## Pre-trained Model

The fine-tuned model is hosted on Hugging Face:

[Text Summarization T5 Model](https://huggingface.co/varsha100704/text-summarization-t5)

## Project Structure

```text
TEXT_SUMMARIZED_APP/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VarshaRaj1604/Text-Summarization-T5.git
```

### 2. Open the project folder

```bash
cd Text-Summarization-T5
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m uvicorn app:app --reload
```

### 5. Open in your browser

```text
http://127.0.0.1:8000
```

## How It Works

1. User enters a conversation into the text area.
2. The input text is processed and tokenized.
3. The fine-tuned T5 model generates a summary.
4. The generated summary is displayed on the webpage.

## Future Improvements

* Improve summary quality.
* Support longer input documents.
* Add summary length control.
* Deploy the application online.

## Author

**Varsha Rajbhar**

GitHub: [VarshaRaj1604](https://github.com/VarshaRaj1604)

Hugging Face: [varsha100704](https://huggingface.co/varsha100704)
