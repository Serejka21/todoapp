from django.urls import path

from core.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        mark_as_done,
                        mark_as_undo,
                        TagListView,
                        TagUpdateView,
                        TagDeleteView,
                        TagCreateView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/",
         TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/edit/",
         TaskUpdateView.as_view(), name="task-edit"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/mark-as-done/",
         mark_as_done,
         name="task-done"),
    path("task/<int:pk>/mark-as-undo/",
         mark_as_undo,
         name="task-undo"),
    path("tags/",
         TagListView.as_view(),
         name="tag-list"),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"),
    path("tags/<int:pk>/edit/",
         TagUpdateView.as_view(),
         name="tag-edit"),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"),

]

app_name = "core"
