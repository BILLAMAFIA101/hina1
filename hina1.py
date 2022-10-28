#  TOOLS CREAT BY SUHAIB

import os
import sys
import marshal
import time
import requests
import platform
import base64

ua = []
cp = []
ok = []
loop = +1

#### LOGO ####

logo = """"
┏━━┓┏━━┳┓╋╋┏┓╋╋┏━━━┓
┃┏┓┃┗┫┣┫┃╋╋┃┃╋╋┃┏━┓┃
┃┗┛┗┓┃┃┃┃╋╋┃┃╋╋┃┃╋┃┃
┃┏━┓┃┃┃┃┃╋┏┫┃╋┏┫┗━┛┃
┃┗━┛┣┫┣┫┗━┛┃┗━┛┃┏━┓┃
┗━━━┻━━┻━━━┻━━━┻┛╋┗"""

#----  MAIN  ----#
def menu():
	os.system("clear")
	print(" ")
	print(" [1] BILLA YOUTUBE CHANNEL LINK ")
	print(" [0] EXIT TOOL ")
	hina = input(" CHOOSE : ")
	if hina in ["1","01"]:
		    sohaib()
	elif hina in ["0","00"]:
		    exit()

def sohaib():
	os.system("xdg-open https://youtube.com/channel/UC5U6VqYYW4-RS3mc_GYmY1A")
	
menu()
