from df import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import colorama
from colorama import Fore
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
colorama.init(convert=True, autoreset=True)#config pra auto reseta 
from string import ascii_letters
from random import choice
#imports

mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#user-agent