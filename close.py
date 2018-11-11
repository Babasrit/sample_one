'''def f():
    print("complte")
a=f
f()
def first(msg):
    message=msg
    def second(t):
        message="hello"
        print(message)
        print(t*3)
    return second
if __name__=="__main__":
    a=first("Hi")
    a(3)
    print(f'file_name = {__name__}')'''

'''def first(original):
    print("First")
    first.__call__=0
    def second(*args,**kwargs):
        first.__call__+=1
        print(f"This function is executed before {original.__name__}")
        return original(*args,**kwargs)
    
    #print("Total calls",first.__call__)
    return second
@first
def dispaly(name,age):
    c=0
    print("Total calls",first.__call__)
    print(f'My name is {name} and my age is {age}')

dispaly('Babu',25)'''
'''class red:
    def __init__(self):
        self._update()
    def _update(self):
        print("I am printing")
a=red()
a._update()'''
class first:
    c=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def second(self):
        print("Total count:",first.c)
        print(self.name+'@gmail.com')
    def third(self):
        print(self.age)
class func(first):
    def __init__(self,model,year,name,age):
        self.model=model
        self.year=year
        super().__init__(name,age)
    def sample(self):
        print(self.name+str(self.age))
        print(f'printing {self.model} in {self.year} executed after {func.__name__}')
'''b=first("babu",25)
b.second()
c=b.third()
c'''
b=func('Note4',2016,"babu",23)
b.sample()


