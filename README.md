# Atarank

### By Sharonne Vanessa Kemboi


<p> 13th June 2022 </p>


### Screenshot of the App

<img src="">



## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [How To Access the Site](#howtoaccessthesite)
+ [TDD](#tdd)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Known-Bugs](#knownbugs)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description
> This is a django web application that allows a user to post a project he/she has created and get it reviewed by his/her peers. A project can be rated based on 3 different criteria; Design, Usability, and Content . These criteria can be reviewed on a scale of 1-10 and the average score is taken.


## Setup/Installation Requirements

### You need to have the following installed

#### Prerequisites

You must have git, django, postgres and python3.8+ installed in your pc.
To install django and Postgres, you can use the following commands:

```
#django
$ pip install django

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

```
 
 git clone https://github.com/SharonneKemboi/Atarank.git

 virtualenv virtual

 source virtual/bin/activate

 pip3 install -r requirements.txt

 psql CREATE DATABASE galleria

 python3.8 manage.py runserver

 python manage.py migrate

 python manage.py test

```

### Deployment environment
* Heroku

### How To Access the Site
> This App is being hosted by Heroku. The link to the live site is: https://atarank.herokuapp.com/


## TDD

> To test the app, run this command in the terminal;

`$ python manage.py test`


## User Story
> As a user, I would like to:

* View posted projects and their details ---Achieved
* Post a project to be rated/reviewed ----Achieved
* Rate/ review other users' projects  ---Achieved
* Search for projects ---Achieved
* View projects overall score ---Achieved
* View my profile page ---Achieved

### Technology & Tools
* Python
* Django (Python Framework)
* HTML
* CSS
* Bootstrap
* Postgres (Database)
* JavaScript


## Reference

* [Django documentation](https://docs.djangoproject.com/en/4.0/)
* [ Django REST Framework Tutorial](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)




## Known Bugs
> There are no known bugs yet. Seen Any Bug? Please Reach out ASAP!

## License

> [MIT License](https://github.com/SharonneKemboi/Atarank/blob/master/LICENSE) 

* This application's source code is free for any open source projects

> Copyright (c) 2022 **Sharonne Kemboi**



## Authors information
> Feel free to add your contribution to the code.

> If you have any questions,comments or advice,feel free to contact me

* [Email](sharonnekay23@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/sharonne-vanessa-kemboi-a118bb135)

