import datetime
from datetime import timezone

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/index.html"
    ordering = ["-done"]


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:task-list")


class TagListView(generic.ListView):
    model = Tag
    ordering = ["name"]


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")


def mark_as_done(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    task.done = True
    task.save()
    return HttpResponseRedirect(
        request.META.get(
            "HTTP_REFERER",
            reverse_lazy(viewname="core:task-list"))
    )


def mark_as_undo(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    task.done = False
    task.save()
    return HttpResponseRedirect(
        request.META.get(
            "HTTP_REFERER",
            reverse_lazy(viewname="core:task-list"))
    )
