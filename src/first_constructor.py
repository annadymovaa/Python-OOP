import sys
import os

class Research():
    def __init__(self, filepath):
        self.filepath = filepath

    def check_content(self, data):
        self.flag = False
        if len(data) > 2:
            header = data[0].split(',')
            if len(header) == 2:
                for word in header:
                    if word.replace('\n', '') == '':
                        self.flag = True
                        break
            else:
                self.flag = True

            for i in range(1, len(data)):
                line = data[i].split(',')
                if len(line) == 2:
                    for value in line:
                        value = value.replace('\n', '')
                        if value != '1' and value != '0':
                            self.flag = True
                            break
                else:
                    self.flag = True
        else:
            self.flag = True

    def file_reader(self) -> list:
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.check_content(data)
        if not self.flag:
            return(data)
        else:
            raise Exception('Incorrect data structure in the file!')

    def print_data(self, data):
        for line in data:
            print(line, end='')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filepath = sys.argv[1] #../data.csv
        obj = Research(filepath)
        data = obj.file_reader()
        obj.print_data(data)

