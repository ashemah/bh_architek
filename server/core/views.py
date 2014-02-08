from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from builder.client import BuilderClient
from core.models import App, Service


class HomeView(View):

    def get(self, request, *args, **kwargs):

        app_name = request.GET.get('app')
        cmd = request.GET.get('cmd', None)

        app = App.objects.get(short_name=app_name)

        client = BuilderClient('192.168.56.1', 10001)

        service_list = app.service_list()

        res_info = {}

        if cmd is None or cmd == 'status':
            res_info = client.status(service_list)
            Service.update_from_info(res_info)

        if cmd == 'build':

            res_info = client.build(app_name, service_list)
            Service.update_from_info(res_info)

        if cmd == 'start':
            res_info = client.start(app_name, service_list)
            Service.update_from_info(res_info)

        if cmd == 'stop':
            res_info = client.stop(app_name, service_list)
            Service.update_from_info(res_info)

        if cmd == 'remove':
            res_info = client.remove(app_name, service_list)
            Service.update_from_info(res_info)

        return HttpResponse(str(res_info))