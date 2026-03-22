# MINI-RAG-System

mini RAG System is a Retrieval-Augmented Generation (RAG) system designed to assist lawyers in retrieving relevant legal information and generating responses based on that information. The system combines natural language processing (NLP) techniques with a knowledge base of legal documents to provide accurate and contextually relevant answers to legal queries.

## Requirements

- Python 3.8 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fadymaher24/lawyer-rag-system.git
   ```

2. Navigate to the project directory:

   ```bash

   cd lawyer-rag-system
   ```

3. Install the required dependencies:

   ```bash

   pip install -r requirements.txt
   ```

## Usage

1. Prepare your legal documents and add them to the knowledge base.

## Set up your environment variables

```bash
cp .env.example .env
```

Use a Mongo connection URL with credentials and auth source, for example:

```env
MONGODB_URL="mongodb://admin:admin@localhost:27007/?authSource=admin"
MONGODB_DATABASE="mini_rag"
```

## Run MongoDB (Docker)

From the `docker` folder:

```bash
docker compose up -d
```

If you changed `MONGO_INITDB_ROOT_USERNAME` or `MONGO_INITDB_ROOT_PASSWORD` after first startup, recreate the volume so Mongo can re-initialize the root user:

```bash
docker compose down -v
docker compose up -d
```

## run the app

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
