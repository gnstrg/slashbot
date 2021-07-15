from imp import *
def linha(tam=42):
    return Fore.BLUE + '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(43))
    print(linha())

def menu(lista):
    cabecalho(Fore.BLUE + "MENU")
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())

def gerar(l, v):
    link = l
    vari = v
    #variaves
    while 1 < 2:
        chrome_options.add_argument('--headless')#opção de ficar em segundo plano
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #opção para não aparecer logs no console
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})#opção para não carregar imagens
        browser = webdriver.Chrome("chromedriver.exe", options=chrome_options,  desired_capabilities = chrome_options.to_capabilities())#instaciando o webdriver
        browser.get(l)#entrando na url
        sleep(3)#para aparecer os Botões
        try:
            am_button = browser.find_element_by_class_name("am-button")
            am = am_button.text
            if am == "Help your friend slash the price！":
                print(linha())
                pass
            else:
                print(Fore.RED + "invalid link⚠️")
                break
            am_button.click()
        except:
            print(Fore.RED + "error slash menu⚠️")
            gerar(link, vari)

        try:
            sleep(1)
            browser.find_element_by_class_name("next-tabs-tab-inner").click()
            browser.implicitly_wait(1)

        except:
            print(Fore.RED + "error⚠️")


        email = ''.join(choice(ascii_letters) for x in range(15))#gerando uma string aleatoria
        try:
            strmai = v + "." + email + "@gmail.com" #juntando as variaves
            browser.find_element_by_class_name("email").send_keys(strmai) 
        except:
            print(Fore.RED + "error generating email⚠️")
            gerar(link, vari)

        try:
            browser.find_element_by_class_name("password").send_keys("githubgenus0")#senha 
            browser.implicitly_wait(6)
            submit_button = browser.find_element_by_class_name("submit-box").click()
            browser.implicitly_wait(6)
            sleep(1)
        except:
            print(Fore.RED + "error password our submit⚠️")
            gerar(link, vari)
        
        try:
            browser.find_element_by_class_name("success-mark")
            print(Fore.GREEN + "account created successfully✅")

        except:
            print(Fore.RED + "error create account⚠️")
            gerar(link, vari)
        browser.back()
        sleep(3)
        browser.find_element_by_class_name("am-button").click()


        try:
            browser.find_element_by_class_name("deal-success-panel--Title--Q4IxJpc")
            valor = browser.find_element_by_class_name("deal-success-panel--DealPercentBoard--25t-Clo")
            res = valor.text
            print(Fore.GREEN + res + "💸")
            print(linha())
        
        except:
            print(Fore.RED + "error changer ip please⚠️")#se ta dando esse erro resete seu modem
            break

        finally:
            browser.quit()

