from df import *
from imp import *
#imports     


while 1 < 2:
    menu(["slash🔪", "exit🛑"])
    res = input("Your option: ")
    if res ==  "1":
        print('-' * 60)
        print(Fore.RED + "NOTE change your ip every hour")
        print(Fore.RED + "reset your modem")
        print('-' * 60)
        link = input("what is the product link? ")
        vari = input("what word does the email start with? ")
        gerar(link, vari)
        break
    elif res == "2":
        exit()
    else:
        print(Fore.RED + "Invalid option")
        sleep(1)