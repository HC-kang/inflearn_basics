class LowCohesion:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'
        
    def process_a(self):
        print(self.a)
        
    def process_b(self):
        print(self.b)
        
    def process_c(self):
        print(self.c)
