from envparse import env
import os

def clear():
	os.system('clear')

white_list = env.list("PASSWORDS", default=[]) 
print(white_list)

