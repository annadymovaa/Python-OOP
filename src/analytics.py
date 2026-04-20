import sys

class Research():
    def __init__(self, filepath):
        self.filepath = filepath
        self.calc = self.Calculations()

    class Calculations():
        def counts(self, data):
            count_heads = 0
            count_tails = 0
            for pair in data:
                if pair[0] == 1:
                    count_heads += 1
                else:
                    count_tails += 1
            return count_heads, count_tails

        def fractions(self, heads, tails):
            summa = heads + tails
            heads_perc = round(heads/summa, 4)
            tails_perc = 1 - heads_perc
            return heads_perc, tails_perc

    def check_content(self, data, has_header):
        self.flag = False
        start = 0
        if len(data) > 2:
            if has_header:
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

    def file_reader(self, has_header=True) -> list:
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = file.readlines()

        self.check_content(data, has_header)
        if not self.flag:
            start = 0
            if has_header:
                start = 1
            processed_data = list()
            for i in range(start, len(data)):
                process = data[i].replace('\n', '').split(',')
                temp = list()
                for value in process:
                    temp.append(int(value))
                processed_data.append(temp)

            return processed_data
        else:
            raise Exception('Incorrect data structure in the file!')



    def print_data(self, data):
        heads, tails = self.calc.counts(data)
        heads_perc, tails_perc = self.calc.fractions(heads, tails)
        print(data)
        print(f'{heads} {tails}')
        print(f'{heads_perc} {tails_perc}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        obj = Research(filepath)
        data = obj.file_reader(False)
        obj.print_data(data)


