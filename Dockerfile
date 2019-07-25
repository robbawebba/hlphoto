FROM python:3.7

# Create source and db directories for our project and database files
RUN mkdir /src/ /db/

# Install requirements before copying our source to take advantage of layer caching
# Because the requirements will change less frequently than the source code
WORKDIR /src/
COPY requirements.txt /src/
RUN pip install -r requirements.txt

COPY . /src

EXPOSE 8000

# The database will be created at /db/db/sqlite3. Users should mount an external
# volume to /db into the container if they would like to persist the data from
# running this project.
ENV DB_PATH "/db"
VOLUME /db

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
