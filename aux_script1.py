import json
import csv

class FileCreator:
    # Save TXT -------------------
    def save_txt(self, path, file_name):
        text_data = input('Enter your data: ')

        try:
            with open(path + '/' + file_name + '.txt', 'w', encoding='utf8') as file:
                file.write(text_data)
                print(f'File {file_name}.txt successfully created in: {path}')

        except Exception as e:
            print('Error: ', e)

    # Save JSON -------------------
    def save_json(self, path, file_name):
        user_data = input('Enter your data separated by commas: ')

        if ',' in user_data:
            data_list = user_data.split(',')
        else:
            data_list = user_data.split()

        # If odd number of elements, append None
        if len(data_list) % 2 != 0:
            data_list.append(None)  # or 'null'

        obj_json = {}

        for i in range(0, len(data_list), 2):
            key = data_list[i]
            value = data_list[i+1]
            obj_json[key] = value

        try:
            with open(path + '/' + file_name + '.json', 'w', encoding='utf8') as file:
                json.dump(obj_json, file)
                print(f'File {file_name}.json successfully created in: {path}')

        except Exception as e:
            print('Error: ', e)

    # Save CSV ---------------------
    def save_csv(self, path, file_name):
        headers = input('Enter the headers separated by commas: ')
        headers_list = headers.split(',')

        rows = []
        add_row = True

        while add_row:
            row = input('Enter row data separated by commas OR type END to finish: ')
            if row.upper() == 'END':
                add_row = False
                break
            row_list = row.split(',')
            rows.append(row_list)

        try:
            with open(path + '/' + file_name + '.csv', 'w', encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerow(headers_list)  # write headers
                writer.writerows(rows)         # write all rows
                print(f'File {file_name}.csv successfully created in {path}')

        except Exception as e:
            print('Error: ', e)
