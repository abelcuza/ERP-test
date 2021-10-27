# How to run the project
Note: Use python >= 3.8
### Set up the project
Install the requirements:    
```shell script
pip install -r requirements.txt
```

Run the migrate command:
```shell script
python manage.py migrate
```

Fill the db with fixtures:
```shell script
python manage.py loaddata data.json
```

### Run the development server
```shell script
python manage.py runserver 8000
```
