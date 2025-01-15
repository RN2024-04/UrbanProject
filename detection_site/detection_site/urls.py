from django.contrib import admin
from django.urls import path, include
from object_detection import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('register/', views.register),
    path('',include('object_detection.urls'))
]


# cd detection_site
# python manage.py runserver

# ln -s C:/Users/asus/PycharmProject/UrbanProject/detection_site/db.sqlite3 trainval_lmdb
# C:/Users/asus/PycharmProject/UrbanProject/detection_site/db.sqlite3