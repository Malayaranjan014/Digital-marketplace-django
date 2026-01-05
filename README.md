🛒 Digital Marketplace – Django Web Application

A full-stack Digital Marketplace web application built using Django and Tailwind CSS.
This project allows users to browse products, make purchases, and view earnings and order statistics through a clean dashboard.

 Features
 ___________________________________

👤 User Authentication

-User registration & login
-Secure session-based authentication
-Role-based access (buyers / sellers)

🛍️ Product Management

-Add, edit, and delete products
-Product listing with details
-Seller-specific product control

🛒 Purchase System

-Create purchase orders
-Track total orders
-Calculate total earnings automatically

📊 Dashboard & Analytics
  -Earnings overview  
  - Orders overview  
  - Charts and statistics  
  - Functional navigation bar 

🎨 UI / UX

-Responsive design using Tailwind CSS
-Clean and modern layout
-User-friendly forms and pages


🛠️ Tech Stack
_______________________________________
Technology	          Usage
Python	              Backend logic
Django 5	            Web framework
SQLite	              Database
Tailwind CSS	        Styling
HTML	                Templates
JavaScript	          UI interactions
Git & GitHub	        Version control


## 📂 Project Structure

DIGITAL_MARKETPLACE/
│
├── mysite/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── myapp/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ │ └── myapp/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── dashboard.html
│ │ ├── sales_dashboard.html
│ │ ├── create_product.html
│ │ ├── product_edit.html
│ │ ├── delete_product.html
│ │ ├── details.html
│ │ ├── purchases.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── logout.html
│ │ ├── success.html
│ │ ├── failed.html
│ │ └── invalid.html
│ │
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ └── urls.py
│
├── uploads/
├── db.sqlite3
├── manage.py
├── .env
├── .gitignore
└── venv/






