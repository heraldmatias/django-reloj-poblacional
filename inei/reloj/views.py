# -*- coding: utf-8 -*-
import json
from django.views.generic import TemplateView
from django.http.response import Http404, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from inei.reloj.api import Api, intWith
from inei.reloj.constants import POPULATION

__author__ = 'holivares'


class IndexView(TemplateView):
    template_name = 'reloj/reloj.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(*kwargs)
        api = Api(2014)
        ctx['population_initial'] = intWith(' ', POPULATION)
        ctx['elapsed_time'] = api.get_elapsed_time()
        return ctx


class PopulationView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # if not request.is_ajax():
        #     raise Http404("Only ajax.")
        return super(PopulationView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        api = Api(2014)
        data = {
            'elapsed_time': api.get_elapsed_time(),
            'population': intWith(' ', api.get_estimated_population()),
            'success': True
        }
        response = HttpResponse(json.dumps(data), content_type="application/json")
        return response

    def get(self, request, *args, **kwargs):
        api = Api(2014)
        data = {
            'elapsed_time': api.get_elapsed_time(),
            'population': intWith(' ', api.get_estimated_population()),
            'success': True
        }
        response = HttpResponse(json.dumps(data), content_type="application/json")
        return response