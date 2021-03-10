from envparse import env
import os

def clear():
	os.system('clear')

USERNAMES = env.list("USERNAMES", default=[]) 
PASSWORDS = env.list("PASSWORDS", default=[]) 


