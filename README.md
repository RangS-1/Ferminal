# Ferminal


[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010+-red?logo=windows&logoColor=white)](https://github.com/RangS-1/RangSpreter)

Ferminal or I like to call it **F*ck Terminal** is a lightweight, Python-based terminal made specifically for Windows users who are tired of typing long commands in Command Prompt or PowerShell. I really hate terminal but like it. I mean,
when you use terminal, u need to write 'dir', 'mkdir', 'clear' when that is suck for me.
and yeah, i made this terminal for more efficient time, but only on windows, sorry '-_-

Instead of writing long commands repeatedly, just use short **custom aliases** that you define yourself.

Examples:
- `d` → change directory
- `w` → working directory
- `k` → make directory
- `p` → clear terminal
- etc...

## Commands

| Commands     | Description                                                            | Command Prompt|
|--------------|------------------------------------------------------------------------|---------------|
|      h       | show this help menu                                                    | nothing :V    |
|      p       | clear the screen                                                       | cls           |
|      l       | show directory                                                         | dir           |
|      i       | install something                                                      | winget        |
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
|      z       | you don't need it -_-                                                  | nothing :V    |
|      x       | Exit from terminal                                                     | exit          |

## Installer

all this command is using winget or . . . you can check the source code!

|      i       | Description                                | Command   |
|--------------|--------------------------------------------|-----------|
|     git      | install git                                | i git     |
|   composer   | install composer                           | i composer|
|      py      | install python3.1                          | i py      |
|     php      | install php                                | i php     |
|     jdk      | install jdk (Java)                         | i jdk     |
|     ojdk     | install openjdk (Java)                     | i ojdk    |
|     msql     | install MySQL (SQL)                        | i msql    |
|     psql     | install PostGreSQL (SQL)                   | i psql    |
|    xampp     | install XAMPP                              | i xampp   |

## Installation

1. Make sure you have **Python 3.8+** installed
2. Clone the repo:

```bash
git clone https://github.com/RangS-1/Ferminal.git
cd Ferminal
```
3. python3 main.py