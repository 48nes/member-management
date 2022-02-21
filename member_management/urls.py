from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # list page
    path('add', views.add, name='add_member'),  # add member page
    path('edit/<member_id>', views.edit, name='edit_member'),  # edit member page
    path('<path>', views.unknown_path, name='unknown_path')  # unknown paths
]
