__author__ = 'FRAMGIA\le.cong.phuc'
from django.views.generic import TemplateView


class BaseIndexView(TemplateView):
    template_name = 'index.html'
