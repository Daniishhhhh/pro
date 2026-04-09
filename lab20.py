🔬 EXPERIMENT 20: CI/CD Pipeline using Jenkins, Maven, and Docker (Final Clean Manual)
🎯 AIM

To automate build, testing, packaging, and deployment of a Java application using Jenkins, Maven, and Docker.

🧠 THEORY
CI/CD automates the software lifecycle.
Maven → Build + Test + Package (JAR)
Jenkins → Automation server
Docker → Container-based deployment

Pipeline flow:

Code → Maven Build → JUnit Test → JAR → Docker Image → Container Run
🛠️ TOOLS REQUIRED
Jenkins (http://localhost:8080)
Docker Desktop
Maven
Java (JDK 17+)
📍 PROJECT PATH (USE EXACT)
C:\Users\danis\OneDrive\Pictures\Documents\devopslab\junit-demo
📂 FINAL PROJECT STRUCTURE
junit-demo/
│
├── src/
├── target/
├── pom.xml
└── Dockerfile
⚙️ STEP 1: UPDATE pom.xml

Ensure your pom.xml includes:

<packaging>jar</packaging>

<build>
    <finalName>app</finalName>
</build>
⚙️ STEP 2: CREATE DOCKERFILE

📄 Path:

C:\Users\danis\OneDrive\Pictures\Documents\devopslab\junit-demo\Dockerfile
📄 Dockerfile
FROM eclipse-temurin:17-jdk

WORKDIR /app

COPY target/*.jar app.jar

CMD ["java", "-jar", "app.jar"]
⚙️ STEP 3: VERIFY LOCALLY

Run in PowerShell:

cd C:\Users\danis\OneDrive\Pictures\Documents\devopslab\junit-demo

mvn clean package
✅ VERIFY JAR
dir target

Output must contain:

app.jar
⚙️ STEP 4: TEST DOCKER LOCALLY
docker build -t devops-app .
docker run devops-app
⚙️ STEP 5: CONFIGURE JENKINS
🔹 Open Jenkins
http://localhost:8080
🔹 Create New Job
Name: CI-CD-Pipeline
Type: Freestyle Project
🔹 General → Advanced

✔ Enable:

Use custom workspace

Enter:

C:\Users\danis\OneDrive\Pictures\Documents\devopslab\junit-demo
⚙️ STEP 6: ADD BUILD STEPS
🔹 STEP 1: Maven Build

Add → Invoke top-level Maven targets

Goals: clean package
🔹 STEP 2: Docker Build

Add → Execute Windows batch command

docker build -t devops-app .
🔹 STEP 3: Docker Run

Add → Execute Windows batch command

docker stop devops-container >nul 2>&1
docker rm devops-container >nul 2>&1
docker run -d --name devops-container devops-app
⚙️ STEP 7: POST-BUILD ACTION

Add → Publish JUnit test result report

target/surefire-reports/*.xml
▶️ STEP 8: RUN PIPELINE

Click:

Build Now
✅ EXPECTED OUTPUT
Jenkins Console:
BUILD SUCCESS
Tests run: 3, Failures: 0
Docker Check:
docker ps -a

You will see:

devops-container (Exited)
⚠️ IMPORTANT NOTE
This is a non-web application
No browser output expected
Container runs and exits after execution
📊 RESULT
Maven build successful
JUnit tests executed
JAR file generated
Docker image built
Container executed using Jenkins
CI/CD pipeline completed successfully