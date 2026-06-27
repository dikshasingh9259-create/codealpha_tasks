# 🛒 Full-Stack E-Commerce Platform

A dynamic, full-stack e-commerce web application featuring a responsive HTML/CSS/JavaScript frontend and a robust Django backend. This platform handles user authentication, product management, real-time searching, shopping cart operations, and order processing.

---

## 🚀 Key Features

* **Live Search Bar:** Instant, real-time product filtering as users type.
* **Shopping Cart:** Add, update, and remove items with dynamic price calculations.
* **Product Details Page:** Dedicated, rich viewing experience for every item.
* **User Authentication:** Secure user registration, login, and session management.
* **Order Processing:** Seamless checkout workflow to handle user purchases.
* **Admin Dashboard:** Built-in Django panel to easily manage products, users, and orders.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript (Vanilla ES6)
* **Backend Framework:** Django (Python)
* **Database:** SQLite (Default) / PostgreSQL 
* **Authentication:** Django Built-in Auth System

---

## 📦 Project Structure
text 
CODEALPHA_ECOMMERCESITE/
├── ecommerce/      # Main application logic and components
├── store/          # Store-specific logic, products, or checkout
├── media/          # Directory for uploaded media (e.g., product images)
│   └── products/   # Sub-folder specifically for product assets
├── db.sqlite3      # The project's SQLite database file
├── manage.py       # Django command-line utility for administrative tasks
└── README.md       # Project documentation and setup instructions

  
## ⚙️ Installation and Setup

Follow these steps to set up and run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/dikshasingh9259-create/codealpha_tasks/tree/main/codealpha_ecommercesite
cd codealpha_tasks/codealpha_ecommercesite
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```
*(Note: If you have a requirements.txt file, run: `pip install -r requirements.txt`)*

### 4. Apply Database Migrations
Create the database tables for products, users, and orders:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin User
Create a superuser account to access the Django backend dashboard:
```bash
python manage.py createsuperuser
```
*Follow the terminal prompts to set up your username, email, and password.*

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to view your e-commerce store. Access the admin dashboard at [http://127.0.0](http://127.0.0).

---

