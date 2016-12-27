# osb.moe

![Cool screenshot, bro!](http://i.imgur.com/QtdtG7b.jpg)

The website for Osu! Storyboarder Banquet, a site highlighting the best storyboards featured on the online rhythm game, [osu!](https://osu.ppy.sh). Storyboards are background animations that play alongside circle-clicking action. This site not only aims to showcase the best visual works for them, but also be an educational resource for learning how to storyboard and program. osb.moe is developed through the web framework [Django](https://djangoproject.com).

# Contributions
Contributions are welcome! Any efforts to improve the website, whether on the front or back-end, are all hugely appreciative. Currently, future proposed ideas and a general direction of where to improve the site are [all organized on Trello](https://trello.com/b/dyXbXLtN/osb-moe).

## Setup
Cloning your own repository, while relatively painless with Git, can be a bit more complicated when dealing with package dependencies. To clone, just run this command in your terminal in the desired directory.

`git clone https://github.com/osb-group/osb.moe`

You'll need the following dependencies on your installation of Python 2.7:
* Django 1.10.4
* Pillow 3.4.2
* Django-Photologue 3.6 (and its dependencies)
* psycopg2 (PostgreSQL) 2.62

`settings.py` for the osb project should be pretty ambivalent regarding the actual website's information, but you may need to change things in there to satisfy your own build; for instance, if it has to load on a localhost. The most important changes would making sure that you have a corresponding PostgreSQL database and superuser for Django to perform operations on. You can see that `settings.py` relies on a dictionary named `OUTSIDE_INFO` for these components.

It's probably best to develop or work on this using a virtual Python library, so installed components do not overlap or intertwine with anything. No one likes unexpected errors due to funny installations.

Execution of the server should be typical of any basic Django installation. For more information, it never hurts to read the [official Django 1.10 documentation](https://docs.djangoproject.com/en/1.10).
