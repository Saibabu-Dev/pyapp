# 🚀 Docker Flask + MySQL Project

## 📌 Project Overview
This project is a simple 2-tier application built using Docker.

- Flask (Python web app)
- MySQL (Database)
- Docker containers
- Docker networking

The application fetches data from MySQL database and displays it in a browser.

---

## 🛠️ Technologies Used
- Python (Flask)
- MySQL
- Docker
- AWS EC2

---

## ⚙️ Project Architecture

Flask App (Container)  --->  MySQL (Container)

Both containers are connected using Docker custom network.

---

## 🚀 How to Run

### 1. Create Network
```bash
docker network create twotier
