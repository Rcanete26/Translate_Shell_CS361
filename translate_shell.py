
import googletrans
from googletrans import Translator
from simple_term_menu import TerminalMenu

# Needed Packages:
# pip install googletrans==4.0.0rc1
# python3 -m pip install simple-term-menu
supported_languages = googletrans.LANGUAGES

def main():
    Running = True
    destination_language = 'en'
    
    while Running == True:
        main_options = ['Translate', 'More Info','Change Destination Language','Quit']
        main_menu = TerminalMenu(main_options)
        menu_entry = main_menu.show()
        if main_options[menu_entry] == "Quit":
            Running = False
            print("Goodbye and Thank you for using my program! :D")

        elif main_options[menu_entry] == 'Change Destination Language':
            new_language = change_language(destination_language)
            destination_language = new_language

        elif main_options[menu_entry] == 'Translate':
            translation_part(destination_language)

def change_language(current_language):
    for languages in supported_languages:
        print(f"Code:{languages}, {supported_languages[languages]}")
    print(f'The current destination language is: {current_language}')
    new_language = input('What language would you like to translate to? (Please enter language code): ')
    return str(new_language)

def translation_part(destion_lang):
            translator = Translator()
            source_text = input("What would you like the translate?: ")
            translation = translator.translate(source_text, destion_lang)
            print(translation.text)

if __name__ == '__main__':
    main()

# translator = Translator()
# source = 'すみません'

# translation = translator.translate(source)

# print(translation.text)