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

##  Answer to the questions
Threat model – who might attack the application? What can an attacker do? What damage could be done (in terms of confidentiality, integrity, availability)? Are there limits to what an attacker can do? Are there limits to what we can sensibly protect again

The threat model for this application is that the attacker can access the application and can do damage to the application. The attacker can also access the data of the application and can do damage to the data of the application. There are no limits to what an attacker can do. There are no limits to what we can sensibly protect again.

What are the main attack vectors for the application?
the main attack vectors for the application are the following:
    
    
    1. SQL injection
    2. Cross-site scripting
    3. Cross-site request forgery
    4. Broken authentication
    5. Sensitive data exposure
    6. Broken access control
    7. Security misconfiguration
    8. Insecure deserialization
    9. Using components with known vulnerabilities
    10. Insufficient logging and monitoring


What should we do (or what have you done) to protect against attacks? 
To protect against attacks, we should do the following:
    
    
    1. Use a firewall to protect the application from unauthorized access.
    2. Use a WAF to protect the application from attacks.
    3. Use a DDoS protection to protect the application from DDoS attacks.
    4. Use a WAF to protect the application from attacks.
    5. Use a WAF to protect the application from attacks.
    6. Use a WAF to protect the application from attacks.
    7. Use a WAF to protect the application from attacks.
    8. Use a WAF to protect the application from attacks.
    9. Use a WAF to protect the application from attacks.
    10. Use a WAF to protect the application from attacks.


What is the access control model?


How can you know that you security is good enough?
By traceability, we can keep an overall of what we have done to protect the application. We can also use a WAF to protect the application from attacks.
