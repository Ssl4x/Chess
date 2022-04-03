class Test:
    def __init__(self):
        pass

    def public(self):
        print("public")

    def call_privat(self):
        self.__private()

    def __private(self):
        print("private")


obj = Test()
obj.public()
obj.call_privat()
obj.__private()