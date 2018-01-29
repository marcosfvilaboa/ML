
'''
#Created on 26/5/2016

@author: Marcos F. Vilaboa
'''

from src.Menu import *
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    
    menu = Menu() 
    
    while True:
        menu.drawMain()  
        select = raw_input("\n--- Insert an option number: ")
        print("\n\n")
        
        if select == '1':
            menu.fileCreationOpt()
        elif select == '2':
            menu.simpleKnnOpt()
            menu.wait()
        elif select == '3':
            menu.weightedKnnOpt()
            menu.wait()
        elif select == '4':
            menu.help()
            
        elif select == '5':
            menu.points()
            print(" THANKS to use our App!!")
            print(" See you soon")
            menu.points()
            break        
        else:
            menu.points()
            print(" Invalid option!")
            menu.points()
    
