##Tutorial with Django-rest-framework

this is an introduction tutorial for the Django-Rest-Framework

##installation
```python
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/books.json
python manage.py loaddata fixtures/gr_users.json 
#pip install httpie==0.9.3
#pip install djangorestframework==3.2.3