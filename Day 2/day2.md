## Create a view hello_world and map it to endpoint hello/

```python
# app/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello, World!')
```

```python

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
]
```

```bash

# Run development server
python manage.py runserver
```

Open your browser and navigate to http://localhost:8000/hello/

You should see "Hello, World!" displayed on the page.
