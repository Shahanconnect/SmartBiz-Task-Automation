# SmartBiz Task Automation 🧠⚙️

SmartBiz Task Automation is a Python-powered web platform designed to streamline critical business operations through a unified dashboard. It integrates multiple tools including AI-assisted product description generation, dynamic price tracking, web scraping, professional invoice creation, and OS-level utilities.

---

## 🚀 Features

* AI-based Product Description Generator (TinyLLaMA via Ollama)
* E-commerce Price Alert Notification System
* Smart Web Scraper using Playwright
* Invoice Generator with PDF support
* OS-Level Task Controller (browser, system info, restart, shutdown)
* Secure Authentication with Role-based Access (User/Admin)
* Admin Dashboard for Service, User, and Role Management
* Persistent storage using MySQL or SQLite

---

## 🛠️ Tech Stack

| Layer     | Technology                            |
| --------- | ------------------------------------- |
| Backend   | Python, Flask, Flask-Login, Flask-WTF |
| Frontend  | HTML5, CSS3, Bootstrap 5, Jinja2      |
| Database  | MySQL / SQLite, SQLAlchemy ORM        |
| Scraping  | Playwright (headless scraping)        |
| AI Engine | TinyLLaMA (locally hosted via Ollama) |

---

## 🗂️ Project Structure

```
SmartBiz/
├── app/
│   ├── templates/
│   ├── static/
│   ├── forms/
│   ├── services/
│   ├── routes.py
│   └── __init__.py
├── models/
├── database/
├── requirements.txt
├── README.md
└── run.py
```

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/shahanconnect/SmartBiz-Task-Automation.git
cd SmartBiz-Task-Automation

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install required packages
pip install -r requirements.txt

# Set up the database
flask db init
flask db migrate -m "Initial"
flask db upgrade

# Start the application
python run.py
```

---

## 📸 Screenshots

### 🔹 Homepage

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/homepage.png" width="600" style="margin-bottom: 10px;">
<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/homepage2.png" width="600" style="margin-bottom: 10px;">

### 🔹 Signup & Login

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/signup.png" width="600" style="margin-bottom: 10px;">
<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/login.png" width="600" style="margin-bottom: 10px;">

### 🔹 User Dashboard

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/user.png" width="600" style="margin-bottom: 10px;">

### 🔹 Product Description Generator

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/description.png" width="600" style="margin-bottom: 10px;">

### 🔹 E-commerce Scraper

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/scraper.png" width="600" style="margin-bottom: 10px;">
<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/scraper2.png" width="600" style="margin-bottom: 10px;">

### 🔹 Price Alert Notifier

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/price-alert.png" width="600" style="margin-bottom: 10px;">

### 🔹 Invoice Generator

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/invoice.png" width="600" style="margin-bottom: 10px;">
<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/invoice2.png" width="600" style="margin-bottom: 10px;">

### 🔹 Admin Dashboard

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/admin-dashboard.png" width="600" style="margin-bottom: 10px;">

### 🔹 User Management

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/user-management.png" width="600" style="margin-bottom: 10px;">

### 🔹 Service Management

<img src="https://raw.githubusercontent.com/shahanconnect/SmartBiz-Task-Automation/main/app/screenshots/service-management.png" width="600" style="margin-bottom: 10px;">

---

## 👨‍💻 Developer

Shahan Ahmad
GitHub: [@shahanconnect](https://github.com/shahanconnect)

---

## 📄 License

```
Copyright (c) 2025 Shahan Ahmad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
