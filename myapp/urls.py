from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns=[
    path('topics/',views.topic,name="topic"),
    path('records/',views.records,name="records"),
    path('page5/',views.page5,name='forms'),
    path('display/',views.display,name="display"),
    path('page7/',views.page7,name='page7'),
    path('delete/',views.delete,name="delete"),
    path('page9/',views.page9,name='page9'),
    path('update/',views.update,name="update"),
    path('page10/',views.page10,name='page10'),
    path('report/',views.report,name='report')
]