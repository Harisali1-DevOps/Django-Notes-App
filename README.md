<<<<<<< HEAD
# django-testproject
=======
# Django-Notes-App
A colorful, full-width notes app built with Django, featuring create/edit/delete functionality and a sticky-note style UI. Dockerized for easy deployment.


cat > README.md << 'EOF'
# 📝 Django Notes App

A colorful, full-width notes app built with Django. Create, edit, and delete notes with a clean, sticky-note style UI — each note can be color-coded (yellow, blue, green, red, purple).

![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django)
![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)

## ✨ Features

- Create, edit, and delete notes
- Color-coded notes (5 color options)
- Responsive, full-width grid layout
- Gradient background with smooth hover animations
- Dockerized for easy deployment

## 🛠️ Tech Stack

- **Backend:** Django 6.1
- **Database:** SQLite
- **Server:** Gunicorn
- **Containerization:** Docker

## 🚀 Getting Started

### Option 1: Run locally

\`\`\`bash
git clone <your-repo-url>
cd django-notes-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
\`\`\`

Visit `http://localhost:8000` in your browser.

### Option 2: Run with Docker

\`\`\`bash
sudo docker build -t django-notes-app .
sudo docker run -d -p 8000:8000 --name notes-container django-notes-app
sudo docker exec -it notes-container python manage.py migrate
\`\`\`

Visit `http://localhost:8000` (or your server's IP) in your browser.

## 📂 Project Structure

\`\`\`
Django-App/
├── hello_django/       # Project settings
├── my_app/             # Main app (models, views, templates)
│   ├── models.py
│   ├── views.py
│   └── templates/my_app/
│       ├── note_list.html
│       ├── note_form.html
│       └── note_confirm_delete.html
├── manage.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
\`\`\`

## 📌 Notes

- By default, the SQLite database inside the container is **not persistent** — data resets when the container is removed. To persist data, mount a volume:
  \`\`\`bash
  sudo docker run -d -p 8000:8000 -v $(pwd)/db.sqlite3:/app/db.sqlite3 --name notes-container django-notes-app
>>>>>>> c830d6a0cb07bff667b359a880d440368f66135a
