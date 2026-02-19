import sys
import shlex
import os
import time as t
from colorama import Fore

def app():
    print("Ferminal v.1.0")
    print("(c) RangS. All rights reserved\n")
    while True:
                
        sys.stdout.write(Fore.CYAN + "F# " + Fore.WHITE)
        command = input()

        try:
            insert = shlex.split(command)
        except Exception as e: # i thought exception is just a var -_- 
            raise e
        
        #command
        if command.strip().startswith("x"):
            print("Bye -_-\n")
            sys.exit(1)

        elif command.strip().startswith("b"):
            os.system('cls')
        
        elif command.strip().lower().startswith("e"):
            if len(insert) > 1:
                print("\n ".join(insert[1:]))
            else:
                print("What did you say?\n")

        elif command.strip().lower() == "h":
            print("""| Commands     | Description                                                            | Command Prompt|
|--------------|------------------------------------------------------------------------|---------------|
|      h       | show this help menu                                                    | nothing :V    |
|      p       | clear the screen                                                       | cls           |
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
            os.chdir(command[2:])
        
        elif command[:2] == "k ":
            os.mkdir(command[2:])

        elif command[:2] == "m ":
            os.rmdir(command[2:])
            print(f"folder has been deleted :^\n")

        elif command[:2] == "n ":
            os.system(f'del {command[2:]}')
            print(f"file has been deleted :^\n")
            
        elif command.strip().lower() == "l":
            lis = os.system('dir')
            print(lis)

        elif command[:2] == "f ":
            file = os.system(f'type nul > {command[2:]}')
            print(f"file called {command[2:]} is made")
        
        elif command[:2] == "v ":
            move = os.system(f'move {command[2:]}')
            print(f"file called {command[2:]} is moved")

        elif command[:2] == "c ":
            copy = os.system(f'copy {command[2:]}')
            print(f"file called {command[2:]} is moved")

        elif command[:2] == "u ":
            u = os.system(f'type {command[2:]}')
            print(f"\n\ninside of {command[2:]}")

        elif command == 'z': # i'm just trolling _:)
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
            else:
                print("Read Documentation!")
        else:
            os.system(command)
            print("Done using CMD _:)\n")


if __name__ == '__main__':
    app()