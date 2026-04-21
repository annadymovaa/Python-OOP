from random import randint
import config

class Research():
    def __init__(self, filepath, has_header=True):
        self.filepath = filepath
        self.has_header = has_header

    class Calculations():
        def __init__(self, data):
            self.data = data

        def counts(self):
            self.heads = 0
            self.tails = 0
            for pair in self.data:
                if pair[0] == 1:
                    self.heads += 1
                else:
                    self.tails += 1


        def fractions(self):
            self.counts()
            summa = self.heads + self.tails
            self.heads_perc = round(self.heads/summa, 4)
            self.tails_perc = 1 - self.heads_perc


    class Analytics(Calculations):
        def predict_random(self, number: int):
            predictions = list()
            for i in range(number):
                heads = randint(0, 1)
                pair = [heads, 1 - heads]
                predictions.append(pair)
            return predictions

        def predict_last(self):
            last_pair = self.data[-1]
            return last_pair

        def save_file(self, data, file_name, extension='txt'):
            filename = file_name + '.' + extension
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(data)

        def num_to_word(self, num: int):
            ans = num
            if num >= 0 and num <= 10:
                ans = config.numbers[num]
            return ans


    def check_content(self, data):
        self.flag = False
        start = 0
        if len(data) > 2:
            if self.has_header:
                start = 1
                header = data[0].split(',')
                if len(header) == 2:
                    for word in header:
                        if word == '':
                            self.flag = True
                            break
                else:
                    self.flag = True

            for i in range(start, len(data)):
                line = data[i].split(',')
                if len(line) == 2:
                    for value in line:
                        value = value.replace('\n', '')
                        if value != '1' and value != '0':
                            self.flag = True
                            break
        else:
            self.flag = True

    def file_reader(self) -> list:
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = file.readlines()

        self.check_content(data)
        if not self.flag:
            start = 0
            if self.has_header:
                start = 1
            self.processed_data = list()
            for i in range(start, len(data)):
                process = data[i].replace('\n', '').split(',')
                temp = list()
                for value in process:
                    temp.append(int(value))
                self.processed_data.append(temp)
        else:
            raise Exception('Incorrect data structure in the file!')



    def print_data(self, data):
        self.analys = self.Analytics(data)
        self.analys.fractions()
        predictions = self.analys.predict_random(3)
        last = self.analys.predict_last()
        print(self.analys.data)
        print(f'{self.heads} {self.tails}')
        print(f'{self.heads_perc} {self.tails_perc}')
        print(predictions)
        print(last)
