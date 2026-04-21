from config import *
from analytics import *

if __name__ == '__main__':

    obj = DataLoader(filepath)
    obj.file_reader() #obj.processed_data created

    analysis = CoinStatistics(obj.processed_data)
    analysis.fractions() #analysis.heads & analysis.tails & analysis.heads_perc & analysis.tails_perc created
    heads = analysis.num_to_word(analysis.heads)
    tails = analysis.num_to_word(analysis.tails)
    summa = analysis.num_to_word(analysis.heads + analysis.tails)

    heads_perc = analysis.num_to_word(analysis.heads_perc*100)
    tails_perc = analysis.num_to_word(analysis.tails_perc*100)

    predictions = analysis.predict_random(number)
    predict = CoinStatistics(predictions) #created a new object where self.data=predictions
    predict.counts()

    pred_tails = analysis.num_to_word(predict.tails)
    pred_heads = analysis.num_to_word(predict.heads)

    data = text.format(summa=summa, tails=tails, heads=heads, tails_perc=tails_perc, heads_perc= heads_perc, number=number, pred_tails=pred_tails, pred_heads=pred_heads)
    filename = obj.save_file(data, file_to_save)
    message = TelegramNotifier()
    message.send_message(filename)
