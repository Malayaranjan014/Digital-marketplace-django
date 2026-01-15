🛒 Django Digital Marketplace

A full-stack Digital Marketplace web application built using Django, Tailwind CSS, and SQLite.The Digital MarketPlace is a platfrom where only Digital Products are Sold .
This project allows users to browse products, manage listings, place orders, and make secure payments using Stripe while providing sellers with earnings and order analytics through a clean dashboard.

🚀 Features

👤 User Authentication
• Register new users  
• Login / Logout  
• Secure session-based authentication  
• Role-based access control (Buyers / Sellers)  

🛍️ Product Management
• Add new products  
• Edit existing products  
• Delete products  
• Seller-specific product ownership  
• Product listing with detailed views  

🛒 Purchase Management
• Create purchase orders  
• Track total orders  
• Automatic calculation of total earnings  
• Buyer purchase history  

💳 Stripe Payment Gateway
• Stripe Checkout integration  
• Secure online payments  
• Test mode implementation  
• Payment success and failure handling  

📊 Dashboard & Analytics
• Earnings overview for sellers  
• Orders overview  
• Charts and statistics using charts js library
• Clean dashboard UI  
• Fully functional navigation bar  

🎨 UI / UX
• Responsive design using Tailwind CSS  
• Clean and modern layout  
• User-friendly forms and pages  
• Dashboard navigation  

🛠️ Tech Stack

Technology        Purpose  
Python            Programming Language  
Django 5          Backend Framework  
SQLite            Database  
Tailwind CSS      Frontend Styling  
HTML / CSS        Templates  
JavaScript        UI Interactions & Charts  
Stripe API        Payment Processing (Test Mode)  
Git & GitHub      Version Control  

📂 Project Structure

DIGITAL_MARKETPLACE/
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── dashboard.html
│   │       ├── sales_dashboard.html
│   │       ├── create_product.html
│   │       ├── product_edit.html
│   │       ├── delete_product.html
│   │       ├── details.html
│   │       ├── purchases.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── logout.html
│   │       ├── success.html
│   │       ├── failed.html
│   │       └── invalid.html
│   │
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── uploads/
├── db.sqlite3
├── manage.py
├── .env
├── .gitignore
└── venv/

⚙️ Installation & Setup

1. Clone the repository
git clone https://github.com/Malayaranjan014/Digital-marketplace-djang.git
cd Digital-marketplace-django

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create a .env file and add:

SECRET_KEY  
STRIPE_PUBLIC_KEY=**********  
STRIPE_SECRET_KEY=********** 

5. Run migrations
python manage.py makemigrations
python manage.py migrate

6. Start the development server
python manage.py runserver

Visit http://127.0.0.1:8000/

💳 Stripe Test Card

Card Number: 4242 4242 4242 4242  
Expiry Date: 12/27e  
CVV: Any 3 digits  

👨‍💻 Author

Malaya Ranjan  
Python & Django Developer  
GitHub: https://github.com/Malayaranjan014
