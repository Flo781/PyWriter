from selenium import webdriver 
import time 
from selenium.webdriver import ActionChains
from pynput.keyboard import  Controller
from os import environ, system, name
from colorama import *




def clear():
    clearer = "clear"
    if name == "cmd" or "dos":
        clearer = "cls"
    else:
        pass
    system(clearer)
clear()


###log in

user = input(Fore.LIGHTGREEN_EX +'Enter your username: '+ Style.RESET_ALL)
password = input(Fore.LIGHTGREEN_EX +'Enter your password: ' + Style.RESET_ALL)

clear()

###wie schnell er schreibt
print (Fore.LIGHTBLUE_EX + "typewriter" + Style.RESET_ALL)
zeit = float(input(Fore.LIGHTGREEN_EX +"in how many seconds should it be written: " +Style.RESET_ALL))


environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

###web driversste Zhao

drive = webdriver.Chrome('chromedriver.exe')
keyboard = Controller()
go = True


###web site

drive.get('https://at4.typewriter.at/index.php?r=typewriter/runLevel')
drive.maximize_window()

time.sleep(3)

userlog = drive.find_element_by_id('LoginForm_username')
passwordlog = drive.find_element_by_id('LoginForm_pw')

###user log in

userlog.send_keys(user)
passwordlog.send_keys(password)

log_button = drive.find_element_by_name('yt0')
log_button.click()
time.sleep(5)
runlevelB = drive.find_element_by_class_name('image')
runlevelB.click()
time.sleep(2)
##text1

while go:
    text1c = drive.find_element_by_id('actualLetter')
    text1 = text1c.text
    print(text1)
    con = ActionChains(drive)
    time.sleep(2)
    ###schreibt

    keyboard.press(text1)
    keyboard.release(text1)
    time.sleep(1)

    keyboard.press(text1)
    keyboard.release(text1)

    ##all text 

    ftextc = drive.find_element_by_id('actualLetter')
    stextc = drive.find_element_by_id('remainingText')
    ftext = ftextc.text
    stext = stextc.text
    alltext = ftext + stext


    for x in range(len(alltext)):
            for y in alltext[x]:
                keyboard.press(y)
                keyboard.release(y)
                time.sleep(zeit)

    time.sleep(2)
    print("Level complete")
    drive.back() 
    
    
    clear()
