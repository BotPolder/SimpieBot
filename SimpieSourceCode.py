#-------------------#-------------------System startup
import sys, os, ctypes, urllib.request
operatingsystem = sys.platform
version = '0.1.3'
#-------------------#-------------------Definitions
def print_lst_one_by_one(lstname: list) -> str:
    for lstelement in range(len(lstname)):
        print(printthis(lstname[lstelement]))
    return '\n'
def install_checker(appname: str) -> bool:
    exelist = exeappwalker('names')
    exelist.sort()
    if operatingsystem == 'win32':
        Exename_with_extension = appname + '.exe'
        if Exename_with_extension in exelist:
            return True
        else:
            return exelist
    elif operatingsystem == 'darwin':
        Appname_with_extension = appname + '.app'
        Appname_with_extension = appname[0].capitalize() + appname[1::] + '.app'
        print('The full name of the app:', Appname_with_extension)
        if Appname_with_extension in exelist:
            return True
        else:
            print(exelist)
            return False
def startapp(appname: str):
    import subprocess
    if operatingsystem == 'win32':
        Exename_with_extension = appname + '.exe'
        print(Exename_with_extension)
        try:
            path = get_key(Exename_with_extension)
            path_Appname = path + '\\' + Exename_with_extension
            subprocess.Popen([path_Appname, '-new-tab'])
            answer = 'path: ' + path_Appname + '\nSuccessfully started ' + Exename_with_extension + '!'
            return answer
        except FileNotFoundError:
            return "Something is missing, maybe it's my programmer's brain."
    elif operatingsystem == 'darwin':
        Appname_with_extension = appname[0].capitalize() + appname[1::] + '.app'
        try:
            path = get_key(Appname_with_extension)
            path_Appname = path + '/' + Appname_with_extension
            print(path_Appname)
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", path_Appname])
            answer = 'Successfully started' + Appname_with_extension + '!'
            return answer
        except FileExistsError:
            print("Something is missing, maybe it's my programmer's brain.")     
def get_key(val): 
    path_dict = dict(exeappwalker('both'))
    for key, value in path_dict.items(): 
        if val in value:
            return key 
    return "Seems like this Program is not installed. \nAre you sure you typed it right?"
def checkos():
    if operatingsystem == 'win32':
        winversion = sys.getwindowsversion()
        winversion = str(winversion)
        versionlst = winversion.split(',')
        answer = 'This device is running Windows, Extra info:' + versionlst[2] + versionlst[3] + versionlst[4] + '\nGood choice'
        return answer
    elif operatingsystem == 'darwin':
        import platform
        macversion = platform.mac_ver()
        return "This device is running MacOs \n Hmm you are one of those, it's okay I forgive you."
    else:
        return 'Seems like you are running something fishy'
def printthis(woord: str) -> str:
    return woord
def exeappwalker(answer: str):
    import os
    from os import walk
    exelist = []
    program_info = {}
    if operatingsystem == 'win32':
        programfiles = 'C:\Program Files (x86)'
        if answer == 'names':
            for (dirpath, dirnames, filenames) in walk(programfiles):
                for n in range(len(filenames)):
                    bestand = filenames[n]
                    if bestand[-4:] == '.exe':
                        exelist.append(bestand)
            return exelist
        elif answer == 'both':
            for (dirpath, dirnames, filenames) in walk(programfiles):
                for n in range(len(filenames)):
                    bestand = filenames[n]
                    if bestand[-4:] == '.exe':
                        if dirpath in program_info:
                            program_info[dirpath].append(bestand)
                        else:
                            program_info[dirpath] = [bestand]
            return program_info
    if operatingsystem == 'darwin':
        programfiles = '/Applications'
        if answer == 'names':
            for root, dirs, files in os.walk(programfiles):
                for element in dirs:
                    if element[-4:] == '.app':
                        exelist.append(element)
            return exelist
        elif answer == 'both':
            for root, dirs, files in os.walk(programfiles):
                for element in dirs:
                    if element[-4:] == '.app':
                        if root in program_info:
                            program_info[root].append(element)
                        else:
                            program_info[root] = [element]
            return program_info
        else:
            return 'That is not a command known for this function, try "names" or "both"'
def open(porgram_name: str):
    import subprocess
    if operatingsystem == 'win32':
        print('Trying to open', porgram_name)
        if porgram_name == 'firefox' or porgram_name == 'chrome':    
            try:
                if porgram_name == "firefox":
                    subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe', '-new-tab'])
                if porgram_name == 'chrome' or porgram_name == 'google':
                    subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe', '-new-tab'])
                    return 'Successfully started Google chrome!'
            except FileNotFoundError:
                return 'Seems like this program is not installed.'
        else:
            answer = 'Opening "' + porgram_name + '" is not supported by the command "open". \nTry again with: start ' + porgram_name
            return answer
    elif operatingsystem == 'darwin':
        import subprocess
        if porgram_name == "google" or porgram_name ==  "browser" or porgram_name == "chrome":
            try:
                subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Google chrome.app"])
                return 'Successfully started Google chrome!'
            except FileNotFoundError:
                return 'Seems like this program is not installed.'
        else:
            answer = 'Opening "' + porgram_name + '" is not supported by the command "open". \nTry again with: start ' + porgram_name
            return answer
    else:
        return 'This command is not yet available on your operating system.'
def get_system_info():
    import platform
    import socket
    import os
    Username = platform.node()
    return Username
def lookup(site: str):
    import webbrowser
    if site[0:4] == 'http':
        webbrowser.open(site)
    else:
        adress = 'https://www.google.com/search?q=' + site
        webbrowser.open(adress)
#-------------------#-------------------Main script
name = ''
lst_of_command = [
    '\n',
    'If anything is written inbetween [] in means it can be filled in by own desire (and even be kept open), keep in mind to not overtake the []!!!', 
    'Any text that is in () is just extra information.'
    '\n',
    'stop', 'help', "open [program_name] (fast method only works for some apps)", "show apps", 
    "system info", "print next (will ask for something to print)", "print [word]" , "get user", "check install [program_name]",
    "start [program_name] (slow method works for all apps)", "settings",
]
lst_of_settings_command = [
    "\n",
    'enable LOB (lauch Simpie on startup of the computer) **in development expect it to be out in ver 0.1.4' 
    ,'back (gets you back to Simpie)'
    ,'version (will give the current version of simpie)'
    , 'check update (will go to download site)'
    , 'update simpie (will download the latest installer of the app and run the installer)'
    , 'read blog (will open the devblog of this project. Here your can read all about the latest updates.)'
]
lst_of_syteminfo = []
if operatingsystem == 'win32':
    username = os.getlogin()
    answer = 'Hi ' + username + '!' 
    print(answer)
    print('Type help to see what functions you can use in this program. \n')
while True:
    if operatingsystem == 'darwin':
        if name == '':
            printthis('Hi my name is Simpie')
            name = input('What is your name? ')
            answer = 'Hi ' + name + '!'
            print(printthis(answer))
            printthis('Type help to see what functions you can use in this program.')
    command = input('Your command: ')
    commandlst = command.split(' ')
    if command == 'get user':
        print(get_system_info())
    if command == 'show os' or command == 'operating system' or command == 'system info':
        import platform, socket
        cpu = 'Processor: ' + platform.processor()
        ip4 = 'ip4: ' + socket.gethostbyname(socket.gethostname())
        lst_of_syteminfo.append(cpu)
        lst_of_syteminfo.append(ip4)
        print_lst_one_by_one(lst_of_syteminfo)
        print(checkos())
    if command == 'stop':
        break
    if command == 'show command' or command == 'show commands' or command == 'help':
        print('Okay here is a list of commands you can use:')
        print(print_lst_one_by_one(lst_of_command))
    if command[0:4] == 'open':
        filename = command.split(' ')
        try:
            print(open(filename[1]))
        except IndexError:
            print('Sorry can you try that command again, I think you missed something. Or I did at least.')
            quit
    if command == 'hi' or command == 'hello' or command == 'ni hao':
        print('Hi, how are you doing', name,'?')
        answer = input()
        if answer == 'good' or answer == 'okay' or answer == 'fine':
            print("That is good to hear!")
        elif answer == 'bad' or answer == 'shitty' or answer == 'not okay':
            print("That is to bad anything I can help you with?")
            answer = input()
            if answer == 'yes':
                print('Cool these are the commands I listen to.\n', lst_of_command)
            elif answer == 'no':
                print('Okay you want me to shut down?')
                answer = input()
                if answer == 'yes':
                    break
    if command == 'show applications' or command == 'show apps' or command == 'list apps' or command == 'list app' or command == 'list programs': 
        namesboth = input('Should I just print the names or also the directories? \nType names or both: ')
        if namesboth == 'both' or namesboth == 'names':
            print(exeappwalker(namesboth))
        else:
            print("Sorry I did't get that, just the names of both?")
            namesboth = input('names or both? ')
            if namesboth == 'both' or namesboth == 'names':
                print(exeappwalker(namesboth))
            else:
                print("Sorry I didn't get that, Do you just want the names or also the directroies?")
                namesboth = input('names or both? ')
                print(exeappwalker(namesboth))
    if command[0:5] == 'print':
        if command[6:10] == 'next':
            woord = input('Type here what I have to print: ')
            print(printthis(woord))
        else:
            printcommand = command.split(' ')
            woord = command[6::]
            print(printthis(woord))
    if command[0:5] == 'start':
        startlst = command.split(' ')
        applst = startlst[1::]
        if len(startlst) == 1:
            print('What app should I start', name,'?')
            appname = input()
            print(startapp(appname))
        else:
            seperator = ' '
            appname = seperator.join(applst)
            print(startapp(appname))
    if commandlst[0:2] == ['install', 'check'] or commandlst[0:2] == ['check', 'install']:
        seperator = ' '
        if len(commandlst) <= 2:
            print('For what app install should I look?')
            appname = input('Program name: ')
        else:
            applst = commandlst[2::]
            appname = seperator.join(applst)
        if install_checker(appname) is True:
            print('The application is installed')
        else:
            print(install_checker(appname))
            print("\nSeems like this application is not installed, \nare your sure you typed it's name right? \nYou could look for its name by pressing ctrl + f and then typing the name.")
    if commandlst[0] == "settings":
        print('Here you can customise me. To see what types of settings you can change type help. \nTo leave this settings tree just type back.')
        while command != 'back':
            if operatingsystem == 'win32':
                command = input("Change is good: ")
                if command == 'back':
                    break
                elif command == 'read blog' or command == 'devblog':
                    lookup('https://raw.githubusercontent.com/BotPolder/SimpieBot/master/Devblog.txt')
                if command == 'enable lob' or command == 'lob':
                    try:
                        from winreg import *
                        with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
                            Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
                        downloads_icon = Downloads + "/bot.ico"
                        urllib.request.urlretrieve("https://github.com/BotPolder/SimpieBot/raw/master/bot.ico", downloads_icon)
                        from pyshortcuts import make_shortcut
                        make_shortcut('C:\Program Files (x86)\\BotPolder\Simpie\BotPolder\SimpieBot.exe', name='SimpieBot', icon=downloads_icon)
                        #make_shortcut('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup', name='SimpieBot', icon=downloads_icon)
                        #C:\Program Files (x86)\BotPolder\Simpie\BotPolder
                    except:
                        print('ERROR: pyshortcuts not installer') 
                elif command == 'help':
                    print(print_lst_one_by_one(lst_of_settings_command))  
                elif command == 'version':
                    print(version)
                elif command == 'check update' or command == 'update':
                    lookup('https://github.com/BotPolder/SimpieBot/tree/master/Installer')
                elif command == 'update simpie':
                    from winreg import *
                    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
                        Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
                    downloads_installer = Downloads + "/Simpie Installer.msi"
                    import pathlib
                    installer = pathlib.Path(downloads_installer)
                    if installer.exists ():
                        print ("File exist \nDeleting old installer")
                        os.unlink(downloads_installer) 
                        print('Downloadin latest version. \nThis should not take longer than a minute.s')
                        urllib.request.urlretrieve("https://github.com/BotPolder/SimpieBot/raw/master/Installer/Simpie%20Installer.msi", downloads_installer)
                        print('Download compleet')
                    else:
                        print ("File not exist")
                        print('Beginning file download with urllib2...')
                        urllib.request.urlretrieve("https://github.com/BotPolder/SimpieBot/raw/master/Installer/Simpie%20Installer.msi", downloads_installer)
                        print('Download compleet')
                    print('Running installer')
                    try:
                        os.startfile(downloads_installer)
                        break
                    except FileNotFoundError:
                        print('Download failed')
            if operatingsystem == 'darwin':
                command = input("Change is good: ")
                if command == 'back':
                    break
                elif command == 'enable lob' or command == 'lob':
                    print('This function is not yet available for your operating system')
                elif command == 'help':
                    print(print_lst_one_by_one(lst_of_settings_command))
                elif command == 'version':
                    print(version)
                elif command == 'check update' or command == 'update':
                    lookup('https://github.com/BotPolder/SimpieBot/tree/master/Installer')
                elif command == 'update simpie':
                    import urllib.request
                    print('Beginning file download with urllib2...')
                    url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
                    downloadfile = '/Users/'+ username +'/Downloads/cat.jpg'
                    urllib.request.urlretrieve(url, '/Users/''/Downloads/cat.jpg')
                elif command == 'desktop':
                    import os
                    path = "C:/Users"
                    path = os.path.realpath(path)
                    os.startfile(path)
            # write short cut to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
            # elif command == 'install bottie' or command == 'install':
            # a shortcut will be made
    if commandlst[0] == "google" or commandlst[0] == "lookup" or commandlst[0] == "search":
        if len(commandlst) > 1:
            command = commandlst[1::]
            commandstr = ' '
            commandstr = commandstr.join(command)
            lookup(commandstr)
        else:
            command = input('What should I look for?\n')
            lookup(command)
#-------------------#-------------------Kill
print('By see you nex time.')
quit