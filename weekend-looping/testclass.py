class Testclass():
    def init(self,fname, lname):
        self.fname = fname
        self.lname = lname
    def user(self):
        greet = "Hello {self.fname} {self.lname} and welcome to the world of Programing"
        return greet
