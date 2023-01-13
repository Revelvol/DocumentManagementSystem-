# Document Management System
The Document Management System is a web application built using the Django framework, designed to manage and organize documents.
Tried to host it on heroku and its work ![Document](/static/images/0.png)

![Document](/static/images/1.png)

### Features
- CRUD functionality for user and document models + filter 

![Document](/static/images/crudDocument.png)
![Document](/static/images/crudProfile.png)
- User login, registration, and authentication

![Document](/static/images/registraton.png) ![Document](/static/images/login.png)

- Roles 

![Document](/static/images/roleData.png)
![Document](/static/images/roles.png)


- Password reset

![Document](/static/images/passwordReset1.png)
![Document](/static/images/passwordReset2.png)
- Password validation using built-in Django auth password validators

![Document](/static/images/passwordValidation.jpg)
- Document PDF upload to Amazon S3 bucket with synced progress bar made with AJAX

![Document](/static/images/upload%20bar%20.png)

### Technologies Used

- Language: Python, Html, Css, Javascript
- Framework: Django
- Cloud: Amazon RDS, S3 Bucket
- Database: PostgresSQL  
- Server: Hosted on Heroku

### Installation
1. Clone the repository
2. Create a virtual environment and activate it
3. Install the required packages
4. Create a `.env` file in the root directory and add the following environment variables: DJANGO_SECRET_KEY, AWS_ACCESS_KEY_ID
, AWS_SECRET_ACCESS_KEY
, AWS_STORAGE_BUCKET_NAME
, DATABASE_URL
5. Run migrations
6. Run the server

### Deployment
To deploy the application on Heroku, follow the steps given in the [Heroku documentation](https://devcenter.heroku.com/articles/deploying-python).



