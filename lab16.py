🔬 EXPERIMENT 16: Creating Docker Image using Dockerfile (Final Clean Version)
🎯 AIM

To create a Docker image using a Dockerfile and execute a Java application inside a container.

🧠 THEORY
A Dockerfile is a script that contains instructions to build a Docker image.
It automates application packaging with dependencies.
Key instructions:
FROM → Base image
WORKDIR → Working directory
COPY → Copy files
RUN → Execute commands
CMD → Run application
🛠️ TOOLS REQUIRED
Docker Desktop
Java JDK
Text editor / IDE
📁 STEP 1: CREATE PROJECT FOLDER
mkdir docker-java-app
cd docker-java-app
💻 STEP 2: CREATE JAVA PROGRAM
📄 File: Hello.java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from Docker!");
    }
}
⚙️ STEP 3: CREATE DOCKERFILE
📄 File: Dockerfile (no extension)
FROM eclipse-temurin:17-jdk

WORKDIR /app

COPY . .

RUN javac Hello.java

CMD ["java", "Hello"]
⚠️ IMPORTANT RULES
File name must be exactly:
Dockerfile

(no .txt or extension)

Each instruction must be on a new line
Do NOT combine commands
📦 STEP 4: BUILD DOCKER IMAGE
docker build -t java-app .
▶️ STEP 5: RUN CONTAINER
docker run java-app
✅ EXPECTED OUTPUT
Hello from Docker!
🔍 STEP 6: VERIFY
List images:
docker images
List containers:
docker ps -a
🧹 STEP 7: CLEANUP (OPTIONAL)
Remove container:
docker rm <container_id>
Remove image:
docker rmi java-app
📊 RESULT
Dockerfile created successfully
Docker image built
Java program executed inside container
Output verified
