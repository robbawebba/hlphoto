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

## Generating Test Data

The Gallery app comes with a `genphotos` managment command that allows
users to add a variable number of photos to the database:
```
# Generates 200 photos
python3 manage.py genphotos 200
```

Photo instances are created with a URL pointing to an image from
https://picsum.photos.

## Running with Docker

The Dockerfile located at the root of this directory is a handy tool for building
and running this Django project on any host platform.

To run this application in Docker, you must first build the Docker image locally: 
```
docker build . -t hlphoto
```

Next, we must create our database and apply the migrations to make the database
available across sessions:
```
docker run --rm -it -v hlphoto-db:/db -p 8000:8000 hlphoto python3 manage.py migrate
```

The above command creates a docker volume named `hlphoto-db`, mounts
this volume into the Docker container at `/db`, and runs the database
migration and photo generation commands to initialize the database. This
volume must be mounted into the container every time you would like to
use this database.

If you would like to create some sample data, you can use the genphotos command
at this time to populate the database with some photos:
```
docker run --rm -it -v hlphoto-db:/db -p 8000:8000 hlphoto python3 manage.py genphotos 100
```

Lastly, we can run the django application with this volume mounted into
the container:
```
docker run --rm -it -v hlphoto-db:/db -p 8000:8000 hlphoto
```

if you visit http://localhost:8000 in your browser, you will be able to view
the gallery of photos and order your desired prints :)


You can remove the database volume from your system with the `docker volume rm hlphoto-db` command. Note that once you remove this volume, you will have to perform the above steps for recreating the database.
