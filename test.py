#!/usr/bin/python 

import urllib
import requests
#登录的主页面 
hosturl = 'http://172.16.2.137:8088' 
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据） 
posturl = 'http://172.16.2.137:8088/ClientBin/SFuture.BrightDairy.Silverlight.xap' 

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie 
cj = cookielib.LWPCookieJar() 
cookie_support = urllib2.HTTPCookieProcessor(cj) 
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
urllib2.install_opener(opener) 
  
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功） 
h = urllib2.urlopen(hosturl) 
  
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。 
headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 
   'Referer' : 'http://172.16.2.137:8088/ClientBin/SFuture.BrightDairy.Silverlight.xap'} 
#构造Post数据，他也是从抓大的包里分析得出的。 
postData = {#'op' : 'dmlogin', 
   #'f' : 'st', 
   'UserCode' : 'lin_peina', 
   'Password' : 'lpn2013', 
  # 'rmbr' : 'true', //特有数据，不同网站可能不同 
 #  'tmp' : '0.7306424454308195' //特有数据，不同网站可能不同 
  
   } 
  
#需要给Post数据编码 
postData = urllib.urlencode(postData) 
  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程 
request = urllib2.Request(posturl, postData, headers) 
print (request) 
response = urllib2.urlopen(request) 
text = response.read() 
print(text)
