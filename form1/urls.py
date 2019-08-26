from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('new/',views.test,name='new'),
    path('redirect/',views.redirect,name='redirect'),
    path('showing/',views.showing,name="showing"),
    path('detailview/',views.detail_view,name='details'),
    path('detailview2/<int:id>/',views.detail_view2,name='details2'),
    path('createview/',views.createview,name='createview'),
    path('update/<int:id>/edit',views.update_view,name='update'),
]
