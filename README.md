# python-class-django-overview
Django presentation project for the Python class.

The quick overview of the main concepts of Django Framework: Model, View, Template.

This app does nothing. Just has a few CRUD endpoints.

# How to install
 - make sure that pip has been installed (run `pip -V` in terminal)
 - it recommends to use `virtualenv` to keep projects under personal environment. To manage environments try `pyenv`
 - run `pip install -r requirements/base.txt` in terminal

 # Source code
 The `djtest` project has been started by `django-admin.py startproject djtest` command run. There is no need to run it again.

 Newly created files from the deepest `djtest` folder are needed to be moved one level higher for more convenience, and old folder renamed to `apps` for the project's apps. File `manage.py` should be moved too.

 There is a `settins.py` file tweak:

 ```python
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
```
With this there is no more need to specify the full path to apps' classes.

### Nums app
The `nums` app has been created by `django-admin.py startapp nums` command. Actually, `manage.py` might be used too.
**To create app into `apps` directory need to swith to this into terminal**. Newly created app has been registered into `INSTALLED_APPS` variable, thus told
Django to look for our app on start up.

It is the simplest app endowed with basic functionality without any HTTP methods segregation etcetera.

First of all, we distinguish the main entities of our app and present them by models. In case of this app, `Models` as database entities are.

```python
class Number(models.Model):
    value = models.IntegerField()
```

Look at the base class for `Number` model's class. It's a base class for all user models.

To present our model in database, first of all, we need to create `migrations` files using 'makemigrations' command and then, *migrate* them using 'migrate' command.
Output of `makemigrations`:

```
Migrations for 'nums':
  djtest/apps/nums/migrations/0001_initial.py
    - Create model Number
```

Output of `migrate`:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, nums, sessions
Running migrations:
  Applying nums.0001_initial... OK
```

**Attention**: run `migrate` after code of the repo been cloned.
`makemigrations` calls once new model has been added or changed existing.

Next, `views` were created into `views.py` file. Function-based views were used to keep it simpler (if you're curious - read about Class-Based views).

```python
from django.shortcuts import render

from .models import Number


def list_view(request):
    numbers = Number.objects.all()
    return render(request, 'list.html', context={'numbers': numbers})


def create_view(request, number):
    number = Number(value=number)
    number.save()

    return render(request, 'created.html', context={'number': number})
...
```

Once `views` created, we need to have `urls.py` file to expose app endpoints and serve them.

```python
from django.urls import path

from . import views

urlpatterns = (
    path('', views.list_view, name='nums_list'),
    path('create/<int:number>', views.create_view, name='nums_create'),
    path('update/<int:number_id>/<int:value>', views.update_view, name='nums_update'),
    path('delete/<int:number_id>', views.delete_view, name='nums_delete'),
)
```

Pay your attention to `urlpatterns` var. Using of `include` requires to store our URL patterns into `urlpatterns` var.

Test the app: run `./manage.py runserver localhost:9991` and open the URL in ~~your favorite browser~~ Chrome. :-)

Try requests:
 - `http://localhost:9991/numbers`
 - `http://localhost:9991/create/88`
 - `http://localhost:9991/numbers`
 - `http://localhost:9991/numbers/update/1/99`
 - `http://localhost:9991/numbers`
 - `http://localhost:9991/create/99`
 - `http://localhost:9991/numbers`
