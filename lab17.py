

# 🔬 EXPERIMENT 17: Docker Volumes and Port Mapping

---

## 🎯 AIM

To understand Docker volumes and port mapping, and to persist data using containers.

---

## 🧠 THEORY

* **Port Mapping** allows access to container services from the host system.
* **Volumes** are used to persist data outside the container lifecycle.
* Containers are temporary, but volumes store data permanently.

---

## 🛠️ TOOLS REQUIRED

* Docker Desktop

---

## ⚙️ STEP 1: RUN NGINX WITH PORT MAPPING

Do all these steps in Docker

```bash
docker run -d -p 8081:80 nginx
```

---

## 🌐 STEP 2: ACCESS APPLICATION

Open browser:

```text
http://localhost:8081
```

✔ Nginx default page should appear

---

## 🧠 UNDERSTANDING PORT MAPPING

```text
8081:80
```

* `8081` → Host port
* `80` → Container port

---

## ⚙️ STEP 3: CREATE A VOLUME

```bash
docker volume create myvolume
```

---

## ⚙️ STEP 4: VERIFY VOLUME

```bash
docker volume ls
```

---

## ⚙️ STEP 5: RUN CONTAINER WITH VOLUME

```bash
docker run -d -p 8082:80 -v myvolume:/usr/share/nginx/html nginx
```

---

## 🧠 WHAT THIS DOES

* Mounts volume to:

```text
/usr/share/nginx/html
```

* This is nginx web root
* Data stored here persists even if container is deleted

---

## ⚙️ STEP 6: INSPECT VOLUME

```bash
docker volume inspect myvolume
```

---

## ⚙️ STEP 7: STOP CONTAINER

```bash
docker ps
docker stop <container_id>
```

---

## ⚙️ STEP 8: REMOVE CONTAINER

```bash
docker rm <container_id>
```

---

## ⚙️ STEP 9: RUN AGAIN WITH SAME VOLUME

```bash
docker run -d -p 8082:80 -v myvolume:/usr/share/nginx/html nginx
```

✔ Data remains intact

---

## 📊 RESULT

* Port mapping successfully configured
* Docker volume created and used
* Data persisted across container lifecycle

---

## 🧠 VIVA QUESTIONS

1. What is port mapping?
   → Connecting container port to host port

2. What is volume?
   → Persistent storage for containers

3. Why use volumes?
   → Data persistence

4. Difference between container and volume?
   → Container is temporary, volume is persistent

5. What is -p in Docker?
   → Port mapping

6. What is -v in Docker?
   → Volume mounting

---

## ⚠️ COMMON ERRORS

* Port already in use
* Wrong volume path
* Docker not running
* Confusing host vs container port

---

## ✅ CONCLUSION

Docker volumes and port mapping enable persistent storage and external access to containerized applications, making them essential for real-world deployments.

---
