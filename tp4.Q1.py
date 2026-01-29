""""""""""
IMPORTANT:
    TOUS LES INFOS SONT DANS README.md

"""""""""

class StringFoo:
    def __init__(self):
        self.message = ''

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message.upper())


m1 = StringFoo()
m1.set_string('i like apples and oranges')
m1.print_string()
