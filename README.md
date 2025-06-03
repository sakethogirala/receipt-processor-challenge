# 🧾 Receipt Processor API

This project is a receipt processing web service that calculates reward points based on receipt data using predefined rules.

It implements the API as described in the provided `api.yml`, with endpoints to:
- Process a receipt (`POST /receipts/points`)
- Retrieve points for a given receipt (`GET /receipts/{id}/points`)

---

## Tech Stack

- Python 3.10
- Flask
- Docker

---

## Run Instructions (Using Docker)

> Note: Docker **must be installed** to run this service.

### 1. Clone the repository
```bash
git clone https://github.com/sakethogirala/receipt-processor-challenge.git
cd receipt-processor-challenge

### 2. Build the Docker image
```bash
docker build -t receipt-processor .

### 3. Run the Docker container
```bash
docker run -p 5050:5000 receipt-processor

### API Endpoints:
POST /receipts/points

Request Example:
curl -X POST http://localhost:5050/receipts/points \
  -H "Content-Type: application/json" \
  --data-binary @examples/morning-receipt.json

Response Example:
{"id": "a-uuid-value"}


GET /receipts/{id}/points
Request Example:
curl http://localhost:5050/receipts/a-uuid-value/points

Response Example:
{"points": 31}

