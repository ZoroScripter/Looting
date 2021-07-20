import os
import time

#Cores
#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro

os.system("clear")
os.system("pkg install figlet")
os.system("clear")
print("\033[1;36m \033[1;35m")
os.system("figlet Looting.Exe")
print("""\033[1;36m
l=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l
l                       Looting                                 l
l=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l
l                //=======================\\                     l
l               l  [1]Install Update      l                     l
l               l  [2]Install Upgrade     l                     l
l               l  [3]Install Git         l                     l
l               l  [4]Install Python      l                     l
l               l  [5]Install Python2     l                     l
l               l  [6]Install Python3     l                     l
l               l  [7]Install Figlet      l                     l
l               l  [8]Install curl        l                     l
l               l  [9]Install Perl        l                     l
l               l  [10]Install pip        l                     l
l               l  [11]Install Wget       l                     l
l               l  [12]Install nano       l                     l
l               l  [13]Install php        l                     l
l               l  [14]Install clang      l                     l
l               l  [15]Install F1GH       l                     l
l               l  [16]Install Of-Sploit  l                     l
l               l  [17]Install Open-File  l                     l
l               l  [18]Install Cmatrix    l                     l
l               l  [19]Install SL         l                     l
l               l  [20]Install Labaca     l                     l
l               l  [21]Install Kiny       l                     l
l               l  [22]Sair               l                     l
l                \\=======================//                     l
l=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l
""")
op = input("Digite a Opção: ")

if op == "1":
    os.system("""
    clear
    apt-get update
    python3 looting.py
    """)
elif op == "2":
    os.system("""
    clear
    apt-get upgrade
    python3 looting.py
    """)
elif op == "3":
    os.system("""
    clear
    pkg install git
    python3 looting.py
    """)
elif op == "4":
    os.system("""
    clear
    pkg install python
    python3 looting.py
    """)
elif op == "5":
    os.system("""
    clear
    pkg install python2
    python3 looting.py
    """)
elif op == "6":
    os.system("""
    clear
    pkg install python3
    python3 looting.py
    """)
elif op == "7":
    os.system("""
    clear
    pkg install Figlet
    python3 looting.py
    """)
elif op == "8":
    os.system("""
    clear
    pkg install curl
    python3 looting.py
    """)
elif op == "9":
    os.system("""
    clear
    pkg install perl
    python3 looting.py
    """)
elif op == "10":
    os.system("""
    clear
    pip install requests
    python3 looting.py
    """)
elif op == "11":
    os.system("""
    clear
    pkg install wget
    python3 looting.py
    """)
elif op == "12":
    os.system("""
    clear
    pkg install nano
    python3 looting.py
    """)
elif op == "13":
    os.system("""
    clear
    pkg install php
    python3 looting.py
    """)
elif op == "14":
    os.system("""
    clear
    pkg install clang
    python3 looting.py
    """)
elif op == "15":
    os.system("""
    clear
    git clone https://github.com/ZoroScripter/F1GH.git
    python3 looting.py
    """)
elif op == "16":
    os.system("""
    clear
    git clone https://github.com/ZoroScripter/Of-Sploit.git
    python3 looting.py
    """)
elif op == "17":
    os.system("""
    clear
    git clone https://github.com/ZoroScripter/Open-File.git
    python3 looting.py
    """)
elif op == "18":
    os.system("""
    clear
    pkg install cmatrix
    python3 looting.py
    """)
elif op == "19":
    os.system("""
    clear
    pkg install sl
    python3 looting.py
    """)
elif op == "20":
    os.system("""
    clear
    pkg install libaca
    python3 looting.py
    """)
elif op == "21":
    os.system("""
    clear
    git clone https://github.com/Kiny-Kiny/Kiny-Painel
    python3 looting.py
    """)
elif op == "22":
    os.system("clear")
    print("Até A proxima Versão")
    time.sleep(6)
    os.system("""
    clear
    figlet Saindo!...
    """)
    print("A Justiça é cega, e nos somos os olhos! ZoroScripter")
    exit()
else:
    os.system("python3 looting.py")
