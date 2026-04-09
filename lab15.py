# 🔬 EXPERIMENT 15: Introduction to Docker and Basic Commands (Corrected & Clear)

---

## 🎯 AIM

To understand Docker fundamentals and execute basic Docker commands.

---

## 🧠 THEORY

* **Docker** is a containerization platform used to package applications with dependencies.
* It ensures consistency across environments.
* Key terms:

  * **Image** → Blueprint of application
  * **Container** → Running instance of image

---

## 🛠️ TOOLS REQUIRED

* Docker Desktop (installed and running)

---

## ⚠️ IMPORTANT NOTE (VERY IMPORTANT)

* Docker commands must be run in **host system (PowerShell / CMD)**
* ❌ Do NOT run Docker commands inside container (`root@...`)
* To exit container, use:

```bash
exit
```

---

## ⚙️ STEP 1: VERIFY DOCKER INSTALLATION

```bash
docker --version
```

---

## ⚙️ STEP 2: CHECK DOCKER SERVICE

```bash
docker info
```

---

## ⚙️ STEP 3: RUN FIRST CONTAINER

```bash
docker run hello-world
```

✔ Downloads and runs test container

---

## ⚙️ STEP 4: LIST IMAGES

```bash
docker images
```

---

## ⚙️ STEP 5: LIST CONTAINERS

### Running containers:

```bash
docker ps
```

### All containers:

```bash
docker ps -a
```

---

## ⚙️ STEP 6: RUN UBUNTU CONTAINER

```bash
docker run -it ubuntu
```

✔ Opens interactive Linux shell

To exit:

```bash
exit
```

---

## ⚙️ STEP 7: PULL IMAGE

```bash
docker pull nginx
```

---

## ⚙️ STEP 8: RUN NGINX CONTAINER

```bash
docker run -d -p 8081:80 nginx
```

---

## 🌐 STEP 9: ACCESS APPLICATION

Open browser:

```text
http://localhost:8081
```

✔ Nginx default page should load

---

## ⚙️ STEP 10: STOP CONTAINER

```bash
docker ps
docker stop <container_id>
```

---

## ⚙️ STEP 11: REMOVE CONTAINER

```bash
docker rm <container_id>
```

---

## ⚙️ STEP 12: CLEAN ALL CONTAINERS (OPTIONAL)

```bash
docker ps -aq | % {docker rm $_}
```

---

## ⚙️ STEP 13: REMOVE IMAGE

```bash
docker rmi nginx
```

---

## 📊 RESULT

* Docker installed and verified
* Containers executed successfully
* Basic Docker commands understood
