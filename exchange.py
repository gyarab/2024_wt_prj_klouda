import httpx
from colorama import Fore, init
from datetime import datetime 

today = (datetime.now()).strftime("%d.%m.%Y")
print(today)
url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date='+today
r = httpx.get(url)
init()

#print(r.text)
#print(r.status_code)

lines = r.text.split("\n")

# metoda pro získání kurzu
def get_kurz(currency):
    row=0
    if currency == "CZK":
        return 1
    curr = f"|{currency}|"
    for line in lines:
        if curr in line:
           row = line
    if row==0:
        return -1

    row_arr = row.split("|")

    kurz = row_arr[-1]
    kurz = float(kurz.replace(",","."))
    return kurz

def wrong():
    print(Fore.RED + "Špatná hodnota!" + Fore.WHITE)



for line in lines:
        row_arr = line.split("|")
        if len(row_arr)>2:
            print(Fore.BLUE + row_arr[1] +" - "+ Fore.YELLOW +row_arr[-2])
print(Fore.BLUE+ "Česká koruna - " + Fore.YELLOW + "CZK" + Fore.WHITE)


while (1):

    example="(" +Fore.YELLOW+ "EUR" +Fore.WHITE+ "/" +Fore.YELLOW+ "CZK" +Fore.WHITE+ "/" +Fore.YELLOW+"USD" +Fore.WHITE+ ")"

    curr1 = (input(f"Napište zkratku původní měny {example}")).upper()
    curr2 = (input(f"Napište zkratku výsledné měny {example}")).upper()
    kurz1 = get_kurz(curr1)
    kurz2 = get_kurz(curr2)
    if kurz1==-1 or kurz2==-1:
        wrong()
    else: break

while (1):
    value = input(f"Napiště hodnotu ({Fore.YELLOW}{curr1}{Fore.WHITE}) pro převedení:")
    
    value = value.replace(",",".")

    try:
        value = float(value)
        break
    except:
        wrong()
        value=0

exch = value*kurz1/kurz2
print(f"Vysledná hodnota: {Fore.GREEN}{value} {Fore.YELLOW}{curr1}{Fore.WHITE} = {Fore.GREEN}{exch} {Fore.YELLOW}{curr2}{Fore.WHITE}")




