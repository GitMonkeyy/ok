

class Reminder:

    def __init__(self):
        self.rem_array = []

    def add_remind(self, text):
        self.rem_array.append(text)

    def sout_del_rem_list(self, ):
        reminder = None
        if len(self.rem_array) == 0:
            return 'Список нагадувань порожній'
        else:
            for i in range(len(self.rem_array)):
                reminder = f'{self.rem_array[i]}'
                return reminder
