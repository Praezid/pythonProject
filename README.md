# pythonProject

Project launch:

1) Clone repo `git clone https://github.com/Praezid/pythonProject.git`
2) Go to the project folder `cd pythonProject` 
3) Install the virtual enviroment `virtualenv env`
4) Run the virtual enviroment `.\env\Scripts\activate`
5) Update pip `python -m pip install --upgrade pip`
6) Go to the project folder `cd backend`
7) Install in the virtual enviroment the dependencies for the project `python -m pip install --no-cache-dir -r requirements.txt``
8) Make migrations `python manage.py migrate`
9) Create superuser `python manage.py createsuperuser`
10) Start the local server `python manage.py runserver`
