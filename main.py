#=PYTHON MORSE CODE TRANSLATOR=#
#
# TODO : Make file export work
# TODO : Add more settings

import platform
import os
import time

currentPlatform = platform.system()
isUnix = False
hasTextImported = False
importedTextPath = ""
spaceOption = " "

#MORSE ALPHABET
morseDictionnary = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#CHECKING FOR OS TYPE
if currentPlatform == "Windows":
    isUnix = False
else:
    isUnix = True   #let's hope no one uses some really shady OS with this

###############
#   CLASSES   #
###############
class tools:                        #TOOLS FUNCTIONS
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

class basicmessages:                #BASIC MESSAGES      
    NOFILE = "File not found."
    BADFILE = "Invalid file."
    BADOPTION = "Invalid option."

class filemanips:                   #FILE MANIPULATIONS
    def importTextFile():
        tools.clearConsole()
        print("Insert file path, write X to return")
        txtFilePath = input("""
    >> """)
        if txtFilePath == "X":
            tools.clearConsole()
            splash()
            options()
        else:
            open(txtFilePath, 'r')
    def exportTextFile():
        tools.clearConsole()
        print("placeholder EXP TXT FILE")

class translations:                 #TRANSLATION FUNCTIONS
    global encryptToMorse
    global decryptMorse
    def encryptToMorse(message):
        finalMessage = ''
        for letter in message:
            if letter != ' ':
                finalMessage += morseDictionnary[letter] + ' '
            else:
                finalMessage += spaceOption
        return finalMessage
    def decryptMorse(message):
        message += ' '
        finalMessage = ''
        citext = ''
        for letter in message:
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    finalMessage += ' '
                else:
                    finalMessage += list(morseDictionnary.keys())[list(morseDictionnary.values()).index(citext)]
                    citext = '' #i legit stole this from a tutorial cause i legit don't understand anything
        return finalMessage

    def textToMorse():
        tools.clearConsole()
        print("""Insert your text
        """)  
        textInput = input(">>")
        print(encryptToMorse(textInput.upper()))

    def morseToText():
        tools.clearConsole()
        print("""Insert your morse code text (USE DOUBLE SPACES FOR SPACES)
        """)  
        morseInput = input(">>")
        print(decryptMorse(morseInput))
        
class settings:                     #SETTINGS FUNCTIONS
    def changePlatformMode():
        global isUnix
        isUnix = not isUnix
    def changeSpaceMode():
        global spaceOption
        tools.clearConsole()
        print("""Please select a spacing option:
    1. Use double spacing
    2. Use no spacing
    3. Use '/'
    
    0. Return""")

        spacemodeSelection = int(input("""
    >> """))
        if spacemodeSelection == 1:
            spaceOption = " "
            tools.clearConsole()
            settingsMenu()
        elif spacemodeSelection == 2:
            spaceOption = ""
            tools.clearConsole()
            settingsMenu()
        elif spacemodeSelection == 3:
            spaceOption = "/ "
            tools.clearConsole()
            settingsMenu()
        else:
            tools.clearConsole()
            settingsMenu()

########################
#   PLATFORM CHECKER   #
########################
def platformSetup():   
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
    print("2. Spacing options" + color.GREEN + " (Currently used : \"" + str(spaceOption) + "\")" + color.END)
    print("0. Exit")

    optionSelect = int(input("""
    >> """))

    if optionSelect == 1:
        settings.changePlatformMode()
        platformSetup()
        tools.clearConsole()
        splash()
        options()
    elif optionSelect == 2:
        settings.changeSpaceMode()
    else:
        tools.clearConsole()
        splash()
        options()

def splash():               #BIG TEXT SPLASH
    print(color.PURPLE + """██████╗░██╗░░░██╗███╗░░░███╗░█████╗░
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
platformSetup()
splash()
options()
