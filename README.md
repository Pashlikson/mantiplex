# Mantiplex
```Learning and teaching platform for students, teachers and parents```\
This is a django project, so you need to know basic\
django's commands to custon our project.\
\
Right down is a list of a django basic codes, that every should know:\
```You must read this article to get work with django project!!!```

## How to use django?

### To run project you need:
1. insatall dependency
```bash
pip install
```
2. pull the github project
```bash
git pull origin main 
```

3. run django site
```bash
python manage.py runserver
```

### To run a pulled project(means you can configure the project):
1. just run project with this command
```bash
python manage.py runserver
```
2. after every change you can just save files with ```Ctrl+S``` and reload page


### Static files code:
1. after configuring static files you should run this code to get style changed
```bash
python manage.py collectstatic
``` 

### Models code:
1. after configuring models.py file in app you should run this code to change models properties
```bash
 python manage.py makemigrations --name <changed_my_model>
``` 
2. in second, you have to run this command to get models change
```bash
python manage.py migrate
```

### Create user:
1. to create user you must write down this code
```bash
python manage.py createsuperuser
```
2. you have to write down an username, email and password

## Mark tasks:
In file, you can set tasks for later work, to not forget, what you want to.

1. To set a task, you have to write down code above:

in python file:
```bash
...python code #//TODO: task_description
```
2. in search write down 'TODO' and you will find all tasks

## GitHub instruction:
You can go in this link to get an important git commands:\
[An GitHub document guide](https://docs.google.com/document/d/1ePXHZpycQqG8ReS46S621vizd7IvUzW-YrazYbT1o9I/edit?tab=t.0#heading=h.tgnriy2ij3q);\
[An Youtube GitHub course](https://www.youtube.com/playlist?list=PLenwk9TUJzJ6Vqurjtsg_PsCVirACH9SE).

## GitHub project:
[Mantiplex site (our repository)](https://github.com/Pashlikson/mantiplex/tree/main)