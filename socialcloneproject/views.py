from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='index.html'

class thanksView(TemplateView):
    template_name = "thanks.html"

class testView(TemplateView):
    template_name = "test.html"

