from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from groups.models import Group, GroupMember


class GroupCreateView(CreateView):
    model = Group
    fields = ('name', 'descreption')
    template_name = "group_form.html"


class GroupListView(ListView):
    model = Group
    template_name = "group_list.html"

class GroupDetailView(DetailView):
    model = Group
    template_name = "group_detail.html"

