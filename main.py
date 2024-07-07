from requests import get
from colorama import Fore , init
from urllib.parse import urlparse
from os import system , name , kill , getpid
from fake_useragent import UserAgent
from time import sleep as slp
from pystyle import Colorate , Colors
from datetime import datetime
from socket import socket , gethostbyname , AF_INET , SOCK_DGRAM , SOCK_STREAM
import time

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = """
Y88b         / ,e,         888   _    e88~-_  888                        888   _                    
 Y88b       /   "   e88~~\ 888 e~ ~  d888   \ 888-~88e  e88~~8e   e88~~\ 888 e~ ~   e88~~8e  888-~\ 
  Y88b  e  /   888 d888    888d8b    8888     888  888 d888  88b d888    888d8b    d888  88b 888    
   Y88bd8b/    888 8888    888Y88b   8888     888  888 8888__888 8888    888Y88b   8888__888 888    
    Y88Y8Y     888 Y888    888 Y88b  Y888   / 888  888 Y888    , Y888    888 Y88b  Y888    , 888    
     Y  Y      888  "88__/ 888  Y88b  "88_-~  888  888  "88___/   "88__/ 888  Y88b  "88___/  888    
                                                                                                    

		           [ Created By John Wick - Pytho Learn Team ] V-1.0


           [1] HTTP CHECKER     --->   CHECKING WEBSITE RESPONSE AND GET IP .
           [2] TCP CHECKER      --->   CHECKING IP & PORT ( TCP ) AND RESPONSE .
           [3] UDP CHECKER      --->   CHECKING IP & PORT ( UDP ) AND RESPONSE .
           [4] ISP CHECKER      --->   CHECKING FIREWALLS ( WAF ) WITH IP & PORT OR URL .
           [5] CLEAR            --->   CLEAR THE PAGE .
           [6] EXIT             --->   EXIT THE PROGLAM .
"""

print(Colorate.Horizontal(Colors.blue_to_cyan,banner,1))

while True:
    try:
        method = input(f"\n{green}[{white}>_{green}] {red}Select Options Number {yellow}>>>{blue} ")
    except:
        pass

    uaa = UserAgent()
    ua = uaa.random

    headers = {
        'User-Agent':ua,
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }

    def http(url):
        for _ in range(85):
            res = get(url , headers=headers)
            ip = gethostbyname(target)
            print(f'{red}[{yellow}+{red}] {green}URL {red}: {cyan}{url} {red}| {yellow}RESPONSE {red}: {green}{res.status_code} {red}| {blue}IP {red}: {yellow}{ip} {magenta}-{red}-{cyan}>')

    def tcpp(target_ip , target_port , interval = 0.5): 
        for _ in range(85):
            try:
                start_time = time.time()
                client_socket = socket(AF_INET , SOCK_STREAM)
                client_socket.settimeout(5)
                client_socket.connect((target_ip , target_port))
                client_socket.close()
                end_time = time.time()
                response_time = (end_time - start_time) * 1000
                print(f"{white}Connected to {green}{target_ip}{white}: time={green}{response_time:.2f}ms{white} protocol={green}TCP{white} port={green}{target_port}")
            except socket.error:
                print("\033[91mConnection timed out")

            slp(interval)

    def udpp(target_ip , target_port , interval = 0.5): 
        for _ in range(85):
            try:
                start_time = time.time()
                client_socket = socket(AF_INET , SOCK_DGRAM)
                client_socket.settimeout(5)
                client_socket.connect((target_ip , target_port))
                client_socket.close()
                end_time = time.time()
                response_time = (end_time - start_time) * 1000
                print(f"{white}Connected to {green}{target_ip}{white}: time={green}{response_time:.2f}ms{white} protocol={green}TCP{white} port={green}{target_port}")
            except Exception as e:
                print("\033[91mConnection timed out")

            slp(interval)
    
    def ispp(target):
        try:
            now = datetime.now()
            current_datetime = datetime.now()
            date = current_datetime.date()
            timee = now.strftime('%H:%M:%S')

            response = get(f"http://ip-api.com/json/{target}")
            response.raise_for_status()
            data = response.json()

            isp = data['as']
            city = data['city']
            zone = data['timezone']

            bann = f"""

{green}Y88b         / ,e,         888   _    e88~-_  888                        888   _                    
 Y88b       /   "   e88~~\ 888 e~ ~  d888   \ 888-~88e  e88~~8e   e88~~\ 888 e~ ~   e88~~8e  888-~\ 
  Y88b  e  /   888 d888    888d8b    8888     888  888 d888  88b d888    888d8b    d888  88b 888    
   Y88bd8b/    888 8888    888Y88b   8888     888  888 8888__888 8888    888Y88b   8888__888 888    
    Y88Y8Y     888 Y888    888 Y88b  Y888   / 888  888 Y888    , Y888    888 Y88b  Y888    , 888    
     Y  Y      888  "88__/ 888  Y88b  "88_-~  888  888  "88___/   "88__/ 888  Y88b  "88___/  888    
                                                                                                    

		           {red}[ {cyan}Created By John Wick {red}- {green}Pytho Learn Team {red}] {blue}V{red}-{green}1{cyan}.{magenta}0

            {cyan}╔══════════════════════════════════════════════════════════════════╗
            {yellow} Date   {red}: {yellow}[ {green}{date}{yellow} ]
            {yellow} Time   {red}: {yellow}[ {green}{timee}{yellow} ]
            {yellow} Isp    {red}: {yellow}[ {green}{isp}{yellow} ]
            {yellow} Zone   {red}: {yellow}[ {green}{zone}{yellow} ]
            {yellow} City   {red}: {yellow}[ {green}{city}{yellow} ]
            {yellow} Tool   {red}: {yellow}[ {red}Wick{green}-{cyan}Checker{yellow} ]
            {cyan}╚══════════════════════════════════════════════════════════════════╝"""
            system('cls' if name == 'nt' else 'clear')
            print(bann)
        except:
            pass

    try:
        if method == '1':
            url = input(f'\n{green}[{white}>_{green}] {yellow}Enter Your URL ADDRES {red}:{cyan} ')
            parsed_url = urlparse(url)
            target = parsed_url.netloc
            http(url)
        elif method == '2':
            target_ip = str(input(f'\n{green}[{white}>_{green}] {yellow}Enter Your IP ADDRES {red}:{cyan} '))
            target_port = int(input(f'{green}[{white}>_{green}] {yellow}Enter Your PORT NUMBER {red}:{cyan} '))
            interval = 0.5
            tcpp(target_ip , target_port , interval)
        elif method == '3':
            target_ip = str(input(f'\n{green}[{white}>_{green}] {yellow}Enter Your IP ADDRES {red}:{cyan} '))
            target_port = int(input(f'{green}[{white}>_{green}] {yellow}Enter Your PORT NUMBER {red}:{cyan} '))
            interval = 0.5
            udpp(target_ip , target_port , interval)
        elif method == '4':
            url = input(f'\n{green}[{white}>_{green}] {yellow}Enter Your URL ADDRES {red}:{cyan} ')
            parsed_url = urlparse(url)
            target = parsed_url.netloc
            ispp(target)
        elif method == '5':
            system('cls' if name == 'nt' else 'clear')
            print(Colorate.Horizontal(Colors.blue_to_cyan,banner,1))
        elif method == '6':
            kill(getpid() , 9)
    except:
        pass
