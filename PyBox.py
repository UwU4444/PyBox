# By: Youssef Ahmed
# C: Egypt
# Py; PY3
import sys
import time
import os
import webbrowser
import socket
import requests
import random
class Dev_Style():
    class Hack_Mode():
        def Loading(TEXT, MSG_LOAD):
            sleep=time.sleep
            for i in range(0, 2-1):
                print(TEXT, '  ', '[  -  ]', end='\r')
                sleep(0.3)
                print(TEXT, '  ', '[  |  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  -  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  |  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  -  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  |  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  -  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  |  ]', end='\r')
                sleep(0.2)
                print(TEXT, '  ', '[  -  ]', end='\r')
                sleep(0.2)
            print(MSG_LOAD, '    ', '[  +  ]')
        def GET_PUBLIC_IP():
            ip=requests.get('https://ifconfig.me').text
            return ip
        def GET_PC_NAME():
            PC=socket.gethostname()
            return PC
        def GET_IP_CONFIG():
            PC_IP=socket.gethostbyname(socket.gethostname)
        def Command(command):
            os.system(command)
        def W_System():
            if sys.platform in ['win32', 'win64']:
                platform='Win'
                return platform
            elif sys.platform in ['linux', 'linux2']:
                platform='linux'
                return platform
            else:
                platform='<-->'
                return platform
        def Token_Generator(Range):
            Token=''
            char='AABCVSFGNMKWOLSITsdakfmewiacn'
            for i in range(Range):
                Token += random.choice(char)
            return Token
        def Main_Hack():
            try:
                import requests
            except ImportError:
                os.system('pip install requests')
        def Write_Script(ScriptName , Text):
            File=open(ScriptName, 'a')
            File.write('''%s''' %Text)
    class HTML_MODE():
        def h1(Text):
            print (Text)
        def input(Text, id):
            id=id
            id=input(Text)
            return id
        def script(scr, Mode, Text=''):
            if Mode == 'r':
                scrp=open(scr, 'r')
                scrp.read()
            elif Mode == 'w' or Mode == 'a':
                scrp=open(scr, 'a')
                scrp.write(Text)
            else:
                msg='[!] Error Format'
        def div(id, Md_raw):
            id=id
            def id():
                Md_raw
        def a_herf(link):
            webbrowser.open(link)
