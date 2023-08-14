
import googletrans
from googletrans import Translator
from simple_term_menu import TerminalMenu
import socket
import random

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 2259 # The port used by the server

RandomSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RandomSocket.connect((HOST, PORT))
print(f"connected to:  {HOST}  Port:  {PORT}")

# Needed Packages:
# pip install googletrans==4.0.0rc1
# python3 -m pip install simple-term-menu
supported_languages = googletrans.LANGUAGES
intro = 'Hello! \n This program is a script that allows you to to easily translate through your shell! The input should be auto detected and will translate to english by default. Select Change Destination Language if you would like to translate to a different langauge! \n'
warning = "Please be careful when using this project! Longer prompts of text will take longer to translate so please be patient. Please do not send anything over 15k charaters or the program might fail or cause instability. Due to some of the packages this program uses this only works on mac currently.\n"
more_info_app = "This program was made using two packages! Simple Term Menu allows this program to have a selectable menu from the command line. GoogleTras is the package that allows this program to provide the translations! This app is not associated with google.\n "
instructions = " Use the up and down arrow keys to navigate through the menu and enter to select.\n"
line_break = "----------------"

def main():
    Running = True
    destination_language = 'en'
    last_translation = "There have been no translations yet!"
    print(line_break)
    print(intro)
    print(line_break)
    print(warning)
    print(line_break)
    print(instructions)
    while Running == True:
        main_options = ['Translate', 'More Info','Show Last Translation', 'Change Destination Language','See a random translation!','Quit']
        main_menu = TerminalMenu(main_options)
        menu_entry = main_menu.show()
        if main_options[menu_entry] == "Quit":
            Running = False
            print("Goodbye and Thank you for using my program! :D")

        elif main_options[menu_entry] == 'Change Destination Language':
            new_language = change_language(destination_language)
            destination_language = new_language

        elif main_options[menu_entry] == 'Translate':
            translation_array = translation_part(destination_language)
            last_translation = translation_array[0]

        elif main_options[menu_entry] == 'Show Last Translation':
            print(last_translation)
        
        elif main_options[menu_entry] == 'More Info':
            print(line_break)
            print("More Info! \n")
            print(more_info_app)
        
        elif main_options[menu_entry] == 'See a random translation!':
            quote = get_random_quote()
            random_language = random.choice(list(supported_languages.values()))
            translator = Translator()
            quote_translation = translator.translate(quote, random_language)
            print(f"{quote} = ({random_language})-{quote_translation.text}")



def change_language(current_language):
    for languages in supported_languages:
        print(f"Code:{languages}, {supported_languages[languages]}")
    print(f'The current destination language is: {current_language}')
    new_language = input('What language would you like to translate to? (Please enter language code): ')
    return str(new_language)

def translation_part(destion_lang):
            return_array = []
            translator = Translator()
            source_text = input("What would you like the translate?: ")
            translation = translator.translate(source_text, destion_lang)
            print(translation.text)
            return_array.append(f"{source_text} = ({destion_lang})-{translation.text}")
            return_array.append(translation) 
            return (return_array)

def get_random_quote():
    quote = b'quote'
    RandomSocket.sendall(quote)
    print('message sent:', quote.decode())
    data = RandomSocket.recv(1024).decode("utf-8")
    # print(f"Received {data!r}")
    return data

if __name__ == '__main__':
    main()

# translator = Translator()
# source = 'すみません'

# translation = translator.translate(source)

