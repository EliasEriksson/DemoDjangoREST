# DemoDjangoREST
A demo project for a REST service using django, and django rest framework.

## Running the demo
To run the demo open `demoClient/index.html` in a browser and filling in the credentials.

The demo always runs against `https://djangodemo.eliaseriksson.eu/`

## Run the service
The django server requires a new `settings.py` file to be generated as it contains some sensitive data and have \
therefor not been included in the repository.

1. To be able to run the service a new `settings.py` file needs to be generated. This can be done by starting a new django \
project and take that generated `settings.py` file and put it inside `djangoRESTRoot/djangoREST/`.
2. Iinstall all necessary packages to your preferred python home. If run under the django development server you probably want a venv.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    ```

3. add this to `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       "REST.apps.RestConfig",
       "rest_framework",
       "rest_framework.authtoken",
       "corsheaders"
   ]
   
   MIDDLEWARE = [
       ...
       'corsheaders.middleware.CorsMiddleware',
       'django.middleware.common.CommonMiddleware',
   ]
   
   CORS_ORIGIN_ALLOW_ALL = True
   CORS_ALLOWED_ORIGINS = [
       '*',
   ]
   ```
    Default database is sqlite3 but can be changed to any database supported by django.
4. run the migrations required for the database:
   ```bash
   cd djangoRESTRoot
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run with django development server
    ```bash
    python manage.py runserver
    ```