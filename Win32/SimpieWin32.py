#-------------------#-------------------System startup
import sys
operatingsystem = sys.platform  
import os, ctypes, urllib.request, time, requests
from winreg import *
from bs4 import BeautifulSoup
version = '0.1.7'
version_lst = version.split('.')
skip_initial_command = False
#-------------------#-------------------Definitions
#def gettime(zone: str, setting: str):
#    import datetime
#    current_time = datetime.datetime.now()
#    current_time.setting
#    return current_time
def update_check() -> str: ## The updated_check() will only work if subversion (z) in (x.y.z) is not higher than 15. ##and will only work for alpha (0.x.y)   
    url = 'https://github.com/BotPolder/SimpieBot/tree/master/Installer'
    try:
        response = requests.get(url)
        check = str(response)
        if check == '<Response [200]>':
            soup = BeautifulSoup(response.text, "html.parser")
            set_of_span = set(soup.findAll("span", {"class": "css-truncate css-truncate-target"}))
            str_of_span = str(set_of_span)
            devblog_words = str_of_span.split()
            ver_github = '0.0.0'
            ver = '0.1.'
            ver_lst = []
            for n in range(15):
                ver_str = ver + str(n)
                if ver_str in devblog_words:
                    ver_github = ver_str
                    ver_lst = ver_str.split('.')
                    if ver_str == version:
                        return 'latest'
                    #if n == 14:
                        #print('last')
            ver_github_lst = ver_github.split('.')
            if int(ver_github_lst[1]) >= int(version_lst[1]):
                if int(ver_github_lst[2]) >= int(version_lst[2]):
                    return ver_github
                else:
                    return 'newer_version'
            else:
                return 'newer_version'
    except:
        return 'internet_error'
def update_simpie():
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    downloads_installer = Downloads + "/Simpie Installer.msi"
    import pathlib
    installer = pathlib.Path(downloads_installer)
    if installer.exists ():
        print ("\nFile exist \nDeleting old installer")
        os.unlink(downloads_installer) 
        print('Downloading latest version. \nThis should not take longer than a minute. -> ', end='')
        urllib.request.urlretrieve("https://github.com/BotPolder/SimpieBot/raw/master/Installer/Simpie%20Installer.msi", downloads_installer)
        print('Download compleet -> ', end='')
    else:
        print ("File not exist")
        print('Beginning file download from Github repo')
        urllib.request.urlretrieve("https://github.com/BotPolder/SimpieBot/raw/master/Installer/Simpie%20Installer.msi", downloads_installer)
        print('Download compleet')
    print('Running installer')
    try:
        return os.startfile(downloads_installer)
    except FileNotFoundError:
        return 'Download failed'
def print_lst_one_by_one(lstname: list, way: str) -> str:
    if way == 'with_enters':
        for lstelement in range(len(lstname)):
            print(lstname[lstelement])
    if way == 'with_tabs':
        for lstelement in range(len(lstname)):
            try:
                if len(lstname[lstelement]) < 15 and len(lstname[lstelement + 1]) < 15 and len(lstname[lstelement + 2]) < 15 and len(lstname[lstelement + 3]) < 15:
                    print(lstname[lstelement], '\t\t', lstname[lstelement + 1], '\t\t', lstname[lstelement + 2], '\t\t', lstname[lstelement + 3])
                else:
                    print(lstname[lstelement], '\t\t\t', lstname[lstelement + 1], '\t\t\t', lstname[lstelement + 2], '\t\t\t', lstname[lstelement + 3])
            except IndexError:
                break
    if way == 'no_style':
        for lstelement in range(len(lstname)):
            print(lstname[lstelement])
    return '\n'
def install_checker(appname: str) -> bool:
    exelist = exeappwalker('names')
    exelist.sort()
    Exename_with_extension = appname + '.exe'
    print(Exename_with_extension)
    if Exename_with_extension in exelist:
        return True
    else:
        return exelist
def startapp(appname: str):
    import subprocess
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
def get_key(val): 
    path_dict = dict(exeappwalker('both'))
    for key, value in path_dict.items(): 
        if val in value:
            return key 
    return "Seems like this Program is not installed. \nAre you sure you typed it right?"
def checkos():
    winversion = sys.getwindowsversion()
    winversion = str(winversion)
    versionlst = winversion.split(',')
    answer = 'This device is running Windows, Extra info:' + versionlst[2] + versionlst[3] + versionlst[4] + '\nGood choice'
    return answer
def printthis(woord: str) -> str:
    return woord
def exeappwalker(answer: str):
    import os
    from os import walk
    exelist = []
    program_info = {}
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
def open(porgram_name: str):
    import subprocess
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
raw_lst_of_command = [
    'get user', 'show os', 'operating system', 'system info', 'stop', 'quit', 'show command', 'show commands',
    'help', 'open chrome', 'open firefox', 'open google', 'hi', 'hello', 'ni hao', 'show applications', 'show apps', 'list apps', 'list app',
    'list programs', 'print', 'start', "google", "lookup", "search", "settings", 'check', 'install', 'back', 'devblog', 'check install', 'install check',
    'clear', 'read board', 'trello', 'discord'
]
lst_of_command = [
    ''' \nIf anything is written inbetween [] it means it can be filled in by own desire (and even be kept open), 
    keep in mind to not overtake the []!!!
    Any text that is in () is just extra information.
    ''',
    'Okay here is a list of commands you can use:\n'
    , '\n[[ USEFULL ]]'
    , "time (will display current time)"
    , 'lookup [word or direct link] (will look words or links up on the internet)'
    , "open [program_name] (fast method only works for some apps)"
    , "start [program_name] (slow method works for all apps)"
    , "show apps (gives you a list of all the applications installed on your device)"
    , "check install [program_name]"
    , '\n[[ FUN ]]'
    , "print next (will ask for something to print)"
    , "print [word]"
    , '\n[[ TECHNICAL ]]'
    , "system info (will tell you something more about your pc."
    , "get user (will give you the current username and name of the device)"
    , '\n[[ READ ABOUT THIS PROJECT ]]'
    , 'devblog (will print out the devblog)'
    , 'read board (or) trello (will bring you to the trello board where you can read more about upcomming features and bug fixes)'
    , 'discord (will take you to the discord "plaza" server where you can join the simpie community :)) )'
    , '\n[[ IMPORTANT ]]'
    , "settings (customise me)", 'stop (or) quit (will shut me down)', 'help', 'clear (will clean up your screen)'
]
lst_of_settings_command = [
    "\n",
    'enable LOB (lauch Simpie on startup of the computer) **in development expect it to be out in ver 0.1.5' 
    ,'back (gets you back to Simpie)'
    ,'version (will give the current version of simpie, and compare it to the current installation.)'
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
    info = update_check() 
    if info[0:2] == '0.':
        print('There is a new version available would you like to update? \nCurrent version: ', version, '\nNewer version: ', info)
        answer = input('yes / no: ')
        if answer == 'yes':
            update_simpie()
        else:
            print('Okay current version remains.')
    #elif info == 'newer_version':
    #    print('Hi developer :)')
    elif info == 'internet_error':
        print('Seems like you are not connected to the internet. \nWant to check for an update?')
        answer = input('yes / no: ')
        if answer == 'yes':
            lookup('https://github.com/BotPolder/SimpieBot/tree/master/Installer')
    elif info != 'latest' and info[0:2] != '0.' and info != 'newer_version' and info != 'network_error':
        print(info)
while True:
    if skip_initial_command is False:
        command = input('Your command: ')
    skip_initial_command = False
    commandlst = command.split(' ')
    commandlst.append('command')
#    if (command == 'time') and commandlst[-1] == 'command':
#        print(gettime('CET', 'hour'))
    if command == 'get user': #and commandlst[-1] == command:
        print('The system name:',get_system_info(), '\nThe username:', username)
    if (command == 'show os' or command == 'operating system' or command == 'system info') and commandlst[-1] == 'command':
        import platform, socket
        lst_of_syteminfo = []
        cpu = '\nProcessor: ' + platform.processor()
        ip4 = 'ip4: ' + socket.gethostbyname(socket.gethostname())
        lst_of_syteminfo.append(cpu)
        lst_of_syteminfo.append(ip4)
        print_lst_one_by_one(lst_of_syteminfo, 'no_style')
        print(checkos())
    if (command == 'stop' or command == 'quit') and commandlst[-1] == 'command':
        break
    if (command == 'show command' or command == 'show commands' or command == 'help') and commandlst[-1] == 'command':
        print(print_lst_one_by_one(lst_of_command, 'no_style'))
    if commandlst[0] == 'open'and commandlst[-1] == 'command':
        filename = command.split(' ')
        try:
            print(open(filename[1]))
        except IndexError:
            print('Sorry can you try that command again, I think you missed something. Or I did at least.')
            quit
    if (command == 'hi' or command == 'hello' or command == 'ni hao') and commandlst[-1] == 'command':
        print('Hi, how are you doing', name,'?')
        answer = input()
        if answer == 'good' or answer == 'okay' or answer == 'fine':
            print("That is good to hear!")
        elif answer == 'bad' or answer == 'shitty' or answer == 'not okay':
            print("That is to bad anything I can help you with?")
            answer = input()
            if answer == 'yes':
                print('Cool these are the commands I listen to.\n', print_lst_one_by_one(lst_of_command, 'no_style'))
            elif answer == 'no':
                print('Okay you want me to shut down?')
                answer = input()
                if answer == 'yes':
                    break
    if (command == 'show applications' or command == 'show apps' or command == 'list apps' or command == 'list app' or command == 'list programs')and commandlst[-1] == 'command': 
        namesboth = input('Should I just print the names or also the directories? \nType names or both: ')
        if namesboth == 'both' or namesboth == 'names':
            exelst_dict = exeappwalker(namesboth)
            if type(exelst_dict):
                print_lst_one_by_one(exelst_dict, 'with_tabs')
            else:
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
    if commandlst[0] == 'print'and commandlst[-1] == 'command':
        if command[6:10] == 'next':
            woord = input('Type here what I have to print: ')
            print(woord)
        else:
            printcommand = command.split(' ')
            woord = command[6::]
            print(woord)
    if commandlst[0] == 'start'and commandlst[-1] == 'command':
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
    if commandlst[0:2] == ['install', 'check'] or commandlst[0:2] == ['check', 'install'] and commandlst[-1] == 'command':
        seperator = ' '
        if len(commandlst) <= 3: ## because of this dumb command check i have to use 3 instead of 2.
            print('For what app install should I look?')
            appname = input('Program name: ')
        else:
            applst = commandlst[2::]
            appname = seperator.join(applst)
            appname = appname[0:-8] ## and here i have to delete the dumb thing so that it skips the last 8 dumb string kars. Damnit
        if install_checker(appname) is True:
            print('The application is installed')
        else:
            print(install_checker(appname))
            print("\nSeems like this application is not installed, \nare your sure you typed it's name right? \nYou could look for its name by pressing ctrl + f and then typing the name.")
    if commandlst[0] == "settings"and commandlst[-1] == 'command':
        print('\nHere you can customise me. To see what types of settings you can change type help. \nTo leave this settings tree just type back.')
        while command != 'back':
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
                    #from pyshortcuts import make_shortcut
                    #make_shortcut('C:\Program Files (x86)\\BotPolder\Simpie\BotPolder\SimpieBot.exe', name='SimpieBot', icon=downloads_icon)
                    #make_shortcut('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup', name='SimpieBot', icon=downloads_icon)
                    #C:\Program Files (x86)\BotPolder\Simpie\BotPolder
                except:
                    print('ERROR: pyshortcuts not installer') 
            elif command == 'help':
                print(print_lst_one_by_one(lst_of_settings_command, 'no_style'))  
            elif command == 'version':
                info = update_check() 
                if info[0:2] == '0.':
                    print('\nThere is a new version available would you like to update? \nCurrent version', version, '\nNewer version: ', info)
                    answer = input('yes / no: ')
                    if answer == 'yes':
                        update_simpie()
                    else:
                        print('Okay current version remains.')
                elif info == 'latest':
                    print('Latest version (', version, ') installed')
                elif info == 'not_supported':
                    print('This function is not yet supported by your Operating System')
                elif info == 'newer_version':
                    print('Hi developer :) \nYou are on:\tStaging Branch: ', version)
                elif info == 'internet_error':
                    print('Seems like you are not connected to the internet. Want to check or leave it for now?')
                    answer = input('Want to check if the downloadsite is online: ')
                    if answer == 'yes':
                        lookup('https://github.com/BotPolder/SimpieBot/tree/master/Installer')
                else:
                    print(info)
                    print("Could not check for new version of me online. \nAre you sure you have internet?")
                    answer = input('Want to check if te site is online: ')
                    if answer == 'yes':
                        lookup('https://github.com/BotPolder/SimpieBot/tree/master/Installer')
            elif command == 'check update' or command == 'update':
                lookup('https://github.com/BotPolder/SimpieBot/tree/master/Installer')
            elif command == 'update simpie':
                update_simpie()
    if (commandlst[0] == "google" or commandlst[0] == "lookup" or commandlst[0] == "search") and commandlst[-1] == 'command':
        if len(commandlst) > 2:
            command = commandlst[1:-1]
            seperator = ' '
            commandstr = seperator.join(command)
            lookup(commandstr)
        else:
            command = input('What should I look for?\n')
            lookup(command)
    if commandlst[0] == "devblog" and commandlst[-1] == 'command':
        url = 'https://raw.githubusercontent.com/BotPolder/SimpieBot/master/Devblog.txt'
        try:
            response = requests.get(url)
            check = str(response)
            if check == '<Response [200]>':
                skip = False
                devblog = str(BeautifulSoup(response.text, "html.parser"))
                devblog_list = devblog.split('\n')
                first_devblog_element = str(devblog_list[0])
                print('About what version would you like to read the devblog?')
                print('Available devblog versions: 0.0.1 ->', version)
                answer = input('current / other / all: ')
                if answer == 'all':
                    for n in range(len(devblog_list)):
                        print(devblog_list[n])
                        skip = True
                if answer == 'current' and skip is False:
                    devblog_list = devblog.split('Devblog: ver ')
                    for current_github_version in devblog_list:
                        if version == current_github_version[0:5]:
                            print('\n', current_github_version)
                    skip = True
                if answer != 'other' and answer != 'current' and answer != 'all' and skip is False:
                    print("Sorry I didn't get that \n")
                    skip_initial_command = True
                    skip = True
                if answer == 'other' and skip is False:
                    print('type the numbers of the version one by one:')
                    dev_version = ''
                    while len(dev_version.split('.')) < 3:
                        for n in range(3):
                            answer = input(dev_version)
                            try:
                                answer = str(int(answer))
                                if n < 2:
                                    dev_version += str(answer) + '.'
                                else:
                                    dev_version += str(answer)
                                    answer = 'other'
                            except ValueError:
                                if answer == 'back':
                                    dev_version = dev_version.split('.')
                                    dev_version.pop(-1)
                                    seperator = '.'
                                    dev_version = str(seperator.join(dev_version))
                                else:
                                    print('You can only put in one number.')
                try:
                    if skip is False:
                        devblog_list = devblog.split('Devblog: ver ')
                        for current_github_version in devblog_list:
                            if dev_version == current_github_version[0:5]:
                                print('\n', current_github_version)
                except:
                    print("sorry I didn't get that")
                    skip_initial_command = True
        except:
            print('internet_error')
    if command == 'clear':
        import os
        try:    
            os.system("cls")
        except:
            print('Seems like this command does not work on you system.')
    if command == 'read board' or command == 'trello':
        lookup("https://trello.com/b/AFvBSXwj/simpiebot")
    if commandlst[0] == 'discord':
        print('Have fun and be polite :)')
        lookup('https://discord.gg/pxKBbKM')
    if commandlst[-1] == 'command' and command not in raw_lst_of_command and commandlst[0:2] != ['check', 'install'] and commandlst[0:2] != ['print', 'next'] and commandlst[0] != 'print' and commandlst[0] != 'lookup' and commandlst[0] != 'open' and commandlst[0] != 'start':
        for gues_command in raw_lst_of_command:
            current_command_check = []
            count = 0
            for kar in gues_command :
                current_command_check.append(kar)
            for kar in command:
                if kar in current_command_check:
                    count += 1
            count = float(count)
            if count >= 0.75 * len(command):
                print('Did you mean to type:', gues_command, '?')
                answer = input('yes, no, stop: ')
                if answer == 'yes':
                    command = gues_command
                    skip_initial_command = True
                    break
                if answer == 'stop' or answer == 'quit':
                    break
        if answer != 'stop' and  answer != 'yes' and  answer != 'quit':
            print("Sorry I didn't get that, try typing the command again. \nOr use the command help for more info.")

#-------------------#-------------------Kill
print('Bye see you next time.')
quit