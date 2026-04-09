EXPERIMENT 18: Dockerizing a Python Application (Corrected & Clean)
🎯 AIM

To create and run a Python application inside a Docker container using a Dockerfile.

🧠 THEORY
Docker can containerize applications written in any language.
A Dockerfile defines how the environment is built.
Python apps do not require compilation → directly executed.
🛠️ TOOLS REQUIRED
Docker Desktop
Text editor / IDE
📁 STEP 1: CREATE PROJECT FOLDER
mkdir docker-python-app
cd docker-python-app
💻 STEP 2: CREATE PYTHON PROGRAM
📄 File: app.py
print("Hello from Python Docker App!")
⚙️ STEP 3: CREATE DOCKERFILE
📄 File: Dockerfile (no extension)
FROM python:3.10

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
⚠️ IMPORTANT RULES
File name must be exactly:
Dockerfile

(no extension)

Each instruction must be on a new line
CMD must be complete
📦 STEP 4: BUILD DOCKER IMAGE
docker build -t python-app .

✔ This creates the image locally

▶️ STEP 5: RUN CONTAINER
docker run python-app
✅ EXPECTED OUTPUT
Hello from Python Docker App!
🔍 STEP 6: VERIFY
List images:
docker images
List containers:
docker ps -a
🧹 STEP 7: CLEANUP (OPTIONAL)
Remove container:
docker rm <container_id>
Remove image:
docker rmi python-app
📊 RESULT
Python application successfully containerized
Docker image built and executed
Output verified