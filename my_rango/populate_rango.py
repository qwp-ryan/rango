import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'my_rango.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {"title":"Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial"},
        {"title":"how to think like a computer scientist",
         "url":"http://www.greenteapress.com/thinkpython"},
        {"title":"Learn Python in 10 minutes",
         "url":"http://www.korokithakis.net/tutorials/python"}
    ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01"},
        {"title":"django rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"how to tango with django",
         "url":"http://www.tangowithdjango/"},
    ]

    other_pages = [
        {"title":"bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"flask",
         "url":"http://flask.pocoo.org"},
    ]

    cats = {"Python":{"pages":python_pages},
            "Django":{"pages":django_pages},
            "Other Framworks":{"pages":other_pages},}

    for cat, cat_data in cats.items():
        c=add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print (" - {0} - {1}".format(str(c),str(p)))


def add_page(cat, title, url, views=0):
    p=Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p


def add_cat(name):
    c=Category.objects.get_or_create(name=name)[0]
    if c.name == "Python":
        c.views=128
        c.likes=64
    elif c.name == "Django":
        c.views = 64
        c.likes = 32
    elif c.name == "Other Framworks":
        c.views = 32
        c.likes = 16
    c.save()
    return c

if __name__ == '__main__':
    print ("Starting Rango population script ...")
    populate()

