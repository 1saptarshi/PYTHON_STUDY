class MyFirstClass:
    """This is a document string..."""
    class_var1 = 100   # class or static variable
    class_var2 = 200
    def _init_(self,data1, data2): # Constructor method  positional parameters
        print("Executing the constructor method...")   # self is called an object binding variable
        print("self:", self, type(self))
        self.inst_var1 = data1   # instance variable
        self.inst_var2 = data2
    def display(self):
        print("Executing the display method...")
        print(f"Class variable values are {MyFirstClass.class_var1} and {MyFirstClass.class_var2}...")
        print(f"Class varibale values are {self.class_var1} and {self.class_var2}... ")
        print(f"Instane variable values are {self.inst_var1} and {self.inst_var2}...")
        
    def update(self):
        print("Updating class variable...")
        MyFirstClass.class_var1 += 100
        MyFirstClass.class_var2 += 120
        
ob1 = MyFirstClass(111,222) # positional arguments
ob1.display()
 
ob2 = MyFirstClass(333, 444)
ob2.display()
 
print ()
ob1.update()
ob1.display()