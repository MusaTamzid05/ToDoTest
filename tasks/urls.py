from django.urls import path
from . import views


urlpatterns = [
        path("create/", views.create_task, name="create_task"),
        path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
        path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
        path("show/<int:task_id>/", views.show_task, name="show_task"),
        ]


