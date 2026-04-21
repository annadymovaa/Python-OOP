from random import randint
import config
import logging
import requests
import os
import token

logging.basicConfig(level=logging.DEBUG, filename='analytics.log', format='%(asctime)s %(message)s')

class DataLoader():
    def __init__(self, filepath, has_header=True):
        self.filepath = filepath
        self.has_header = has_header

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
        logging.debug('Extracting file contents')

    def save_file(self, data, file_name='report', extension='txt'):
        filename = file_name + '.' + extension
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
        logging.debug(f'Saving the data in a file named {filename}')
        return filename

class CoinStatistics():
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
        logging.debug('Calculating the counts of heads and tails')

    def fractions(self):
        self.counts()
        summa = self.heads + self.tails
        self.heads_perc = round(self.heads/summa, 4)
        self.tails_perc = 1 - self.heads_perc
        logging.debug('Calculating the fractions of heads and tails')

    def predict_random(self, number: int):
        predictions = list()
        for i in range(number):
            heads = randint(0, 1)
            pair = [heads, 1 - heads]
            predictions.append(pair)
        logging.debug(f'Predicting {number} tosses')
        return predictions

    def predict_last(self):
        last_pair = self.data[-1]
        logging.debug('Predicting based on the last toss')
        return last_pair
    
    def num_to_word(self, num: int):
        ans = num
        if num >= 0 and num <= 10:
            ans = config.numbers[num]
        logging.debug('Turning numbers into words (0-10 works, the rest stay numbers)')
        return ans
    

class TelegramNotifier():
    def get_message(self, filename):
        message = "The report hasn't been created due to an error"
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            message = "The report has been successfully created"
        logging.debug('Generating a message for the TG channel')
        return message

    def send_message(self, filename):
        message = self.get_message(filename)

        url = f"https://api.telegram.org/bot{token.token}/sendMessage"
        send_inf = {
            'chat_id': token.chat_id,
            'text': message
            }
        response = requests.post(url, data=send_inf)
        logging.debug('Sending a message to the TG channel')
        return response.json()    
