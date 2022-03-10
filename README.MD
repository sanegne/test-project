## Swagger UI
- Implemented the Swagger UI. The default url shows the Swagger UI Page.

## Running the Server
- go to the source directory on terminal
``` bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Filter Guide
- /api/books/?genere=Contemporary&genere=Detective&genere=Dystopian
   1. this shows the books whose genere is Contemporary or Detective or Dystopian
- /api/books/?genere=Contemporary&genere=Detective&genere=Dystopian&operation=and
   1. this shows the books whose genere is Contemporary and Detective and Dystopian
- /api/books/?genere=Contemporary&genere=Detective&genere=Dystopian&operation=and&search=ken
   1. this shows the books whose genere is Contemporary and Detective and Dystopian and which have 'ken' in author, name, synopsis.

