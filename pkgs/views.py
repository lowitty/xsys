#encoding=utf-8
from django.shortcuts import render
import json
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader

from com.egx.wh.common.mopexpect import MoWhApi

def index(request):
    template = loader.get_template('pkgs/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def getStrCmd(request):
    s_cmd = str(json.loads(request.body)["scmd"])
    mo_se = MoWhApi("/srv/installed/moshell/moshell", "/srv/installed/jdk1.8.0_45/bin/java", "/srv/tmp/dpkg.zip")
    mo_se.connect()
    cmd_ret = mo_se.sendCmd(s_cmd)
    mo_se.close()
    
    return JsonResponse({"ret_str" : cmd_ret})
    #return HttpResponse("Hello, world. You're at the polls index.")
    