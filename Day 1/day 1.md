-  Create python virtual environment
```bash
python3 -m venv venv
```
-  Activate the virtual environment
```bash
source venv/bin/activate
```
- Create django project
```bash
django-admin startproject day1
```
- Create django app
```bash
python manage.py startapp app
```
- Add app to installed apps in settings.py
```python
INSTALLED_APPS = [
    'app',
    ...
]
```

- Run development server
```bash
python manage.py runserver
```