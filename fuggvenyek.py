class Muveletek:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("0-val nem osztunk.")
        return a/b
    
