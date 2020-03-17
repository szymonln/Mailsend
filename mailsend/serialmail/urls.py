from django.urls import path

from . import views


urlpatterns = [
    path('upload', views.upload_file, name='upload'),
    path('send_mails/<file_name>', views.send_mails, name='send_mails'),
    path('', views.root_view, name='root_view')
]
