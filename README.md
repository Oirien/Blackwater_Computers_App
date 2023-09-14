# Blackwater Computers Webapp

## Requires Python and Flask installation.

This project was a brief to create a python MVC based app using flask and a postgreSQL database, and the first major project I undertook as a student software developer. Specifically I chose to create a fictional service to browse PC components and be able to create a custom build. The learning objectives were to consolidate my understanding of Python and Flask whilst integrating SQL databases and specifically postgreSQL and SQLalchemy. My extension goals were to create the ability to dynamically fill information on the page about the total price of the computer, whther the total power supply was able to meet the total power draw of the components and whether or not the Motherbaord and CPU were compatible with each other, all of which I managed to do, however using Jinja and Python made that rather tricky, and it is my understanding that it would be far easier in Javascript which we were forbidden from using for this project.

---

I learned a lot during the course of the project, however the learning outcome that surprised me the most was I went from not particularly enjoying CSS to really quite liking working with it. I however did find that SQL and join tables with polymorphic subclasses to be more difficult than I anticipated and given how they ended up structured in the database at the end I woulnd't have bothered with them again for this type of application.

---

Below are a couple of pictures of the final product.

![B1](https://github.com/Oirien/Blackwater_Computers_App/assets/136370232/5dcccde6-73ac-4b43-a20c-c5c9f9d1c8e7)

![B2](https://github.com/Oirien/Blackwater_Computers_App/assets/136370232/572dc43b-ee82-447d-893a-a33b4f01afd7)

### TO RUN

You will need Python and Flask, as well as PostgreSQL and SQLAlchemy.

On line 7 of app.py you will have to adjust the path to your own database.

To start you will need to initialise and seed the database. We can do this by:

  flask db init
  flask db upgrade
  flask db migrate
  flask db run seed

Then after the database is properly seeded we run the following.

  flask run

This should give a prompt to say that the app is running on the localhost.

