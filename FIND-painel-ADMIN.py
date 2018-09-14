#!/usr/bin/python3

import requests, subprocess

a = "\033[1;32m" # Verde
A = "\033[0;32m" # Verde Normal
b = "\033[1;31m" # Vermelho
bb= "\033[0;31m" # Vermelho normal
c = "\033[1;37m" # Branco
C = "\033[0;37m"

subprocess.call("clear", shell=True)
print("""
--------------------------
| Autor: Mister Cyber    |
| Canal: Legiao Anonyma  |
| Team : GHS | C.I.H     |
| Data : 06/09/2018      |
| Versa: 1.0             |
--------------------------\n""")

print("\033[00;37m")
print("\t██▓███   ▄▄▄       ██▓ ███▄    █ ▓█████  ██▓    ▄▄▄      ▓█████▄  ███▄ ▄███▓ ██▓ ███▄    █ ")
print("\t▓██░  ██▒▒████▄    ▓██▒ ██ ▀█   █ ▓█   ▀ ▓██▒   ▒████▄    ▒██▀ ██▌▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ")
print("\t▓██░ ██▓▒▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒▒███   ▒██░   ▒██  ▀█▄  ░██   █▌▓██    ▓██░▒██▒▓██  ▀█ ██▒")
print("\t▒██▄█▓▒ ▒░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██░   ░██▄▄▄▄██ ░▓█▄   ▌▒██    ▒██ ░██░▓██▒  ▐▌██▒")
print("\t▒██▒ ░  ░ ▓█   ▓██▒░██░▒██░   ▓██░░▒████▒░██████▒▓█   ▓██▒░▒████▓ ▒██▒   ░██▒░██░▒██░   ▓██░")
print("\t▒▓▒░ ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ")
print("\t░▒ ░       ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░ ▒  ░ ▒   ▒▒ ░ ░ ▒  ▒ ░  ░      ░ ▒ ░░ ░░   ░ ▒░")
print("\t░░         ░   ▒    ▒ ░   ░   ░ ░    ░     ░ ░    ░   ▒    ░ ░  ░ ░      ░    ▒ ░   ░   ░ ░ ")
print("\t               ░  ░ ░           ░    ░  ░    ░  ░     ░  ░   ░           ░    ░           ░ ")

print(bb+"\t---------------------------------------"+b+"[ BY: MISTER CYBER ]"+bb+"---------------------------------\n\n")
url = input(b+"═══━ "+a+"URL do site EX: http://site.com.br: "+c)
word = open("listadmin.txt","r")
lines = word.readlines()
print(" ")

try:
    for line in lines:
        line = line.replace("\n", " ")
        response = url+"/"+line
        host = requests.get(response)
        code = host.status_code

        if code != 301 and code != 404:
           print(a+"[+] Pagina foi encontrada "+b+"»» "+A+response)
        else:
           print(b+"[-] Pagina nao encontrada »» "+C+response)
except KeyboardInterrupt:
       print(C+"\n[!] Voce precionou Ctrl+C para cancelar!")


print(A+"\n\n====>> FIM DO PROCESSO..!")
