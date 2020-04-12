from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from groups.models import Group, GroupMember
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import IntegrityError


class GroupCreateView(CreateView):
    model = Group
    fields = ('name', 'descreption')
    template_name = "groups/group_form.html"


class GroupListView(ListView):
    model = Group
    template_name = "groups/group_list.html"


class GroupDetailView(DetailView):
    model = Group
    template_name = "groups/group_detail.html"


class joinGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning!, already a memeber!')
        else:
            messages.success(self.request, 'you are a memeber now')
        return super().get(request, *args, **kwargs)


class leaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user=self.request.user, group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request, 'Sorry, you are not a member of this group!')
        else:
            membership.delete()
            messages.success(self.request, 'you left the group now')
        return super().get(request, *args, **kwargs)
