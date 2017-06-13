#!/usr/bin/env  python
#coding:utf-8
__author__='jianwei'
import random
from django.utils.safestring import mark_safe
def exam_page(page,default=10):
    try:
        page=int(page)
    except Exception:
        page=int(default)
    return page


class Show_Page:
    def __init__(self,page,total_item,item_perpage=10):
        self.page=page
        self.total_item=total_item
        self.item_perpage=item_perpage

    def start(self):
        start_item=(self.page-1)*self.item_perpage
        return start_item
    def end(self):
        end_item=self.page*self.item_perpage
        return end_item
    def get_pages(self):
        res=divmod(self.total_item,self.item_perpage)
        if res[1]==0:
            total_page=res[0]
        else:
            total_page=res[0]+1
        return total_page



def html_page(page,totalpage):
    page_html=[]
 #   page_idx = mark_safe('<a href="/myapp/fenye/1">1</a>')
    if page <= 1:
        priv_page = '<a href="#">上一页<a/>'
    else:
        priv_page = '<a href="/index/%d">上一页</a>' % (page - 1)
    page_html.append(priv_page)
    '''
    if page-5<=0:
        start1=0
    else:
        start1=page-6
    if page+5>totalpage:
        end1=totalpage
    else:
        end1=page+5
      '''
    if totalpage <= 11:
        start1 = 0
        end1 = totalpage
    else:
        if page < 6:
            start1 = 0
            end1 = 11
        else:
            start1 = page - 6
            end1 = page + 5
            if page + 5 > totalpage:
                start1 = totalpage - 11
                end1 = totalpage

    for i in range(start1, end1):
        #    for i in range(totalpage):
        if page == i + 1:
            a_html = '<a style="color:red" href="/index/%d">%d</a>' % (i + 1, i + 1)
        else:
            a_html = '<a href="/idnex/%d">%d</a>' % (i + 1, i + 1)
        page_html.append(a_html)
    if page >= totalpage:
        next_page = '<a href="#">下一页</a>'
    else:
        next_page = '<a href="/index/%d">下一页</a>' % (page + 1)
    page_html.append(next_page)
    page_string=mark_safe(' '.join(page_html))
    return page_string

class Gen_Code:
    def __init__(self,count=4):
        self._count=count
        self.num=''.join(map(str,range(10)))
        self.upperstr=''.join(map(str,[chr(i) for i in range(65,91)]))
        self.lowerstr=''.join(map(str,[chr(i) for i in range(65,91)])).lower()
        self.code_pool=''.join((self.num,self.upperstr,self.lowerstr))
    def simple_code(self):
        self.val_code=random.sample(self.code_pool,self._count)
        return ''.join(self.val_code)


#class MyMiddleware(object):
 #   def process_request(self):