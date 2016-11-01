from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    """
    Home page
    """
    template_name = 'index.html'


class MeetingsView(generic.TemplateView):
    """
    Meetings we are
    """
    template_name = 'meetings.html'


class MembersView(generic.TemplateView):
    """
    Information for members page
    """
    template_name = 'members.html'


class HistoryView(generic.TemplateView):
    """
    Our history page
    """
    template_name = 'history.html'


class PartnersView(generic.TemplateView):
    """
    Partners and Sponsors page
    """
    template_name = 'partners.html'


class ProjectsView(generic.TemplateView):
    """
    Projects list page
    """
    template_name = 'projects.html'


class ContactView(generic.TemplateView):
    """
    Contact page
    """
    template_name = 'contact.html'

