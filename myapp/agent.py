#!/usr/bin/env python
#coding:utf-8
import httplib
import urllib
import  psutil
cpucount=psutil.cpu_count()
boottime=psutil.boot_time()
server_info={
'cpu_count':1,
'boot_time':2,

}
def RequestUrl(host,port,source,params,timeout):
	headers={"Content-type":"application/json"}
	try:
		conn=httplib.HTTPConnection(host,port,timeout)
		conn.request('POST',source,params,headers)
		response=conn.getresponse()
		original=response.read()
		print original
	except Exception,e:
		raise
	return original
requestdata=urllib.urlencode({'data':server_info})
result=RequestUrl('127.0.0.1','8888','/postdata/',requestdata,20)

print "=============%s======"%result

