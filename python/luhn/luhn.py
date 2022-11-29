class Luhn:
    def __init__(self, card_num):
        self.card_num = str(card_num).strip().replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1:
            return False

        try:
            int_list = [int(i) for i in self.card_num]
        except:
            return False

        for x in range(len(int_list) - 2, -1, -2):
            if int_list[x] * 2 > 9:
                int_list[x] = int_list[x] * 2 - 9
            else:
                int_list[x] = int_list[x] * 2

        adjusted_sum = 0

        for x in int_list:
            adjusted_sum = adjusted_sum + x

        if adjusted_sum % 10 == 0:
            return True
        else:
            return False
