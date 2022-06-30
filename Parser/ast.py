# Datatype

NIL = None

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class String():
    def __init__(self, value):
        self.value = value
     
    def eval(self):
        return self.value[1:-1]

class Array():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


# Boolean

class TRUE():
    def __init__(self):
        self.value = Number(1)

    def eval(self):
        return self.value.eval()   

class FALSE():
    def __init__(self):
        self.value = Number(0)

    def eval(self):
        return self.value.eval()     

# Inbuilt function

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
