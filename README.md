# Photos Gallery Backend 
An application serve api endpoint for others server can easily connect with
## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a RESTful API application, the purpose of this application is serve api endpoint for a web application where I have plan to create my own blog, my profile as a software engineer and showing girl's photos just for relax 

## Technologies 
Project is created with: 
* Django 
* Mysql 
* Others library to handle authentication with jwt

## Setup 
To run this project, firstly, clone this project into your computer, when you inside root's project folder 

Install library from requirements.txt. I highly recommend to create a new virtual environment before
```
$ npm install -r requirements.txt
```

Change configure values in ```settings.py``` to fit with your DB local

Run project by typing script 
```
$ python manage.py runserver
```
