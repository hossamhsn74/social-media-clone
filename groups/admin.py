from django.contrib import admin
from groups.models import Group, GroupMember

admin.site.register(Group)


class GroupMemeberInline(admin.TabularInline):
    model = GroupMember
