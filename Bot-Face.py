from fbchat import Client
from fbchat.models import *
import getpass,os,sys
from time import sleep
from termcolor import colored
"""
GReETz 2 Dj3Bb1RaN0n && BLACK-HACKER
 
"""
def slowprints1(slow):
        for slowprint in slow +"\n":
            sys.stdout.write(slowprint)
            sys.stdout.flush()
            sleep(3./90)

try:
        
    sleep(1)
    os.system("clear && clear")
    linux = sys.platform
    sleep(1)
    print("Checking Operation System !")
    sleep(1)
    if "linux" not in linux :
            print("\n")
            slowprints1(colored("Linux is Required ","red"))
            slowprints1(colored("Microsoft Sucks =)","white"))
            print("\n")
            sys.exit(127)
    else :
        slowprints1(colored("[*] LINUX CONFIRMED ",'green'))    
        sleep(1)
    os.system("clear && clear")
    _email = raw_input('\n                                 USERNAME/EMAIL : ')
    _password = getpass.getpass(prompt='\n                                 PASSWORD : ', stream=None)
    print("\n")
    client = Client(_email, _password)
    friend_name = raw_input(colored(text="\n                                 FRIEND NAME ~# ", color="green"))
    friend_id = raw_input(colored(text="\n                                 FRIEND ID/USERNAME ~# ", color="green"))
    friends = client.searchForUsers(friend_name)
    friend = friends[0]
    uid = friend.uid
    sleep(1)
    slowprints1(colored("WELCOME ...","white"))
    sleep(1)
    def check():
        raw_input('Click Enter to Continue ')
    def clear():
        os.system('clear && clear')
    
    def main():

        def banner():
                os.system("clear && clear")
                print("\n")
                print(colored("                          ____  ____  ______            _________   ____________","red"))
                print(colored("                         / __ )/ __ \/_  __/           / ____/   | / ____/ ____/", "red"))
                print(colored("                        / __  / / / / / /    ______   / /_  / /| |/ /   / __/   ", "red"))
                print(colored("                       / /_/ / /_/ / / /    /_____/  / __/ / ___ / /___/ /___  ", "red"))
                print(colored("                      /_____/\____/ /_/             /_/   /_/  |_\____/_____/", "red"))
                print(colored("\n                                       CODED BY : ""B14ck_DZ             ", "red"))

                print(colored("""\n       
                                            1) MESSAGE
                                            2) IMAGE
                                            3) FILE
                                            4) CHANGE NICKNAME
                                            5) BLOCK USER
                                            6) DELETE MESSAGE
                                            7) FETCH USERS
                                            8) REMOVE FRIEND
                                            00) LOGOUT & EXIT\n""",'blue'))

        banner()


        def sendMessage():
                print ("To Return Press")
                print (colored("CTRL + C\n","red"))
                while True:
                    try:
                        print("")
                        messageis = raw_input("MESSAGE ~# ")
                        client.sendMessage(message=messageis,thread_id=friend_id,thread_type=ThreadType.USER)
                    except KeyboardInterrupt:
                        sleep(1)
                        clear()
                        main()


        def sendImage():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    image_dir = raw_input("IMAGE PATH ~# ")
                    msg = raw_input("MESSAGE ~# ")
                    client.sendLocalImage(message=msg,image_path=image_dir,thread_id=friend_id,thread_type=ThreadType.USER)
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()

        def sendFile():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    file_dir = raw_input("FILE PATH ~# ")
                    msg = raw_input("MESSAGE ~# ")
                    client.sendLocalFiles(message=msg, file_paths=file_dir, thread_id=friend_id,thread_type=ThreadType.USER)
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()

        def changeNick():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    new_nick = raw_input("NICKNAME ~# ")
                    client.changeNickname(nickname=new_nick,thread_id=friend_id,user_id=friend_id,thread_type=ThreadType.USER)
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()
        def blockUser():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    userID = raw_input("USER ID ~# ")
                    client.blockUser(user_id=userID)
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()
        def deleteMSG():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    messageID = raw_input("MESSAGE ID ~# \n")
                    client.deleteMessages(message_ids=[messageID])
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()

        def fetchUsers():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    client.fetchAllUsers()
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()

        def delFriend():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    userID = raw_input("\nUSER ID ~# ")
                    client.removeFriend(friend_id=userID)
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()

        def searchForUsers():
            print ("To Return Press")
            print (colored("CTRL + C\n", "red"))
            while True:
                try:
                    print("")
                    name = raw_input("NAME ~# ")
                    client.searchForUsers(name=name,limit=10)
                except KeyboardInterrupt:
                    sleep(1)
                    clear()
                    main()

        def logout():
            checkIF = client.isLoggedIn
            client.logout()
            sleep(1)
            slowprints1(colored("\nLOGOUT DONE !","green"))
            sleep(1)
            slowprints1(colored("SHUTING DOWN ...\n","red"))
            exit(0)
        
        b14 = raw_input("~# ")
        if b14 == "1":
            sendMessage()
        elif b14 == "2":
            sendImage()
        elif b14 == "3":
            sendFile()
        elif b14 == "4":
            changeNick()
        elif b14 == "5":
            blockUser()
        elif b14 == "6":
            deleteMSG()
        elif b14 == "7":
            fetchUsers()
        elif b14 == "8":
            delFriend()
        elif b14 == "00":
            logout()
        else:
            sleep(1)
            print(colored("Select Again !","red"))
            sleep(1)
            main()
    main()

except KeyboardInterrupt:
    sleep(1)
    slowprints1(colored("\nSHUTING DOWN ...\n","red"))