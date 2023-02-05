# Django-HTMX Chat Application

This is a simple backend focused chat application, created with django and htmx. There is 0% trace of javascript in the source code :) 
HTMX abstracts aay the usage of Javascript for connecting and interacting with the websockets and other protocols.

## Features:

- Create Rooms
- Join Room with code
- Send and Recieve Message

## Installation:

1. Clone the repository

```
git clone https://github.com/Mr-Destructive/django-htmx-chat
```

2. Create a python virtual environment

```
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Make Migrations:

```
python manage.py migrate
```

5. Run the Server:

```
python manage.py runserver
```
