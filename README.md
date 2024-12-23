# Labelbox as a Web App

Labelbox is a web application designed for data annotation. It provides a simple interface for managing annotation tasks and projects, storing them in a database, and ensuring no data is saved locally on the user's device.

## Features

- **Annotation Projects:** Create and manage annotation projects.
- **Task Management:** Assign images to annotation tasks and store task details in the database.
- **Annotation Saving:** Save annotations in JSON format directly to the database.
- **Web-Based Interface:** Access and use the application via a web browser.
- **Deployable Solution:** Designed for deployment as a standalone web application.

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Labelbox
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

1. **Create a Project:**  
   Add a new project using the Django admin interface or via a custom project management view.

2. **Add Tasks:**  
   Assign images to tasks for annotation.

3. **Annotate:**  
   Navigate to the annotation screen for a specific task. Add annotations and save them directly to the database.

## Directory Structure

```plaintext
Labelbox
├─ annotations
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations/
│  ├─ models.py
│  ├─ views.py
│  ├─ templates/
│  │  └─ annotations/
│  │      ├─ annotation_screen.html
│  └─ __init__.py
├─ Labelbox
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
└─ README.md
```

## Requirements

- Python 3.8 or higher
- Django 5.1.4
- SQLite (default) or any other supported database

