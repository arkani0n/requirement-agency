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

First in 'recruitment_agency' directory rename 'settings_info_example.py' to 'settings_info.py'

     Though Python:
         Postgresql installed 
         Run init.sql in Postgres (\i 'path to file'/init.sql)
         Select virtual environment
         Run pip install -r requirements.txt
         Run python manage.py makemigrations and python manage.py migrate
         If needed to create superuser to use admin part run python manage.py createsuperuser
         To run server: python manage.py runserver

     Though Docker:
        docker and docker compose installed
        remane 'docker-comose_example.yml' to 'docker-compose.yml'
        run docker-compose up     
    
