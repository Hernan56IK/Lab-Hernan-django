# Backend Component

## Summary

Under construction

## Steps run the backend without Docker


### 1. Create and activate python environment

Inside backend folder:

```
# Create the virtual environment
python -m venv env 
```

or

```
# Create the virtual environment
virtualenv -p python3 env
```

```
# Activate the virtual environment (Linux/Mac)
source env/bin/activate
```

```
# Activate the virtual environment (Windows)
env\Scripts\activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Configure database connection

In the settings.py file, configure the database you want to use (SQLite is the default).

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Run the development server

```
python manage.py runserver
```

## Steps run the backend with Docker


### 1. Build docker image

Inside backend folder:

```
docker build -t japeto/facturion_backend .

```
### 2. Run backend within Docker container

```
docker run --name facturion_backend -p 0.0.0.0:8000:8000 japeto/facturion_backend
```

