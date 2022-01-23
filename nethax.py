pName = "netHax"
pDescription = "Nethacking Toolbox"
pAuthor = "DaBlincx"
pSource = "https://www.github.com/DaBlincx/nethax"
pVersion = 1.3
debugMode = False



moduleslib = []

try: from lists import *
except: moduleslib.append("please download lists.py from the github repo \nand save it in the same folder as this python script\n")

try: import pyfiglet
except: moduleslib.append("pyfiglet")

try: from rich.console import Console
except: moduleslib.append("rich.console (rich)")

try: from rich.progress import Progress,track
except: moduleslib.append("rich.progress (rich)")

try: from rich.panel import Panel
except: moduleslib.append("rich.panel (rich)")

try: from rich.prompt import *
except: moduleslib.append("rich.prompt (rich)")

try: from os import walk
except: moduleslib.append("os")

try: import time
except: moduleslib.append("time")

try: import subprocess
except: moduleslib.append("subprocess")

try: import random
except: moduleslib.append("random")

try: import string
except: moduleslib.append("string")

try: from sys import *
except: moduleslib.append("sys")

    
def importError():
    print("Cannot import all needed librarys, \nplease make sure to have every one installed.\n\nUsage: 'pip install [module]' or 'pip3 install [module]'\n")
    print("modules:")
    for modl in moduleslib:
        print(modl)
    print()
    exit()

try: con = Console()
except: importError()


def initializer():
    for x in track(range(25),"Initializing..."):
        time.sleep(0.1)

def mainMenu():
    for i in range(250):
        print()
    try: banner = pyfiglet.figlet_format(f"  {pName}  ",font="banner3-D")
    except: importError()
    # then printing that out with rich console and a little intro
    con.print(":"*75,style="bold green")
    con.print(banner+":"*75+"\n",style="bold green")
    con.print(Panel(f"\n{pDescription}\n",style="bold green"))
    print()
    con.print(Panel("1. Web App Hacking\n\n2. Phishing Attack\n\n3. MITM Attack\n\n4. WIFI Hacking\n\n5. Info\n\n6. Exit Program"),style="bold green")

    answer = IntPrompt.ask("Which one do you pick? ",choices=['1','2','3','4','5','6'])
    if answer == 1:
        web_hacking()
    if answer == 2:
        phishingAttack()
    if answer == 3:
        MITM()
    if answer == 4:
        WiFi()
    if answer == 5:
        showInfo()
    if answer == 6:
        exitProgram()

def web_hacking():
    initializer()
    ltf = "./webkey"
    ltfget = []
    dt = []
    url = Prompt.ask("Enter the website's url: ")
    for i in track(range(100),f"Gathering information on {url}"):
        time.sleep(0.1)
    with Progress(transient=True) as prog :
        exploiting = prog.add_task("Exploiting the website",total=500)
    while not prog.finished:
        prog.update(exploiting,advance=0.9)
    for x in walk(ltf):
        dmp = str(x).split(", [",1)
        ul = f"{url}"+dmp[0][3:-1].replace(" ","")
        fl = dmp[1][3:-1].replace(" ","")
        ulflstr = f" URL: {ul}\n Files: {fl}"
        con.print(f"\n\nExploiting: \n{ulflstr}",style="green")
        ltfget.append(ulflstr)


    with Progress(transient=True) as prog :
        decoding = prog.add_task("Cracking the passwords",total=300)
    while not prog.finished:
        prog.update(decoding,advance=0.1)
    for l in ltfget:
        con.print(f"\n\nCracking passwords: \n{l}",style="green")


    with Progress(transient=True) as prog :
        dumping = prog.add_task("Dumping plain text passwords",total=900)
    while not prog.finished:
        prog.update(dumping,advance=0.2)
    f = open("pw_dump.txt","w",encoding="UTF-8")
    for l in ltfget:
        con.print(f"\n\nDumping: \n{l}",style="green")
        f.write(str(l)+"\n")
    f.close
    
    menuReq()

def phishingAttack():
    initializer()
    con.print(Panel("1. SMS-Phishing"),style="bold green")
    con.print(Panel("2. Email Phishing"),style="bold green")
    phishMethod = IntPrompt.ask("Which one do you pick? ",choices=['1','2'])
    if phishMethod == 1:
        phoneCount = IntPrompt.ask("How many phone numbers should be attacked via phishing? ",choices=['1','2','3','4','5'])
        
        phoneSms = []
        for nrnumb in range(0,phoneCount):
            phoneSms.append(Prompt.ask(f"{nrnumb+1}. number: "))
        for numberSms in phoneSms:
            for i in track(range(100),f"Gathering information on {numberSms} and bypassing blocked numbers."):
                time.sleep(0.1)
        print("")
        for numberSms in phoneSms:
            for i in track(range(100),f"Sending phishing links for facebook, linkedin, twitter, youtube and instagram to {numberSms} "):
                time.sleep(0.1)
        emailforaccs = Prompt.ask(f"\nPlease enter you email adress to log phished account details: ")

    menuReq()

def MITM():
    initializer()

    con.print(Panel(f"\nCurrently, this feature does not exist.\nPlease try again later.\n"),style="bold green")

    menuReq()

def getWifis():

    newplatform = platform

    if debugMode == True:
        print("Your current plattform is " + platform + "\nChange it? ")
        newplatform = Prompt.ask("Linux / MacOS / Windows\nlinux / darwin / win32",choices=['linux','darwin','win32'])


    if newplatform == "linux" or newplatform == "linux2":
        print("linux")
        con.print(Panel("\nWiFi Hacking is currently not supported on linux.\nPlease try again on another version.\n"),style="bold green")
        menuReq()
    elif newplatform == "darwin":
        print("macos")
        scan_cmd = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        scan_out, scan_err = scan_cmd.communicate()
    elif newplatform == "win32":
        print("windows")
        con.print(Panel("\nWiFi Hacking is currently not supported on Windows.\nPlease try again on another version.\n"),style="bold green")
        menuReq()


    

    if str(scan_err) == "b''":
        errnoo = True

    if str(scan_out) != "b''":
        scan_out_lines = scan_out.decode("ascii")
        scan_out_data = []
        scan_out_lines = str(scan_out).split("\\n")[1:-1]
        for each_line in scan_out_lines:
            split_line = [e for e in each_line.split("  ") if e != ""]
            split_line.pop()
            split_line.pop()
            split_line.pop()
            if split_line[0].startswith(" ") == True:
                temp = split_line[0]
                temp = temp[1:]
                split_line = temp
            else:
                split_line = split_line[0]
            scan_out_data.append(split_line)
            f = open("wifi_dump.txt","w",encoding="UTF-8")
            n=0
            for network in scan_out_data:
                n+=1
                ntwrk = network[:-3]
                netwrk = ntwrk.rsplit(" ",2)
                netdisplay = "SSID: " + netwrk[0] + (" "*(36-len(netwrk[0]))) + " | MAC-Address: " + netwrk[1]
                f.write(f"{n}. {netdisplay}\n")
            f.close
        return scan_out_data

def WiFi():
    initializer()

    try: 
        scdata = getWifis()
    except: 
        wifiError()
    print(scdata)
    n=0
    if scdata != None:
        for i in range(250):
            print()
        for network in scdata:
            n+=1
            ntwrk = network[:-3]
            netwrk = ntwrk.rsplit(" ",2)
            netdisplay = "SSID: " + netwrk[0] + (" "*(36-len(netwrk[0]))) + " | MAC-Address: " + netwrk[1]
            con.print(Panel(f"{n}. {netdisplay}"),style="bold green")
        
        chsc = []
        for i in range(1,n+1):
            chsc.append(str(i))
        answer = IntPrompt.ask("Select network to hack: ",choices=chsc)
        ntwrkf = scdata[answer-1][:-3]
        netwrkf = ntwrkf.rsplit(" ",2)
        netssid = netwrkf[0]
        netmac = netwrkf[1]
        for i in range(250):
            print()
        for i in track(range(100),f"Gathering information from {netssid}"):
            time.sleep(0.1)
        con.print(Panel(f"1. 4800 pwlist.txt - wordlist"),style="bold green")
        con.print(Panel(f"2. Bruteforcing method"),style="bold green")
        con.print(Panel(f"3. HTTP-Cracking"),style="bold green")
        crackmethod = IntPrompt.ask("Select cracking method: ",choices=['1','2','3'])

        print("\n")
        for i in track(range(10),f"Initializing..."):
            time.sleep(0.1)
        print("\n\n")

        S = random.randint(8,32)

        if crackmethod == 1:
            tim = len(pwlist)
            netpwd = random.choice(pwlist)
            print("\n")
            pwl = 0
            hjb = 0
            for pw in pwlist:
                time.sleep(0.01)
                hjb += 1
                print(f"{hjb}/{len(pwlist)} | Trying {pw}")
                if pw == netpwd:
                    for i in range(250):
                        print()
                    print("Success!\n")
                    break

        

            if netpwd == "charisma":
                retri = Prompt.ask("Password could not be found, retry? ",choices=['y','n'])
                if retri == "y":
                    rerunWifi()
                if retri == "n":
                    print("\n")
                    mmnue = Prompt.ask("Back to main menu? ",choices=['y','n'])
                    if mmnue == "y":
                        mainMenu()
                    if mmnue == "n":
                        exit()

        if crackmethod == 2:
            timedr = random.randint(1,1000)
            for i in track(range(1,timedr),f"Bruteforcing..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))

        if crackmethod == 3:
            for i in track(range(100),f"Sending http requests..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
            for i in track(range(50),f"Retrieving information..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))

        con.print(Panel(f"\n  SSID: {netssid}\n\n  MAC-Address: {netmac}\n\n  Passphrase: {netpwd}\n"),style="bold green")

        menuReq()
    else:
        wifiError()

def showInfo():
    print()
    con.print(Panel(f"\n   Information\n   -----------------------------------------------------\n   Name:          {pName}\n   Description:   {pDescription}\n   Author:        {pAuthor}\n   Source Code:   {pSource}\n   Version:       {pVersion}\n   Debug Mode:    {debugMode}\n"),style="bold green")
    menuReq()

def rerunWifi():
    WiFi()

def wifiError():
    print("\nError: Code could not be executed, because WLAN is disabled.\nPlease enable Wifi connections, so this code can be execuded.")
    menuReq()

def menuReq():
    print()
    mmnue = Prompt.ask("Back to main menu? ",choices=['y','n'])
    if mmnue == "y":
        mainMenu()
    if mmnue == "n":
        exitProgram()

def exitProgram():
    con.print(Panel("\n  Thanks for using!\n"),style="bold green")
    exit()



mainMenu()