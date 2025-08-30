# Project: Notes Manager TXT, CSV, JSON
from aux_script1 import *

class UserInfo:
    menu = (f'Select a number:\n'
            f'1. Create TXT\n'
            f'2. Create JSON\n'
            f'3. Create CSV\n')
    option = input(menu + 'R: ')
    file_name = input('File name: ')
    path = input('Enter file path: ')

    file_creator = FileCreator()

    if option == '1':
        file_creator.save_txt(path, file_name)

    elif option == '2':
        file_creator.save_json(path, file_name)

    elif option == '3':
        file_creator.save_csv(path, file_name)

    else:
        print('Invalid option, try again')



    else:
        print('Invalid option, try again')


