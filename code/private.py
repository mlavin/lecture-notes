class Hidden(object):

    def __init__(self, data):
        self.data = data
        self.__print_data()

    def __print_data(self):
        print(self.data)
