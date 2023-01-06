To run the application, you need to have a working installation of Python 3.6 or higher. You can download it from [python.org](python.org).

##  Installation of required packages
run the following command in the terminal to install the required packages:
    
    
    pip install -r requirements.txt

##  Running the application
To run the application, run the following command in the terminal:
    
    
    python wsgi.py

## My implementation
1. I chose to implement the application using the Flask framework. I chose this framework because it is very easy to use and it is very easy to implement a REST API with it. I also chose to use the Flask-RESTful extension to make it easier to implement the REST API.
2. I use the Flask-SQLAlchemy extension to make it easier to work with the database. It makes it easier to work with the database migrations.
3. Session management is done using the Flask-Login extension. It makes it easier to manage the user sessions.
4. I use the Flask-WTF extension to make it easier to work with forms. It makes it easier to validate the form data.
5. I use jinja2 to make it easier to create the HTML templates.
6. I use blueprints to make it easier to organize the application.
7. I have a config.py file where I store the configuration variables for the application.
8. I have a models.py file where I store the database models for the application.
9. I have a forms.py file where I store the forms for the application.
10. I have a routes.py file where I store the routes for the application.

