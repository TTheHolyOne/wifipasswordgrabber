import subprocess
import pyfiglet
import colorama
from colorama import init
from colorama import Fore, Back, Style

init()
 
ascii_banner = pyfiglet.figlet_format("TTheHolyOne")
ascii_banner1 = pyfiglet.figlet_format("github.com/ttheholyone", font = 'straight')
ascii_banner2 = pyfiglet.figlet_format("www.ttheholyone.com", font = 'rectangles')
print('')
print(Fore.RED + ascii_banner.lower())
print(Fore.BLUE + ascii_banner2.lower())
print(Fore.BLUE + ascii_banner1.lower())
print(Fore.RED + 'WIFI PASSWORD GRABBER')
input()

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")