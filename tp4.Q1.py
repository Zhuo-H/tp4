class StringFoo:
    def __init__(self, message):
        self.message = message

    def printstring(self):
        print(self.message.upper())


m1 = StringFoo("i like apples")

m1.printstring()
