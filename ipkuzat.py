# IPkuzat

# Author - Shoirjon Mamazokorov

# github - https://github.com/Shoirjon1

# Mualliflik huquqini buzmang!

import json
import urllib.request
import webbrowser
import os
import pyfiglet
from termcolor import colored
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        
        print (CY+"""  mmmm  #               "              "
 #"   " # mm    mmm   mmm     m mm   mmm    mmm   m mm
 "#mmm  #"  #  #" "#    #     #"  "    #   #" "#  #"  #
     "# #   #  #   #    #     #        #   #   #  #   #
 "mmm#" #   #  "#m#"  mm#mm   #        #   "#m#"  #   #
                                       #
                                     ""
  """+Y+"""v1.1"""+G+"""

             
      IP Manzil kuzatuvchisi

"""+R+""">>"""+Y+"""----"""+CY+"""        Daturchi- Shirjon_No1 """+Y+"""----"""+R+"""<<""")
        
    def m3():
        try:
            print(R+"""\n
#"""+Y+"""         Ishni boshlymizmi?"""+G+""" >>"""+Y+"""

  1)"""+G+""" SizningIP haqida malumot"""+Y+"""
  2)"""+G+""" IP addresini tekshiruv"""+Y+"""
  3)"""+G+""" Orqaga/Chiqish
""")
            ch=int(input(CY+"     Nima qilamiz tanlang ❯❯  "+W))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                print(Y+"Dasturdan foydalanganingiz uchun raxmat. Agar sizda muammo bo'lsa T.me/Shoirjon_No1_1 telegram guruxida muhokama qilishimiz mumkun"+W)
            else:
                print(R+"\nYaroqsiz tanlov!  Iltimos, yana bir bor urinib ko'ring\n")
                m3()
        except ValueError:
            print(R+"\nYaroqsiz tanlov!  Iltimos, yana bir bor urinib ko'ring\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(Y+'\n>>>'+CY+' IP manzili tafsilotlari\n ')
                print(G+"1) IP manzili : "+Y,data['query'],'\n')
                print(G+"2) Org : "+Y,data['org'],'\n')
                print(G+"3) Shaxar : "+Y,data['city'],'\n')
                print(G+"4) Mintaqa : "+Y,data['regionName'],'\n')
                print(G+"5) Mamlakat : "+Y,data['country'],'\n')
                print(G+"6) Manzil\n")
                print(G+"\tKenglik : "+Y,data['lat'],'\n')
                print(G+"\tUzunlik : "+Y,data['lon'],'\n')
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print(R+"\n#"+Y+" Google xaritasi havolasi : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" Havola brauzerda ochilsinmi?"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nBoshqa IP-ni tekshiring yoki Ctrl + C yordamida chiqing\n\n")
                        start()
                        m3()
                    else:
                        print("\nYaroqsiz tanlov!  Iltimos, yana bir bor urinib ko'ring\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" Havola brauzerda ochilsinmi?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(Y+"\nBoshqa IP-ni tekshiring yoki  "+R+"Ctrl + C ni boing\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\nYaroqsiz tanlov!  Iltimos, yana bir bor urinib ko'ring\n")
                        m3()
                return
            except KeyError:
                print(R+"\n   Xato!  IP/veb-sayt manzili noto'g'ri!\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" Iltimos, internet aloqangizni tekshiring!\n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+"IP-manzil/veb-sayt manzilini kiriting:"+W+" ")
        if u=="":
            print(R+"\nYaroqli IP-manzil/veb-sayt manzilini kiriting!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nTo'xtatildi!  Kuningiz xayrli o'tsin :)"+W)
