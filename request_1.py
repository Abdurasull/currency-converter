import url, requests, pprint, time
from colorama import Fore, Style, Back
from datetime import datetime
#dasturni textatish uchun function
def exitt(exit1: str|float) -> None:
    if exit1 == '1':
        print("\nBizni hizmatimizdan foydalanganingizdan mamnunmiz!!!\n")
        exit()

# menu ni yatish uchun function
def menu() -> None : 
    print(f"{Fore.YELLOW}Currency Converter {Fore.RESET}{Fore.GREEN}dasturiga xush kelibsiz! \n(Agar dasturni tugatmoqchi bo1lsandiz 0 buyrugidan foydalaning){Fore.RESET}")
    print(f"{Fore.CYAN}Mavjud valyutalar:{Fore.RESET}")

    # requests kutubxonasi yordamida url dagi ma`lumotni o`zgaruvchiga ta`minlab olamiz
    requests_sums = requests.get(url.URL)

    # url dan olgan ma`lumotimmiz string turida bo`lgani uchun uni json() function yordamida json ko`rinishi ga o`girib olamiz
    requests_list = requests_sums.json()

    result = map(lambda x: x['code'], requests_list)
    print(f"{Fore.BLUE}{list(result)}{Fore.RESET}", end="\n\n")


# natijani fayl ga qo`shuvchi function
def add_result(valyuta) ->None:
    
    hozirgi_vaqt = datetime.now()

    # vaqtni aniqlab olish
    time_result = hozirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S")
    
    with open("valyuta.txt", "a") as file:
        file.write(f"{time_result} da yaratildi: {str(valyuta)}\n\n")


# asosiy function ma`lumotlarni shu erdan izlanadi va shu erda natija e`lon qilinadi
def return_result() -> int: 
    while True:
        try:
            # konvertatsiya qilmoqchi bo`lgan summa
            summa = float(input("Summani kiriting: "))
            if summa != 0:    
                # Qaysi valyutadan konvertatsiya qilmoqchisiz
                valyuta1 = input('Qaysi valyutadan konvertatsiya qilmoqchisiz (masalan, USD):')
                exitt(valyuta1)
                if valyuta1 == '0':
                    print(f"{Fore.RED}Buncha tiz ketyabsiz??? {Fore.RESET}🥸")
                    exit()

                # Qaysi valyutaga konvertatsiya qilmoqchisiz
                valyuta2 = input('Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                exitt(valyuta2)
                if valyuta2 == '0':
                    print(f"{Fore.RED}Buncha tiz ketyabsiz??? {Fore.RESET}🥸")
                    exit()

                # requests kutubxonasi yordamida url dagi ma`lumotni o`zgaruvchiga ta`minlab olamiz
                requests_sums = requests.get(url.URL)

                # url dan olgan ma`lumotimmiz string turida bo`lgani uchun uni json() function yordamida json ko`rinishi ga o`girib olamiz
                requests_list = requests_sums.json()
                
                # valyuta tug`ri kiritilganligini tikshirish un
                count_check = 0

                # konvertatsiya qilmoqchi bo`lgan valyutalarni for loop yordamida ularni tan narxini chiqaramiz izlaymiz
                if valyuta1.upper() == 'UZS':
                    while True:
                        for valyuta in requests_list: 
                            if valyuta2.upper() == valyuta["code"]:
                                result = f"Natija: {summa} UZS = {round(summa / float(valyuta['cb_price']), 2)} {valyuta['code']}"
                                add_result(result)
                                print(f"\n{Fore.LIGHTCYAN_EX}Natija: {summa} UZS = {round(summa / float(valyuta['cb_price']), 2)} {valyuta['code']}{Fore.RESET}")
                                count_check +=1
                                break
                        # agar count_check 0 ga teng bo`lsa demak biz kiritgan valyuta xato
                        if count_check == 0:
                            print(f"\n{Fore.RED}Siz kiritgan ->{Fore.YELLOW} '{valyuta2}' {Fore.RESET}{Fore.RED}valyuta mavjud emas, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
                            valyuta2 = input(f'Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                            exitt(valyuta2)
                        else:
                            break
                else:
                    count_check = 0
                    while True:
                        for valyuta in requests_list:
                            if valyuta1.upper() == valyuta['code']:
                                while True:
                                    for val in requests_list:
                                        if valyuta2.upper() == val['code']:
                                            count_check +=1
                                            result = f"\nNatija: {summa} {valyuta['code']} = {round(float(valyuta['cb_price']) / float(val['cb_price'])*summa, 2)} {val['code']}"
                                            add_result(result)
                                            print(f"\n{Fore.LIGHTCYAN_EX}Natija: {summa} {valyuta['code']} = {round(float(valyuta['cb_price']) / float(val['cb_price'])*summa, 2)} {val['code']}{Fore.RESET}")        
                                    # agar count_check 0 ga teng bo`lsa demak biz kiritgan valyuta xato
                                    if count_check == 0:
                                        print(f"\n{Fore.RED}Siz kiritgan -> {Fore.YELLOW}'{valyuta2}'{Fore.RED} valyuta mavjud emas, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
                                        valyuta2 = input('Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                                        exitt(valyuta2)
                                    else:
                                        break  
                        # agar count_check 0 ga teng bo`lsa demak biz kiritgan valyuta xato
                        if count_check == 0:
                            print(f"\n{Fore.RED}Siz kiritgan -> {Fore.YELLOW}'{valyuta1}' {Fore.RED}valyuta mavjud emas, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
                            valyuta1 = input('Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS):')
                            exitt(valyuta1)
                        else:
                            break  
            
            else:
                print(f"{Fore.RED}Buncha tiz ketyabsiz??? {Fore.RESET}🥸")
                exit()
        except ValueError:
                        
            print(f"{Fore.RED}Iltimos, faqat butun yoki float son kiriting!{Fore.RESET}\n")
            