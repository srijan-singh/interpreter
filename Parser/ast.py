# Datatype

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class String():
    def __init__(self, value):
        self.value = value
     
    def eval(self):
        return self.value

# Binary Operation

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Mod(BinaryOp):
    def eval(self):
        return self.left.eval() % self.right.eval()

class Concat(BinaryOp):
     def eval(self):
          
          result = '\''

          for elm in self.left.eval():
               if (elm == '\''):
                    continue
               result+=elm

          for elm in self.right.eval():
               if (elm == '\''):
                    continue
               result+=elm

          result += '\''               

          return result

# Identifier

class Identifier():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


# Inbuilt function

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())