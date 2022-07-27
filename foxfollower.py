from os import name , system , path , stat
from requests import session 
from json import dump , load
from random import choice 
Session = session()
sesnumid = session()
adet = 0

UserAgents = [
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"

]


Ascii = """\033[96m
    ______     _  __    ______      ____                       
   / ____/___ | |/ /   / ____/___  / / /___ _      _____  _____
  / /_  / __ \|   /   / /_  / __ \/ / / __ \ | /| / / _ \/ ___/
 / __/ / /_/ /   |   / __/ / /_/ / / / /_/ / |/ |/ /  __/ /    
/_/    \____/_/|_|  /_/    \____/_/_/\____/|__/|__/\___/_/     
    
    \033[93mCoded By \033[94m→\033[2;31;5m b4rc0d\033[0;m  \033[93mChannel \033[94m→ \033[2;31;5m@BlackFoxSecurityTeam\033[0;m
"""


def clear(): 
    if name == 'nt':
        system('cls') # Cleaning the terminal in Windows
    elif name == 'posix':
        system('clear') # Cleaning the terminal in Linux&Unix base

def Login():

    username = input("FoXFoLLoWer\033[2;31;5m( UserName )\033[0;m > \033[96m") # UserName account 
    password = input("\033[0;mFoXFoLLoWer\033[2;31;5m( UserName )\033[0;m > \033[96m") # PassWord account 

    Session.headers ={
        "User-Agent": choice(UserAgents) # Random user agent
    }

    data = Session.get("https://igfollower.net/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")

    Session.headers.update(
        {
            "Referer": "https://igfollower.net/girisyap"
        }
    )

    login = Session.post(
            "https://igfollower.net/girisyap?",
            data={
                "username":username,
                "password":password
            }
        ).json()
        
    # print(login)

    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul \033[91m;)")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mUnsuccessFul :(\033[0m")
        Login()
    
    cockies = data.cookies.items()[0]
    data = Session.get("https://igfollower.net/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    
    Session.headers.update(
            {
                cockies[0]: cockies[1]
            }
        )  

    with open('sessions/cookies.txt', 'w+') as file:
        dump(Session.cookies.get_dict(), file)
    with open('sessions/headers.txt', 'w+') as file:
        dump(Session.headers, file)


def Subsidiary():
    with open('sessions/cookies.txt', 'r') as file:
        Session.cookies.update(load(file))
    with open('sessions/headers.txt', 'r') as file:
        Session.headers = load(file)

def FindeNumId(username):
    
    sesnumid.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"}
    data = sesnumid.get("https://commentpicker.com/instagram-user-id.php")
    sesnumid.headers.update({"Referer": "https://commentpicker.com/instagram-user-id.php"})
    data = sesnumid.get('https://commentpicker.com/actions/token.php?id=secret')
    # print(data.text)
    data = sesnumid.get(f"https://commentpicker.com/actions/instagram-id-action.php?username={username}&token={data.text}")
    # print(data.text)
    id = data.json()['id']
    return id

def Sender():
    User = input("\033[93mTar-User \033[32m→\033[96m ")
    Number = int(input("\033[93mNumber \033[32m→\033[96m "))
    global adet
    adet += Number
    numId = FindeNumId(User)
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer \033[93m]\033[96m───────────────")
    while(adet >= 0 ):
        data = Session.post(
                f"https://igfollower.net/tools/send-follower/{numId}?formType=send" ,
                data={
                    "adet":Number,
                    "userID":numId,
                    "userName":User
                }
            ).json()
        
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['message']}")

        if adet == 1:
            adet -= 1
        else :
            adet -= 2
    print("\033[96m──────────────────────────────────────────────")



clear()
print(Ascii)
if(path.exists("sessions/cookies.txt") == True ) and (stat("sessions/cookies.txt").st_size > 0) and (path.exists("sessions/headers.txt") == True) and (stat("sessions/headers.txt").st_size > 0):
    Subsidiary()
    Sender()
else:   
    Login()
    Sender()
        


