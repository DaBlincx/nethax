# 
# This script can be used to trick people into thinking, that you are a hacker.
# This is not a real hacking tool and should not be interpreted as one.
# 
# Licensed under the GNU General Public License v3.0
# 
# 2022 | Copyleft by DaBlincx
# -------------------------------------------
# 
# Have fun :)

pName = "netHax"
pDescription = "Nethacking Toolbox"
pAuthor = "DaBlincx"
pSource = "https://www.github.com/DaBlincx/nethax"
pVersion = 1.4
debugMode = False



moduleslib = []


# trying to import modules 
# adds string to moduleslib if module cannot be imported
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
    # printing needed librarys if anything fails to be imported 
    # ends script to prevent other errors
    print("Cannot import all needed librarys, \nplease make sure to have every one installed.\n\nUsage: 'pip install [module]' or 'pip3 install [module]'\n")
    print("modules:")
    for modl in moduleslib:
        print(modl)
    print()
    exit()

# trying to set con as Console() but if rich.console is not imported it will throw an error
try: con = Console()
except: importError()

if bool(moduleslib) != False:
    # if modules lib is not empty, throw error
    importError()


def initializer(lenght):
    # "initializer" for all the tools
    for x in track(range(lenght),"Initializing..."):
        time.sleep(0.1)

def mainMenu():
    for i in range(250):
        print()
    # trying to create banner using pyfiglet
    try: banner = pyfiglet.figlet_format(f"  {pName}  ",font="banner3-D")
    except: importError()
    con.print(":"*75,style="bold green")
    con.print(banner+":"*75+"\n",style="bold green")
    # printing description
    con.print(Panel(f"\n{pDescription}\n",style="bold green"))
    print()
    # select what tool you want to use
    con.print(Panel("1. Web App Hacking\n\n2. Phishing Attack\n\n3. MITM Attack\n\n4. WIFI Hacking\n\n5. Info\n\n6. Exit Program"),style="bold green")

    answer = IntPrompt.ask("Which one do you pick? ",choices=['1','2','3','4','5','6'])

    # execute selected tool
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
    initializer(25)
    # sets starting point for walk command
    ltf = "./webkey"
    ltfget = []
    # url to display filepaths 
    url = Prompt.ask("Enter the website's url: ")
    for i in track(range(100),f"Gathering information on {url}"):
        time.sleep(0.1)
    # displaying filepaths and formatting filepath for use in cracking and dumping
    for x in walk(ltf):
        dmp = str(x).split(", [",1)
        ul = f"{url}"+dmp[0][3:-1].replace(" ","")
        fl = dmp[1][3:-1].replace(" ","")
        ulflstr = f" URL: {ul}\n Files: {fl}"
        con.print(f"\n\nExploiting: \n{ulflstr}",style="green")
        ltfget.append(ulflstr)

    # "cracking" passwords
    for l in ltfget:
        con.print(f"\n\nCracking passwords: \n{l}",style="green")

    # dumping filepaths to pw_dump.txt
    f = open("pw_dump.txt","w",encoding="UTF-8")
    for l in ltfget:
        con.print(f"\n\nDumping: \n{l}",style="green")
        f.write(str(l)+"\n")
    f.close
    
    menuReq()

def phishingAttack():
    initializer(25)
    # option for fake phishing attack
    con.print(Panel("1. SMS-Phishing"),style="bold green")
    # email phishing does not exist
    con.print(Panel("2. Email Phishing"),style="bold green")
    phishMethod = IntPrompt.ask("Which one do you pick? ",choices=['1','2'])
    if phishMethod == 1:
        # max 5 phone numbers allowed
        phoneCount = IntPrompt.ask("How many phone numbers should be attacked via phishing? ",choices=['1','2','3','4','5'])
        
        phoneSms = []
        for nrnumb in range(0,phoneCount):
            # adding numkbers to spam list
            phoneSms.append(Prompt.ask(f"{nrnumb+1}. Number: "))
        for numberSms in phoneSms:
            for i in track(range(100),f"Gathering information on {numberSms} and bypassing blocked numbers."):
                # fake unblocking
                time.sleep(0.1)

        print("")
        for numberSms in phoneSms:
            for i in track(range(100),f"Sending phishing links for facebook, linkedin, twitter, youtube and instagram to {numberSms} "):
                # fake sending
                time.sleep(0.1)
        # and it asks for an email adress, why not
        emailforaccs = Prompt.ask(f"\nPlease enter you email adress to log phished account details: ")

    if phishMethod == 2:
        # error for email phishing
        featureDoesntExist()

    menuReq()

def MITM():
    initializer(25)

    # this feature does not exist
    featureDoesntExist()

    menuReq()

def getWifis():

    newplatform = platform

    # option to change current platform in debug mode 
    # if your actual platform is not supported, a wifi error will be generated
    if debugMode == True:
        print("Your current plattform is " + platform + "\nChange it? ")
        newplatform = Prompt.ask("Linux / MacOS / Windows\nlinux / darwin / win32",choices=['linux','darwin','win32'])

    # gets your current platform and throws error if its currently not supported
    if newplatform == "linux" or newplatform == "linux2":
        if debugMode:
            print("Current platform: linux")
        # error
        con.print(Panel("\nWiFi Hacking is currently not supported on linux.\nPlease try again on another version.\n"),style="bold green")
        menuReq()
    elif newplatform == "darwin":
        if debugMode:
            print("Current platform: macos")
        # runs terminal command to get available wifi networks on macos
        scan_cmd = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        scan_out, scan_err = scan_cmd.communicate()
    elif newplatform == "win32":
        if debugMode:
            print("Current platform: windows")
        # error
        con.print(Panel("\nWiFi Hacking is currently not supported on Windows.\nPlease try again on another version.\n"),style="bold green")
        menuReq()

    # prompt to create wifi error if debug mode is enabled
    if debugMode:
        create_wifierror = Prompt.ask("Create intentional WiFi error?",choices=['y','n'])
        if create_wifierror == 'y':
            scan_out, scan_err = "b''"
        if create_wifierror == 'n':
            pass

    if str(scan_err) == "b''":
        errnoo = True
        # not needed piece of code i guess?

    if str(scan_out) != "b''":
        # if there is working output, format it and add it to wifi list
        scan_out_lines = scan_out.decode("ascii")
        if debugMode:
            print(scan_out)
        scan_out_data = []
        scan_out_lines = str(scan_out).split("\\n")[1:-1]
        for each_line in scan_out_lines:
            # split every line into list entrys
            split_line = [e for e in each_line.split("  ") if e != ""]
            # remove unneeded entrys
            split_line.pop()
            split_line.pop()
            split_line.pop()
            # remove first character if it is a space
            if split_line[0].startswith(" ") == True:
                temp = split_line[0]
                temp = temp[1:]
                split_line = temp
            else:
                split_line = split_line[0]
            scan_out_data.append(split_line)

            # writing fetched networks to wifi_dump.txt
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
    initializer(25)

    # trying to get networks, if it fails, it throws wifi error
    try: 
        scdata = getWifis()
    except: 
        wifiError()
    if debugMode:
        print(scdata)
    n=0
    if scdata != None:
        cleanScreen()
        # displaying all fetched networks
        for network in scdata:
            n+=1
            ntwrk = network[:-3]
            netwrk = ntwrk.rsplit(" ",2)
            netdisplay = "SSID: " + netwrk[0] + (" "*(36-len(netwrk[0]))) + " | MAC-Address: " + netwrk[1]
            con.print(Panel(f"{n}. {netdisplay}"),style="bold green")
        
        # choose your victim
        chsc = []
        for i in range(1,n+1):
            chsc.append(str(i))
        answer = IntPrompt.ask("Select network to hack: ",choices=chsc)
        ntwrkf = scdata[answer-1][:-3]
        netwrkf = ntwrkf.rsplit(" ",2)
        netssid = netwrkf[0]
        netmac = netwrkf[1]
        cleanScreen()
        for i in track(range(100),f"Gathering information from {netssid}"):
            time.sleep(0.1)
        # select your preferred fake hacking thingy
        con.print(Panel(f"1. 4800 pwlist.txt - wordlist"),style="bold green")
        con.print(Panel(f"2. Bruteforcing method"),style="bold green")
        con.print(Panel(f"3. HTTP-Cracking"),style="bold green")
        crackmethod = IntPrompt.ask("Select cracking method: ",choices=['1','2','3'])

        print("\n")
        initializer(10)
        print("\n\n")

        S = random.randint(8,32)

        if crackmethod == 1:
            # searches pwlist in lists.py for the randomised password
            netpwd = random.choice(pwlist)
            #if debugMode:
            #    netpwd = repselfnetpwd()
            print("\n")
            tryed = 0
            
            wfend = False
            for i in track(range(0,len(pwlist)-1),"Searching..."):
                time.sleep(0.005)
                tryed += 1
                # couldn't get the progress bar with changing variables to work
                # so its just printing everything
                print(f"{tryed}/{len(pwlist)} | Trying {pwlist[i]}")
                if pwlist[i] == netpwd and netpwd != "nopasswordfound_______free":
                    wfend = True
                    break
            if wfend == True and netpwd != "nopasswordfound_______free":
                cleanScreen()
                print("Success!\n")

        

            if netpwd == "nopasswordfound_______free":
                # adds some "credibillity" if there are things that dont work
                retri = Prompt.ask("Password could not be found, retry? ",choices=['y','n'])
                if retri == "y":
                    rerunWifi()
                if retri == "n":
                    menuReq()

        if crackmethod == 2:
            # "bruteforcing" but its just generating another password
            timedr = random.randint(1,1000)
            for i in track(range(1,timedr),f"Bruteforcing..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = S))

        if crackmethod == 3:
            # "http-cracking" - not really, idk how this works lmao
            for i in track(range(100),f"Sending http requests..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = S))
                # creates random strings to make the actual pasword 
                # that gets created more random or something like that
            for i in track(range(50),f"Retrieving information..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = S))
                # final fake password gets set here
                # same justification as above

        # panel with network information and fake password
        con.print(Panel(f"\n  SSID: {netssid}\n\n  MAC-Address: {netmac}\n\n  Passphrase: {netpwd}\n"),style="bold green")
        
        menuReq()
    else:
        wifiError()

def showInfo():
    # shows information about the program, can be changed at very the very beginning of the script
    # debug mode can be enabled there
    print()
    con.print(Panel(f"\n   Information\n   -----------------------------------------------------\n   Name:          {pName}\n   Description:   {pDescription}\n   Author:        {pAuthor}\n   Source Code:   {pSource}\n   Version:       {pVersion}\n   Debug Mode:    {debugMode}\n"),style="bold green")
    menuReq()

def cleanScreen():
    for i in range(250):
        print()

def rerunWifi():
    # WiFi() cant run itself so yeah
    WiFi()

def wifiError():
    # throws error if the command to get available networks outputs nothing 
    #(wifi disabled or command not working)
    print("\nError: Code could not be executed, because WLAN is disabled.\nPlease enable Wifi connections, so this code can be execuded.")
    menuReq()
    
def repselfnetpwd():
    corr = False
    fnetpwd = Prompt.ask("Please enter a working password from the password list in lists.py")
    for pwlt in pwlist:
        if fnetpwd == pwlt:
            corr = True
        if corr == True:
            break
    if corr == False:
        fnetpwd = repselfnetpwd()
    if corr == True:
        return fnetpwd

def menuReq():
    # back to main menu or not
    print()
    mmnue = Prompt.ask("Back to main menu? ",choices=['y','n'])
    if mmnue == "y":
        mainMenu()
    if mmnue == "n":
        exitProgram()

def exitProgram():
    # explains itself
    con.print(Panel("\n  Thanks for using!\n"),style="bold green")
    exit()

def featureDoesntExist():
    # for features that dont exist currently, but will be implemented later on
    con.print(Panel(f"\nCurrently, this feature does not exist.\nPlease try again later.\n"),style="bold green")

mainMenu()