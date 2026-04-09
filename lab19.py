🔬 EXPERIMENT 19: Docker Compose (Final Clean Instructions)
🎯 AIM

To run a multi-container application using Docker Compose and deploy a Python Flask web app.

🧠 THEORY
Docker Compose is used to manage multi-container applications.
It uses a YAML file (docker-compose.yml) to define services.
It simplifies running applications with multiple components.
🛠️ TOOLS REQUIRED
Docker Desktop (Docker + Docker Compose installed)
📍 WHERE TO RUN COMMANDS

👉 Run ALL commands in:

PowerShell / CMD (Host System)

❌ Do NOT run inside container

📁 STEP 1: CREATE PROJECT FOLDER
mkdir docker-compose-app
cd docker-compose-app
💻 STEP 2: CREATE PYTHON FILE
📄 File: app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker Compose!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
📄 STEP 3: CREATE REQUIREMENTS FILE
📄 File: requirements.txt
flask
⚙️ STEP 4: CREATE DOCKERFILE
📄 File: Dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask

CMD ["python", "app.py"]
⚙️ STEP 5: CREATE COMPOSE FILE
📄 File: docker-compose.yml
version: "3"

services:
  web:
    build: .
    ports:
      - "5000:5000"
📂 FINAL PROJECT STRUCTURE
docker-compose-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
▶️ STEP 6: BUILD AND RUN

Run in PowerShell:

docker-compose up --build
🔍 STEP 7: CHECK OUTPUT

You should see:

Running on http://0.0.0.0:5000
🌐 STEP 8: ACCESS APPLICATION

Open browser:

http://localhost:5000
▶️ STEP 9: STOP APPLICATION

Press:

Ctrl + C

Then run:

docker-compose down
📊 RESULT
Flask app deployed using Docker Compose
Multi-container setup managed via YAML
Application accessible through browser
