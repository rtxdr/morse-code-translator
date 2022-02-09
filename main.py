#=PYTHON MORSE CODE TRANSLATOR=#
#
# TODO : Make file export work
# TODO : Add more options
# TODO : 
#
#
#

import platform
import os
import time

currentPlatform = platform.system()
isUnix = False
hasTextImported = False
importedTextPath = ""

#CHECKING FOR OS TYPE
if currentPlatform == "Windows":
    isUnix = False
else:
    isUnix = True   #let's hope no one uses some really shady OS with this

###############
#   CLASSES   #
###############
class basicmessages:                #BASIC MESSAGES      
    NOFILE = "File not found."
    BADFILE = "Invalid file."
    BADOPTION = "Invalid option."

class filemanips:                   #FILE MANIPULATIONS
    def importTextFile():
        print("placeholder IMP TXT FILE")
    def exportTextFile():
        print("placeholder EXP TXT FILE")

class translations:                 #TRANSLATION FUNCTIONS
    def morseToText():
        print("placeholder MTT")
    def textToMorse():
        print("placeholder TTM")

class settings:                     #SETTINGS FUNCTIONS
    def changePlatformMode():
        global isUnix
        isUnix = not isUnix

class tools:                        #TOOLS FUNCTIONS
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

########################
#   PLATFORM CHECKER   #
########################
def checkForPlatform():   
    global isUnix
    global color
    if isUnix == False:
        print("System is running Windows, colors won't load")
        class color:
            PURPLE = ''
            CYAN = ''
            DARKCYAN = ''
            BLUE = ''
            GREEN = ''
            YELLOW = ''
            RED = ''
            BOLD = ''
            UNDERLINE = ''
            END = ''
    elif isUnix == True:
        print("Unix is running, colors will load")
        class color:
            PURPLE = '\033[95m'
            CYAN = '\033[96m'
            DARKCYAN = '\033[36m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m'

#############
#   MENUS   #
#############

def settingsMenu():         #SETTINGS MENU             
    tools.clearConsole()
    if isUnix == False:
        print("1. Force Unix mode")
    elif isUnix == True:
        print("1. Force Windows mode")
    print("0. Exit")

    optionSelect = int(input("""
    >> """))

    if optionSelect == 1:
        settings.changePlatformMode()
        checkForPlatform()
        tools.clearConsole()
        splash()
        options()



def splash():               #BIG TEXT SPLASH
    print(color.PURPLE + """
██████╗░██╗░░░██╗███╗░░░███╗░█████╗░
██╔══██╗╚██╗░██╔╝████╗░████║██╔══██╗
██████╔╝░╚████╔╝░██╔████╔██║██║░░╚═╝
██╔═══╝░░░╚██╔╝░░██║╚██╔╝██║██║░░██╗
██║░░░░░░░░██║░░░██║░╚═╝░██║╚█████╔╝
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░""" + color.BLUE + """
====Python Morse Code Translator====
    """ + color.END)

def options():              #OPTIONS
    print(color.BOLD + """
    Select Option:
    """ + color.END + """
    1. Translate text to morse
    2. Translate morse to text
    """ + color.BOLD + """
    Extra stuff:
    """ + color.END + """
    3. Import .txt file""")
    if hasTextImported == False:
        print(color.RED + """    4. Export .txt file (import .txt first)""" + color.END)
    else:
        print("""
    4. Export .txt file""")
    print("""
    5. Options
    0. Exit""")

    menuSelect = int(input("""
    >> """))

    if menuSelect == 1:             #SELECTION
        translations.textToMorse()
    elif menuSelect == 2:
        translations.morseToText()
    elif menuSelect == 3:
        filemanips.importTextFile()
    elif menuSelect == 4:
        if hasTextImported == True:
            filemanips.exportTextFile()
        else:
            tools.clearConsole()
            print(color.RED + basicmessages.NOFILE)
            time.sleep(1)
            tools.clearConsole()
            exit()
    elif menuSelect == 5:
        settingsMenu()
    elif menuSelect == 0:
        tools.clearConsole()
        print("See ya!")
        time.sleep(0.5)
        tools.clearConsole()
        exit()
    else:
        print(basicmessages.BADOPTION)
        exit()

############
#   MAIN   #
############
tools.clearConsole()
checkForPlatform()
splash()
options()
