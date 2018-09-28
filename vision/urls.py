from django.urls import path
from . import views

app_name = 'vision'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/post_detail", views.post_detail, name="post_detail")
]
