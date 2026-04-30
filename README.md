# 🚀 Docker Flask + MySQL Project

## 📌 Project Overview
This project is a simple 2-tier application built using Docker.

- Flask (Python web app)
- MySQL (Database)
- Docker containers
- Docker networking

👉 The application fetches data from MySQL database and displays it in a browser.

---

## 🛠️ Technologies Used
- Python (Flask)
- MySQL
- Docker
- AWS EC2

---

## ⚙️ Project Architecture

Flask App (Container) ---> MySQL (Container)

👉 Both containers are connected using a custom Docker network.

---

## 🚀 How to Run

### 1. Create Network
```bash
# Create a Docker network for container communication
docker network create twotier

### 2. Run MySQL Container
```bash
# Note: If mysql container already running, skip this step
docker run -d --name mysql \
--network twotier \
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_DATABASE=devops \
mysql
