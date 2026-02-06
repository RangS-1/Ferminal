import sys
import shlex
import os
import time as t

def app():
    while True:
        sys.stdout.write("F$ ")
        command = input()

        try:
            insert = shlex.split(command)
        except Exception as e: # i thought exception is just a var -_- 
            raise e
        
        #command
        if command.strip().startswith("x"):
            print("Bye -_-")
            sys.exit(1)

        elif command.strip().startswith("p"):
            os.system('cls')

        elif command.strip().lower().startswith("e"):
            if len(insert) > 1:
                print("\n ".join(insert[1:]))
            else:
                print("What did you say?\n")

        elif command.strip().lower() == "h":
            print("""| Commands     | Description                                                            | Command Prompt|
|--------------|------------------------------------------------------------------------|---------------|
|      h       | Show this help menu                                                    | nothing :V    |
|      p       | Clear the screen                                                       | cls           |
|      l       | Show directory                                                         | dir           |
|      w       | Show working directory or where you are                                | chdir         |
|      e       | Echo (You know what i mean -_-)                                        | echo          |
|      d       | Change directory                                                       | cd            |
|      k       | Make a folder                                                          | mkdir         |
|      f       | Make a file                                                            | type nul > "" |
|      m       | Remove the folder or file                                              | Remove        |
|      v       | Move the folder or file                                                | Move          |
|      z       | You don't need it -_-                                                  | nothing :V    |
|      x       | Exit from terminal                                                     | exit          |""")
        
        elif command.strip().lower() == "w":
            wd = os.getcwd() #working directory
            print(wd)
        
        elif command[:2] == "d ":
            os.chdir(command[2:])
        
        elif command[:2] == "k ":
            os.mkdir(command[2:])

        elif command[:2] == "m ":
            os.rmdir(command[2:])
            print(f"folder has been deleted :^\n")
            
        elif command.strip().lower() == "l":
            lis = os.system('dir')
            print(lis)

        elif command[:2] == "f ":
            file = os.system(f'type nul > {command[2:]}')
            print(f"file called {command[2:]} is made")
        
        elif command[:2] == "v ":
            file = os.system(f'move {command[2:]}')
            print(f"file called {command[2:]} is moved")

        elif command == 'z': # i'm just trolling _:)
            t.sleep(30)

        else:
            print("Command not found bruh :V\n")


if __name__ == '__main__':
    app()