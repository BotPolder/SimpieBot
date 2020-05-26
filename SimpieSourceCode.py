#-------------------#-------------------System startup
import sys
operatingsystem = sys.platform
#-------------------#-------------------Definitions
def install_checker(appname: str) -> bool:
    exelist = exeappwalker('names')
    exelist.sort()
    if operatingsystem == 'win32':
        Exename_with_extension = appname + '.exe'
        print('The full name of the executable:', Exename_with_extension)
        if Exename_with_extension in exelist:
            return True
        else:
            print(exelist)
            return False
    elif operatingsystem == 'darwin':
        appname_with_extension = appname + '.app'
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
            print(path_Appname)
            subprocess.Popen([path_Appname, '-new-tab'])
            return 'Successfully started', Exename_with_extension, '!'
        except FileExistsError:
            print("Something is missing, maybe it's my programmer's brain.")
    elif operatingsystem == 'darwin':
        Appname_with_extension = appname[0].capitalize() + appname[1::] + '.app'
        try:
            path = get_key(Appname_with_extension)
            path_Appname = path + '/' + Appname_with_extension
            print(path_Appname)
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", path_Appname])
            return 'Successfully started', Appname_with_extension, '!'
        except FileExistsError:
            print("Something is missing, maybe it's my programmer's brain.")     
def get_key(val): 
    path_dict = dict(exeappwalker('both'))
    print
    for key, value in path_dict.items(): 
         if val in value: 
             return key 
    return "Seems like this Program is not installed, or I'm just stupid. Probably the latter"
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
    print(woord)
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
                print('Seems like this program is not installed.')
    elif operatingsystem == 'darwin':
        import subprocess
        if porgram_name == "google" or porgram_name ==  "browser" or porgram_name == "chrome":
            try:
                subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Google chrome.app"])
                return 'Successfully started Google chrome!'
            except FileExistsError or FileNotFoundError:
                return 'Seems like this program is not installed.'
        else:
            return 'Seems like this program cannot be openen with this function.'
    else:
        return 'This command is not yet available on your operating system.'
def get_system_info():
    import platform
    import socket
    import os
    Username = platform.node()
    return Username
#-------------------#-------------------Main script
a = 0
name = ''
lst_of_command = [
    '\n',
    'If anything is written inbetween [] in means it can be filled in by own desire, keep in mind to not overtake the []!!!', 
    'Any text that is in () is just extra information.'
    '\n',
    'stop', 'help', "open [program_name] (fast method only works for some apps)", "show apps", 
    "system info", "print next (will ask for something to print)", "print [word]" , "get user", "check install [program_name]",
    "start [program_name] (slow method works for all apps)",
    '\n'
]
while a == 0:
    if name == '':
        printthis('Hi my name is Simpie')
        name = input('What is your name? ')
        answer = 'Hi ' + name + '!'
        printthis(answer)
        printthis('Type help to see what functions you can use in this program.')
    command = input('Your command: ')
    commandlst = command.split(' ')
    if command == 'get user':
        print(get_system_info())
    if command == 'show os' or command == 'operating system' or command == 'system info':
        print(checkos())
    if command == 'stop':
        break
    if command == 'show command' or command == 'show commands' or command == 'help':
        print('Okay here is a list of commands you can use:')
        for n in range(len(lst_of_command)-1):
            print(lst_of_command[n])
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
            printthis(woord)
        else:
            printcommand = command.split(' ')
            woord = command[6::]
            printthis(woord)
    if command[0:5] == 'start':
        startlst = command.split(' ')
        applst = startlst[1::]
        print(applst)
        print(len(startlst))
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
        elif install_checker(appname) is False:
            print("Seems like this application is not installed, \n are your sure you typed it's name right?")
        else:
            print(install_checker(appname))
#-------------------#-------------------Kill
print('By see you nex time.')
quit