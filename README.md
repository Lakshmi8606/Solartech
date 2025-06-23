# SolarTech – Django-Based Solar Management System

A web-based platform built with Django for managing solar energy components, customer requests, installations, and admin workflows. This was developed as an academic project demonstrating full-stack functionality using Python.

---

## 🚀 Features

- Admin dashboard to manage categories, products, complaints, and installations
- CR (Customer Representative) request assignment and tracking
- Dynamic UI rendering using Django templates
- AJAX-based interactivity for responsive user experience
- SQLite database integration for data storage
- Modular and extendable Django app structure

---

## 🛠 Tech Stack

- **Backend**: Python 3.x, Django  
- **Frontend**: HTML, CSS, Bootstrap, AJAX  
- **Database**: SQLite  
- **IDE**: VS Code  

---

## 🧪 How to Run Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

## 📂 Project Structure

```
Solartech/
├── Admin/                  # Django app with views, models, templates
├── db.sqlite3             # Project database
├── manage.py              # Django manager script
└── .vscode/               # Editor config
```
