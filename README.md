# HL Photo Gallery

The online marketplace for genuine prints of the work of HL.

## Installation

```
git clone https://github.com/robbawebba/hlphoto.git && cd hlphoto
pip3 install -r requirements.txt

# create the sqlite database and apply the required migrations
python3 manage.py migrate
```

## Running Locally

You can start the development server by running:
```
python3 manage.py runserver
```

This will start the local development server listening on port 8000 by default.
If you prefer to have the server listen on a different port, you can provide a
different port number as the last argument to runserver:
```
python3 manage.py runserver 8080
```
