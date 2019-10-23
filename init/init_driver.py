from appium import webdriver
import os
from subprocess import Popen, PIPE

def init_driver():
    desired_caps = {}
    # devices = os.system('adb devices')

    resp = Popen("adb devices", shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
    ip = (resp[1][0:-9]).decode('utf-8')

    Version = os.system('adb -s %s shell getprop ro.build.version.release'%ip)


    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = Version
    desired_caps['deviceName'] = ip
    desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.Settings'
    # desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver



