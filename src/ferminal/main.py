import sys
import shlex
import os
import time as t
from colorama import Fore

def main():
    print("Ferminal v1.3.3")
    print("(c) RangS. All rights reserved\n")
    while True:
                
        sys.stdout.write(Fore.CYAN + f"F# {os.getcwd()}>!\n " + Fore.WHITE)
        command = input()

        try:
            insert = shlex.split(command)
        except Exception as e: # i thought exception is just a var -_- 
            raise e
        
        #-- Basic Commands!
        if command.strip().startswith("x"):
            print("Bye -_-\n")
            sys.exit(1)
        elif command.strip().startswith("b"):
            os.system('clear')
        elif command.strip().lower().startswith("e"):
            if len(insert) > 1:
                print("\n ".join(insert[1:]))
            else:
                print("What did you say?\n")

        elif command.strip().lower() == "h":
            print("""| Commands     | Description                                                            | Command Prompt|
|--------------|------------------------------------------------------------------------|---------------|
|      h       | show this help menu                                                    | nothing :V    |
|      b       | clear the screen                                                       | cls           |
|      l       | show directory                                                         | dir           |
|      w       | show working directory or where you are                                | chdir         |
|      e       | echo (You know what i mean -_-)                                        | echo          |
|      d       | change directory                                                       | cd            |
|      k       | make a folder                                                          | mkdir         |
|      f       | make a file                                                            | type nul > "" |
|      m       | remove the folder                                                      | rmdir         |
|      n       | remove the file                                                        | del           |
|      v       | move the folder or file                                                | Move          |
|      c       | copy file                                                              | copy          |
|      u       | show content inside a file                                             | type          |
|      z       | you dont need it -_-                                                   | nothing :V    |
|      x       | Exit from terminal                                                     | exit          |\n""")
        
        elif command.strip().lower() == "w":
            wd = os.getcwd() #working directory
            print(wd,"\n")
        elif command[:2] == "d ":
            if not os.path.exists(command[2:]):
                print("Directory not found!\n")
            else:
                os.chdir(command[2:])
        elif command[:2] == "k ":
            folder = os.mkdir(command[2:])
            print(f"Folder called {command[2:]} has been made")
        elif command[:2] == "m ":
            if not os.path.exists(command[2:]):
                print("Directory not found!\n")
            else:
                os.rmdir(command[2:])
                print(f"Folder called {command[2:]} has been deleted")
        elif command[:2] == "r ":
            folder = os.system(f'rm {command[2:]}')
            print(f"File called {command[2:]} deleted!\n")
        elif command.strip().lower() == "l":
            lis = os.system('ls')
        elif command.strip().lower() == "la":
            lis = os.system('ls -a')
        elif command[:2] == "f ":
            file = os.system(f'touch {command[2:]}')
            print(f"File called {command[2:]} is made")
        elif command[:2] == "v ":
            move = os.system(f'mv {command[2:]}')
            print(f"File or Folder called {command[2:]} is moved")
        elif command[:2] == "c ":
            copy = os.system(f'cp {command[2:]}')
            print(f"File called {command[2:]} has been copied and moved")
        elif command[:3] == "cr ":
            copy = os.system(f'cp -r {command[3:]}')
            print(f"Folder called {copy} has been copied and moved")
        elif command[:2] == "u ":
            u = os.system(f'cat {command[2:]}')
            print(f"\n\ninside of {command[2:]}")

        elif command == 'z': # i'm just trolling _:), at least you can rest for 30 seconds :v
            print("You need to rest for 30 seconds :v\n")
            t.sleep(30)

        elif command[:2] == 'p ':
            p = os.system(f'ping {command[2:]}')

        #installler! you can add something, or maybe you're lazy
        elif command.startswith("i "):
            if command[2:] == 'git':
                os.system("winget install --id Git.Git -e --source winget")
            elif command[2:] == 'py':
                os.system("winget install Python.Python.3 -e")
            elif command[2:] == 'php':
                os.system("winget install PHP.PHP -e")
            elif command[2:] == 'composer':
                os.system("winget install Composer.Composer -e")
            elif command[2:] == 'jdk':
                os.system("winget install Oracle.JDK.21 -e")
            elif command[2:] == 'ojdk':
                os.system("winget install EclipseAdoptium.Temurin.17.JDK -e")
            elif command[2:] == 'msql':
                os.system("winget install Oracle.MySQL -e")
            elif command[2:] == 'psql':
                os.system("winget install PostgreSQL.PostgreSQL -e")
            elif command[2:] == 'xampp':
                os.system("winget install --id ApacheFriends.Xampp.8.2")
            elif command[2:] == 'laravel':
                os.system("laravel new")
            else:
                print("Read Documentation!")

        #-- Git
        elif command[:3] == "gia":
            git_add = os.system(f'git add {command[4:]}')
        elif command[:3] == "gis":
            git_stat = os.system(f'git status "{command[6:]}"')
        elif command[:3] == "gic":
            git_clone = os.system(f'git clone {command[3:]}')
        elif command[:3] == "gin":
            git_init = os.system('git init')
        elif command[:3] == "gib":
            git_branch = os.system(f'git branch {command[3:]}')
        elif command[:3] == "gibd":
            git_branch = os.system(f'git branch -d {command[3:]}')
        elif command[:3] == "gip":
            git_pull = os.system(f'git pull {command[3:]}')
        elif command[:3] == "gih":
            git_push = os.system(f'git push {command[3:]}')
        elif command[:3] == "gim":
            git_commit = os.system(f'git commit -m "{command[3:]}"')
        elif command[:3] == 'gil':
            log = os.system("git log")
        elif command[:3] == 'gif':
            git_fetch = os.system(f'git fetch {command[6:]}')
        elif command[:3] == 'gir':
            git_remote = os.system(f'git remote {command[6:]}')
        elif command[:3] == 'gie':
            git_merge = os.system(f'git merge {command[3:]}')
        elif command[:3] == 'gio':
            git_checkout = os.system(f'git checkout {command[6:]}')
        elif command[:3] == 'giob':
            git_checkout = os.system(f'git checkout -b {command[6:]}')
        elif command[:3] == 'gig':
            git_tag = os.system(f'git tag {command[3:]}')
        else:
            os.system(command)


if __name__ == '__main__':
    main()