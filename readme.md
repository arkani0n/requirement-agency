Project was made for portfolio purpose 
View online: http://165.22.196.216/

In this project i used:
1. Class-based views
1. 2 roles of users (Companies and Clients)
1. Authorisation and authentication 
1. Decorators, to make permissions

About project:

First about users. There are 2 roles of users, companies and clients.
 
Company can create, change and delete vacancies.
Also vacancy can be deactivated, so it will not appear in search results 

Client can upload their CV to website, view vacancies and, if they are interested, 
send their CV to vacancy or return it. 
 
If client sent CV to vacancy, company, that created vacancy, will be able to see it, 
when open the vacancy page    

Structure of website is pretty simple, there only 'Profile' and 'Vacancies' pages
. 

In 'Profile' users can see their information and have link to change information, if it is company, vacancies of company will 
be shown under.

In 'Vacancies' all users can see all active vacancies or use search, if they want to. In search user selects category 
and then enter the words that must be in vacancy title, then press 'Find' button and vacancies would be sorted by user criteria. 
Except this companies can create vacancies here and also see only their vacancies (deactivated too).
Clients, have a link to see all vacancies where they sent CV   

How to start:

Run git clone command to download the project

        git clone https://github.com/arkani0n/requirement-agency.git
        
First in 'recruitment_agency' directory, rename 'settings_info_example.py' to 'settings_info.py'

Though Python:

1. Postgresql installed 
1. Login as postgres and run in postgres command line:

        CREATE USER admin WITH PASSWORD 'password';
        CREATE DATABASE requirement_agency;
        GRANT ALL PRIVILEGES ON DATABASE  requirement_agency TO admin;

1. If your virtual environment isn't created run:

    To create venv
    
         python -m venv /path/to/new/virtual/environment
         
    And to activate it:
    
          source venv/bin/activate  
         
1. To install all needed to run the project:

         pip install -r requirements.txt
1. To prepare database to work, in project directory run:    
     
         python manage.py makemigrations 
         python manage.py migrate

1. To run server: 

          python manage.py runserver
If needed to create superuser run:

         python manage.py createsuperuser

Though Docker:
1. Install docker and docker compose 
1. Rename 'docker-compose_example.yml' to 'docker-compose.yml'
1. In project directory run: 

        docker-compose up 
During build a "PermissionError" may appear with 'requirement-agency/postgres-data' directory
to fix it you need to give rights on this directory to your user:
        
        sudo chown -R 'your user':'your user' postgres-data     
    

    
     
    
