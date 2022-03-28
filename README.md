# Django Boilerplate
### Made with Docker, Nginx, Gunicorn and PostgreSQL
##### For myself and anyone like me who always screws up something when setting up a  new Django project.
![alt text](https://github.com/RasmusSecher/django-boilerplate/blob/main/assets/images/working-site.png)

☝️ This is what you'll see once everything is working 🤞
## Features

- Use for development and production environments.
- Local PostgreSQL database for development or connect to a remote test database.
- Runs with Gunicorn as its WSGI application server
- Nginx configured for serving the Django server and static files.
- Ready to play immediately - Templates are enabled. 

## Manual
##### For development environment follow these steps:
1. Make sure you have docker-compose installed.
2. In the root directory (the one with docker-compose), run `docker-compose build`
3. Followed by `docker-compose up`
4. To stop the services press <kbd>ctrl</kbd> + <kbd>c</kbd> or `docker-compose stop` in another terminal.

##### For production environment follow these:
1. Make sure you have docker-compose installed.
2. Fill in the .prod.env file with information regarding your database.
3. In the root directory (the one with docker-compose), run `docker-compose -f docker-compose.prod.yml build`
4. Followed by `docker-compose -f docker-compose.prod.yml up`
5. To stop the services press <kbd>ctrl</kbd> + <kbd>c</kbd> or `docker-compose stop` in another terminal.
