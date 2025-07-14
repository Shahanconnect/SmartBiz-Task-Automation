# SmartBiz Task Automation 🧠⚙️

**SmartBiz Task Automation** is a Python-powered web platform that simplifies essential business operations. It offers tools for AI-based product description generation, price tracking, web scraping, invoice generation, and system task management — all accessible via a clean  dashboard.

---

## 🚀 Features

-  AI-Powered Product Description Generator (LLM Integrated)
-  E-commerce Price Alert Notifier
-  Smart Web Scraper (Playwright/Selenium)
-  Professional Invoice Generator
-  OS-Level Task Controller (open browser, system info, etc.)
-  Secure User Authentication
-  Admin Dashboard with Role Management (User/Admin)
-  SQLite/MySQL database integration

---

## 🛠️ Tech Stack

| Layer       | Technology                     

| Backend     | Python, Flask, Flask-Login      
| Frontend    | HTML5, CSS3, Bootstrap, Jinja2  
| Database    | MySQL, SQLAlchemy ORM  
| Forms       | Flask-WTF             
| Scraping    | Playwright           
| AI Engine   | TinyLLaMA 


---

## 🖥️ Project Structure


SmartBiz/
├── app/
│ ├── templates/
│ ├── static/
│ ├── routes.py
│ ├── forms/
│ ├── services/
│ └── init.py
├── models/
├── database/
├── README.md
├── requirements.txt
└── run.py


---

## 🔧 Installation & Setup

Download and setup python 3.x , mysql , tinyllama(ollama)  , playwright

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smartbiz-task-automation.git
cd smartbiz-task-automation

## 2.

python -m venv venv
venv\Scripts\activate  # Windows

#3. Install dependencies

pip install -r requirements.txt


#4 setup the database 
flask db init
flask db migrate -m "Initial"
flask db upgrade


#5 run the app
python run.py


🙋‍♂️ Author
Shahan Ahmad
GitHub: @shahanconnect



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
![admin-dashboard](https://raw.githubusercontent.com/shahanconnect/Smartbiz/main/app/screenshots/admin-dashboard.png)

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
