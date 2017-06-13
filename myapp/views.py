# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from BBS.sql_helper import exam_page,Show_Page,html_page,Gen_Code
import sys
import models


from models import News
from django.shortcuts import HttpResponse,render,render_to_response,HttpResponseRedirect
reload(sys)
sys.setdefaultencoding('utf-8')
def index(request,page):
    ret = {}
    per_item = exam_page(request.COOKIES.get('page_num', 10), 10)
    page = exam_page(page)
    total = News.objects.all().count()
    show = Show_Page(page, total, per_item)
    data = News.objects.all()[show.start():show.end()]
    count = News.objects.all()[show.start():show.end()].count()
    list_string = html_page(page, show.get_pages())
    ret['data'] = data
    ret['count'] = count
    ret['totalpage'] = show.get_pages()
    # ret['page_idx']=page_idx
    gencode = Gen_Code(5)
    validate_code = gencode.simple_code()
    request.session['code']=validate_code
    ret['code']=validate_code
    ret['all_html'] = list_string
    response = render_to_response('index.html', ret)
    response.set_cookie('page_num', per_item)

    return response
# Create your views here.


def addfavor(request):
    id=request.POST.get('nid')
    newsobj=models.News.objects.get(id=int(id))
    temp=newsobj.favor_count+1
    newsobj.favor_count=temp
    newsobj.save()
    return HttpResponse(temp)

def validate(request):
    post_code=request.POST.get['check_code']
    if hasattr(request,'session'):
        session_code=request.session.get('code')
        if post_code==session_code:
            return HttpResponse('hello.html')
        else:
            return HttpResponse('error')
    else:
        return HttpResponse('session doesnot')