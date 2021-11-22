# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
#
class Parser:

    def __init__(self, filename_in, filename_out):
        self.filename_in = filename_in
        self.filename_out = filename_out
        self.stat = {}

    def statistic(self, number_of_characters):
        with open(self.filename_in, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    event_statistic = line[1:number_of_characters]
                    if event_statistic in self.stat:
                        self.stat[event_statistic] += 1
                    else:
                        self.stat[event_statistic] = 1

    def write_statistic_in_file(self):
        with open(self.filename_out, 'w') as file:
            for data, count in self.stat.items():
                file.write(f'[{data}] {count} \n')

    def minute_statistic(self):
        self.statistic(number_of_characters=17)

    def hour_statistic(self):
        self.statistic(number_of_characters=14)

    def day_statistic(self):
        self.statistic(number_of_characters=11)

    def month_statistic(self):
        self.statistic(number_of_characters=8)

    def year_statistic(self):
        self.statistic(number_of_characters=5)

new_data = Parser('events.txt', 'out_events.txt')

new_data.minute_statistic()
new_data.write_statistic_in_file()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
