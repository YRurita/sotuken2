import sys
import os
import pprint
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from manager.models import *

path_face = os.getcwd()
sys.path.append(path_face + "\\manager\\face_recognition")
pprint.pprint(sys.path)

from main import main


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    #main()

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        #main()
        f = open("manager/face_recognition/name_list/name_list.txt", "r")
        data = f.read() 
        f.close()
        test = "camera"  
        context['data'] = data  # 入れ物に入れる
        context["test"] = test
        return render(self.request, self.template_name, context)
    
