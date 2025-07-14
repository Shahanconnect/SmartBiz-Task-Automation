# SmartBiz Task Automation 🧠⚙️

**SmartBiz Task Automation** is a Python-powered web platform that simplifies essential business operations.
It provides tools like AI product description generation, price tracking, smart scraping, invoice generation, and OS-level system utilities — all accessible through a clean dashboard with user/admin roles.

---

## 🚀 Features

* 🤖 AI-Powered Product Description Generator *(LLM Integrated via TinyLLaMA)*
* 📉 E-commerce Price Alert Notifier
* 🌐 Smart Web Scraper (Playwright/Selenium)
* 🧾 Professional Invoice Generator
* 🖥️ OS-Level Task Controller *(browser, system info, shutdown, etc.)*
* 🔐 Secure User Authentication
* 🧑‍💼 Admin Dashboard with Role Management *(User/Admin)*
* 📄 SQLite / MySQL Database Integration

---

## 📸 [Jump to Screenshots ↓](#-screenshots)

---

## 🛠️ Tech Stack

| Layer     | Technology                             |
| --------- | -------------------------------------- |
| Backend   | Python, Flask, Flask-Login, Flask-WTF  |
| Frontend  | HTML5, CSS3, Bootstrap 5, Jinja2       |
| Database  | MySQL / SQLite, SQLAlchemy ORM         |
| Scraping  | Playwright (headless scraping)         |
| AI Engine | TinyLLaMA via Ollama (LLM integration) |

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

## 🔧 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shahanconnect/Smartbiz.git
   cd Smartbiz
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # (For Windows)
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database (MySQL / SQLite)**

   ```bash
   flask db init
   flask db migrate -m "Initial"
   flask db upgrade
   ```

5. **Run the App**

   ```bash
   python run.py
   ```

---

## 📸 Screenshots

### 🔹 Homepage

![homepage](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/homepage.png)
![homepage-2](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/homepage2.png)

### 🔹 Signup & Login

![signup](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/signup.png)
![login](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/login.png)

### 🔹 User Dashboard

![user-dashboard](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/user.png)
![user-dashboard-2](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/dashboard.png)

### 🔹 Admin Dashboard

![admin-dashboard]([https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/admin-dashboard.png](https://github.com/Shahanconnect/SmartBiz-Task-Automation/blob/1b7451bea0c6ac12fde0732481bbd14b62804a2a/app/screenshots/admin-dashboard.png))

### 🔹 User Profile

![user-profile](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/user-profile.png)

### 🔹 Product Description Generator

![description](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/description.png)

### 🔹 Invoice Generator

![invoice](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/invoice.png)
![invoice2](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/invoice2.png)

### 🔹 E-commerce Scraper

![scraper](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/scraper.png)
![scraper-2](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/scraper2.png)

### 🔹 Price Alert Notifier

![price-alert](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/price-alert.png)

### 🔹 Service Management

![service-management](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/service-management.png)

### 🔹 System Controller

![system-controller](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/system-controller.png)

### 🔹 User Management

![user-management](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/user-management.png)

---

## 🙋‍♂️ Author

**Shahan Ahmad**
📌 GitHub: [@shahanconnect](https://github.com/shahanconnect)

---

## 📚 License

You can add one of these licenses (recommended for open-source):

* [MIT License](https://choosealicense.com/licenses/mit/)
* [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)
* [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

To add a license:

```bash
touch LICENSE
```

Paste the license text from the site above and commit.
