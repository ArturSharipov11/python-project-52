from django.forms.forms import BaseForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView
from .models import Task
from .forms import TaskForm
from .filters import TasksFilter
from task_manager.mixins import NoAuthMixin, NoPermissionMixin


class IsAuthorTask(UserPassesTestMixin):
    index_url = reverse_lazy('tasks')
    error_message = _('Only its author can delete a task')

    def test_func(self) -> bool | None:
        task = self.get_object()
        return self.request.user == task.author


class IndexTasks(NoPermissionMixin, NoAuthMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks.html'
    filterset_class = TasksFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)

        return context


class CreateTask(NoPermissionMixin, NoAuthMixin, SuccessMessageMixin,
                 CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form: BaseForm):
        form.instance.author = self.request.user

        return super().form_valid(form)


class UpdateTask(NoPermissionMixin, NoAuthMixin, SuccessMessageMixin,
                 UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')


class DeleteTask(NoPermissionMixin, NoAuthMixin, IsAuthorTask,
                 SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted successfully')


class ShowTask(NoPermissionMixin, NoAuthMixin, DetailView):
    model = Task
    template_name = 'tasks/view_task.html'
    context_object_name = 'task'
