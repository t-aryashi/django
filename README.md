# django

For project2 restaurant_service
Here’s a detailed guide on how to run and test the Django project, including setting up a virtual environment (venv):

## 1. Clone the Repository

First, clone your repository from GitHub:

```bash
git clone https://github.com/t-aryashi/django.git
cd django
```

## 2. Set Up a Virtual Environment

Create and activate a virtual environment. This isolates your project’s dependencies from your global Python installation.

### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` file is up to date. You can generate it using:

```bash
pip freeze > requirements.txt
```

## 4. Set Up the Database

Run the following commands to set up your database:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Create a Superuser

Create a superuser account to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser credentials.

## 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Your project should now be accessible at `http://127.0.0.1:8000/`.

## 7. Running Tests

To run tests for your Django project, use:

```bash
python manage.py test
```

Ensure you have written your tests in the appropriate test files under your Django apps.

## 8. Static Files

Collect static files for production:

```bash
python manage.py collectstatic
```

## Additional Notes

### Environment Variables

You might want to create a `.env` file in your project root and load these variables using `django-environ` or a similar package.

Example `.env` file:

```plaintext
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
```

### `.gitignore`

Ensure your `.gitignore` file includes the following lines to avoid committing unnecessary files:

```plaintext
# Virtual environment
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.sqlite3
# Django stuff:
*.log
staticfiles/
media/
```

## Summary

By following these steps, you can set up, run, and test your Django project efficiently. Always ensure your `requirements.txt` is up to date and your environment variables are correctly set up for different environments (development, testing, production).
