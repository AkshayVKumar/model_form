import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","P7.settings")

import django
django.setup()


import random
from myapp.models import *
from faker import Faker

top=["hello",'hai','how']

f=Faker()

def add_topic():
    t=Topic.objects.get_or_create(topic=random.choice(top))[0]
    t.save()
    return t

def add_webpage(webname,url):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic=t,name=webname,url=url)[0]
    w.save()
    return w

def add_records(webname,url,date):
    w=add_webpage(webname,url)
    a=Access_Records.objects.get_or_create(name=w,date=date)[0]
    a.save()

def main(N=5):
    for i in range(N):
        f_name=f.first_name()
        f_url=f.url()
        f_date=f.date()
        add_records(f_name,f_url,f_date)

if __name__=='__main__':
    print("population is started")
    main(N=10)
    print("population is done")












