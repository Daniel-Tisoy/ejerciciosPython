from datetime import datetime

today = datetime.now().strftime('%Y/%m/%d')


class PythonProject():

    def __init__(self, msg):

        self.msg = msg
        self.print_message()

    def print_message(self):
        print(self.msg)


class Utilites(PythonProject):
    def print_message(self):
        print(self.msg, '@', today)


if __name__ == '__main__':

    print('Hi')
    message = "I'm daniel"
    project = PythonProject(message)
    util = Utilites(message)
