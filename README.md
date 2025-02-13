# 🍬 Jelly Bean Flavor CRUD App  

A simple CRUD application built as part of the final interview for the **Software Developer** role at the **BYU Harold B. Lee Library**! 🎉  

## 📌 About This Project  
This application allows an admin to **Create, Read, Update, and Delete (CRUD)** jelly bean flavors, ensuring an efficient way to manage the library’s jelly bean collection.  

I’m incredibly excited about this opportunity!

---

## 🛠️ Tech Stack  
- **Backend:** Django (Python)  
- **Database:** PostgreSQL  
- **Deployment:** AWS Elastic Beanstalk, RDS  
- **Environment Management:** `.env` file locally for database configuration, `AWS Elastic Beanstalk environment variables` for live app  

---

## ⚡ Getting Started  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/trevshum20/jellybeanflavor-crud.git
cd jellybean-crud
```

### 2️⃣ Set Up the Environment Variables  

This repository **does not** include the `.env` file for connecting to the PostgreSQL database. You will also need to setup your own Postgres Database to connect to!  

To run the app locally, create a `.env` file in the root directory with the following values:  

- **DB_NAME**=<your_database_name>
- **DB_USER**=<your_database_user>
- **DB_PASSWORD**=<your_database_password>
- **DB_HOST**=<your_database_host>

### 3️⃣ Run Locally 
Install Dependencies:
```sh
pip install -r requirements.txt
```

Run the application:
```sh
python manage.py runserver
```
---
## 🚀 Deployment  
To deploy this application on AWS Elastic Beanstalk, follow these steps:

### 1️⃣ Create an AWS Elastic Beanstalk App and Environment  
### 2️⃣ ZIP the Project (Exclude Unnecessary Files)  
```sh
zip -r django-app.zip . -x "*.git*" "*.venv*" "__pycache__/*" "*.DS_Store" "sql/*" "*.pytest_cache*" "*.mypy_cache*" "*.log"
```

### 3️⃣ Upload to AWS Elastic Beanstalk
1. Navigate to the Elastic Beanstalk Console
1. Select your application environment
1. Upload django-app.zip and deploy!

---
## 🌍 Live Deployment
- This app is connected to a PostgreSQL RDS instance on AWS.
- It is currently deployed on AWS Elastic Beanstalk.

🔗 Live Demo:
[jellybean.trevorshumway.com](http://jellybean.trevorshumway.com)

---
## 📝 License
This project is for interview purposes only and is not intended for commercial use.