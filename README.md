# 🚀 Flask Multiplication Table App – Docker Deployment Guide

This project is a simple Flask web application where the user enters a number and the app generates its multiplication table.

---

## 🧱 Project Overview

* User enters a number in the browser
* Flask generates the multiplication table from **1 to 10**
* Runs inside a Docker container
* Can be shared and executed by any developer easily

---

## 📌 Flask App Working

The app accepts a number using an HTML form and displays its multiplication table.
Everything runs inside `app.py`.

---

## 🐳 Docker Usage Guide

### 1️⃣ If another developer wants to use your image

Your Docker image has already been pushed to Docker Hub.
Assume your Docker Hub image name is:

```
pratik776/table
```

### 2️⃣ Pull the image from Docker Hub

```bash
docker pull pratik776/table
```

### 3️⃣ Run the container

Expose Flask's default 5000 port:

```bash
docker run -p 5000:5000 pratik776/table
```

### 4️⃣ Open the browser and check

```
http://localhost:5000
```

---

## 🔍 Helpful Docker Commands

| Command         | Purpose                 |
| --------------- | ----------------------- |
| `docker images` | View downloaded images  |
| `docker ps`     | View running containers |

---

## ⚠️ About the `FROM python:3.9` Highlight

The yellow underline in VS Code is **not an error**. It is just metadata showing when the image was last pushed.
There is no issue with the line:

```
FROM python:3.9
```

You can safely ignore the tooltip.

---

## 🎯 Summary

Once your image is on Docker Hub, any developer can run your Flask app using:

```bash
docker pull pratik776/table
docker run -p 5000:5000 pratik776/table
```

No need to install Python, Flask, or dependencies — Docker does everything!

---

Happy Coding! 🛠️
