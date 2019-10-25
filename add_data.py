from myapp.models import *

def add_topic(top_name):
    t=Topic.objects.get_or_create(topic=top_name)[0]
    t.save()
    return t

def get_topic(topic):
    t=Topic.objects.get(topic=topic)
    return t

def add_webpage(topname,webpagename,url):
    w=Webpage.objects.get_or_create(topic=get_topic(topname),name=webpagename,url=url)[0]
    w.save()
