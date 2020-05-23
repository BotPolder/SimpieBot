def printthis(woord: str):
    print(woord)
def give_all_applications():
    from os import walk
    f = []
    for (dirpath, dirnames, filenames) in walk('C:\Program Files\\'):
            for n in range(len(filenames)):
                bestand = filenames[n]
                if bestand[-4:] == '.exe':
                    f.append(bestand)
    return f
def give_all_applications_with_directory():
    exelist = give_all_applications()
    program_dictionary = {}
    print(exelist)
def open(porgram_name: str):
    import subprocess
    try:    
        print('attempting to open file')
        if porgram_name == "firefox":
            subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe', '-new-tab'])
        if porgram_name == 'chrome' or porgram_name == 'google':
            print('Executing chrome')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe', '-new-tab'])
    except FileNotFoundError:
        print('seems like this program is not installed.')
def get_system_info():
    import platform
    import socket
    import os
    Username = platform.node()
    print(Username)
a = 0
name = ''
lst_of_command = [
    'stop', 'show command', "open program_name", "show apps", "print"
]
while a == 0:
    if name == '':
        print('Hi my name is python bot')
        name = input('What is your name? ')
        print('Hi',name,'!')
        print('Type help to see what functions you can use in this program.')
    command = input('Your command: ')
    if command == 'stop':
        break
    if command == 'show command' or command == 'show commands' or command == 'help':
        print('Okay here is a list of commands you can use: ', lst_of_command)
    if command[0:4] == 'open':
        filename = command.split(' ')
        try:
            open(filename[1])
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
                print('Cool these are the commands I listen to.', lst_of_command)
            elif answer == 'no':
                print('Okay you want me to shut down?')
                answer = input()
                if answer == 'yes':
                    break
    if command == 'show applications' or command == 'show apps' or command == 'list apps' or command == 'list app' or command == 'list programs': 
        exelist = give_all_applications()
        print(exelist)
    if command == 'print this' or command == 'print':
        woord = input('Type here what I have to print: ')
        printthis(woord)
    else:
        print("Sorry I didn't get that")
        print('Type help to see what functions you can use in this program.')
print('By see you nex time.')
quit