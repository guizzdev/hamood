import string
import random
import requests
from colorama import Fore

allstring = string.ascii_letters+str(string.digits)

def generate(times):
    validLinks = 0
    validList = []
    invalidLinks = 0
    for i in range(1, times+1):
        link = 'https://discord.gift/'
        for i in range(1, 16+1):
            link += random.choice(allstring)
        url = "https://discordapp.com/api/v9/entitlements/gift-codes/"+link+"?with_application=false&with_subscription_plan=true"
        apiurl = requests.get(url)
        if apiurl.status_code == 200:
            print(Fore.GREEN + "Valid | "+link+Fore.WHITE)
            validLinks += 1
            validList.append(link)
        else:
            print(Fore.RED + "Invalid | "+link+Fore.WHITE)
            invalidLinks += 1

    if validList != []:
        print('\nValid links:')
        for item in validList:
            print(Fore.GREEN+'  '+item)
    print(Fore.GREEN+'\nGenerating done.')
    print(Fore.GREEN+str(validLinks)+' valid links. '+Fore.RED+str(invalidLinks)+' invalid links.')

print('''
 /$$                                                         /$$
| $$                                                        | $$
| $$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$$
| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$| $$  | $$
| $$  | $$ /$$__  $$| $$ | $$ | $$| $$  | $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/|  $$$$$$/|  $$$$$$$
|__/  |__/ \_______/|__/ |__/ |__/ \______/  \______/  \_______/   
                                            by gui#5555                                                      
''')
try:
    links = int(input('How many nitro links: '))
    print(' ')
    generate(links)
except:
    print(Fore.RED+'Wrong input. Restart the program.'+Fore.WHITE)
    exit()
