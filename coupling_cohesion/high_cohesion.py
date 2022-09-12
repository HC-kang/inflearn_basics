class HighCohesion:
    def __init__(self):
        self.abc = "abc"

    def process_a(self):
        self.abc.process_a

    def process_b(self):
        self.abc.process_b

    def process_c(self):
        self.abc.process_c
