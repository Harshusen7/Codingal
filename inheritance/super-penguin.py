# parent class
class bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("bird")
        
    def swim(self):
        print("swim faster")

# child class
class penguin(bird):

    def __init__(self):
        # call super() function
        print("penguin is ready")

    def whoisThis(self):
        super().__init__()
        print("penguin")

    def run(self):
        print("run faster")

peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
