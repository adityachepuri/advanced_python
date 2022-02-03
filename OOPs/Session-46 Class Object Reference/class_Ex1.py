class Test:
    def __init__(self):
        print("Constructor Execution")
        print(id(self))
t=Test()
t.__init__()

