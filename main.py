#begin import
import time
from rich.console import Console
import os
from envparse import env
#end import and begin setup stuff

console = Console()

def clear():
	os.system('clear')
currentUser = None

USERNAMES = env.list("USERNAMES", default=[]) 
PASSWORDS = env.list("PASSWORDS", default=[]) 

#end setUp stuff

def startMenu():
	valid = False
	global USERNAMES, PASSWORDS, currentUser
	clear()
	def detectUserValid(u, p):
		nonlocal valid
		try:
			uIndex = USERNAMES.index(u)
			validPass = PASSWORDS[uIndex]
			if (p == validPass):
				currentUser = USERNAMES[uIndex]
				valid = True
				clear()
				console.print(f":white_check_mark:  [green]Access Granted. Signing into {currentUser}'s account...[/green] :white_check_mark:")
				time.sleep(3)
				clear()
		except ValueError:
			pass
	
	console.print("[bold]Welcome to  [magenta]Coder2195\'s[/magenta] wonderful [bold green]computer![/bold green][/bold] :computer:")
	time.sleep(3)
	while (not valid):
		clear()
		console.print("[italic purple bold]Please sign in to continue[/italic purple bold]")
		usernameInput  = input("Username: ")
		passwordInput = input("Password: ")
		detectUserValid(usernameInput, passwordInput)
		if (not valid):
			clear()
			console.print(":no_entry:  [red]Wrong credentials. Try again.[/red] :no_entry:")
			time.sleep(3)

startMenu()



