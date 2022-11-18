import colorama
colorama.init()
'''''
help()
'''''
# Імпортує команди.
from colorama import init, Fore, Back,  Style

init()

#Дає синій колір для тексту. За це відповідає  Fore.
print(Fore.BLUE + "Blue")

'''''
#Дає білий фон для тексту. За це відповідає Back.
print(Back.WHITE + "White Background")
'''''

#Style відповідає за надання тексту стилю .
print(Style.BRIGHT + 'Style')
print(Style.DIM + 'Style')
print(Style.NORMAL + 'Style')



