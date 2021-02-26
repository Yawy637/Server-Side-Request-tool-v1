import requests
import os
from colorama import Fore, Back, Style

websiteURL = input(Fore.GREEN + 'Enter website:')
print(Style.RESET_ALL)


res = requests.get(websiteURL)

print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')
print(Fore.GREEN + "---------------------")
print("Headers:")
print(Style.RESET_ALL)                                                                                                              print(res.headers)                                                

answer = input(Fore.GREEN + "Would you like the HTML? Enter yes or no: ")
print(Style.RESET_ALL)
if answer == "yes":
        print(Fore.GREEN + "---------------------")
        print("HTML code")
        print(Style.RESET_ALL)
        print(res.text)
elif answer == "no":
        sys.exit()
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "Please enter yes or no.")
    print(Style.RESET_ALL)
