import os
import subprocess
import webbrowser


'''
to do :
    -venv
    -activate venv
    -install django
    -create django project 
    -create super user
    -create app
    -migrate
    -runserver
    -website
'''
new_venv = str(input("Enter the name of Venv ")).strip()
os.system(f'python -m venv {new_venv}')
path = os.path.abspath(f'{new_venv}/Scripts')
os.chdir(path)
os.system('activate')
os.system('pip install django')
os.chdir(os.path.abspath('../..'))

project_name = str(input("Enter the name of project ")).strip()
subprocess.run(f'django-admin startproject {project_name}')
project_path = os.path.abspath(f'{project_name}')
os.chdir(project_path)
query = str(input("Would you want to create app ? 'y' or 'n' ")).strip().lower() 
if query.lower() in 'yes':
    app_name = str(input("Enter the name of app ")).strip()
    os.system(f'python manage.py startapp {app_name}')
    
else:
    pass

os.system('python manage.py migrate')
webbrowser.open('http://127.0.0.1:8000/')
os.system('python manage.py runserver')