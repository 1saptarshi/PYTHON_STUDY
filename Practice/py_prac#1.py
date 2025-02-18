print("hi")

if 10 < 100:
    print("hundred is grater tha ten")

    x =10
    print(type(x))

    a= 10.0
    print(type(a))
    w ='hi men'
    print(type(w))

    cars =['BMW','BBT','LAMBERGINI','BUATTI','ROLLS ROYLES','BENTLY']
    print(type(cars))
car=('BMW','BBT','LAMBERGINI','BUATTI','ROLLS ROYLES','BENTLY')
print(type(car))

ca ={'BMW','BBT','LAMBERGINI','BUATTI','ROLLS ROYLES','BENTLY'}
print(type(ca))

 
s = "saptarshi"
print(s*7)
 
num =range(10)
print(num)


frozen_numbers = frozenset([1, 2, 3, 4, 5])
print(type(frozen_numbers))  # Output: <class 'frozenset'>



num = frozenset([1,2,3,4,5,6,7,8,9,])
print(num)



info ={"Name":"saptarshi","Age":23}
print(type(info))
print(info)



byte_data = b"saptarshi"
print(type(byte_data))  # Output: <class 'bytes'>


empty_value = None
print(type(empty_value))  # Output: <class 'NoneType'>

a= None
print(type(a))


a=100
b=2
print("Addition:", a + b)        
print("Subtraction:", a - b)     
print("Multiplication:", a * b)  
print("Division:", a / b)        
print("Floor Division:", a // b)  
print("Modulus:", a % b)        
print("Exponentiation:", a ** b)  


s="hi"
d="bro"
r=s+" "+d
print(r)


cars=["BMW","BUGATTI","MClaren"]
race=" ".join(cars)
print(race)


n="saptarshi"
a=100
info=f"my name is {n} and i am {a} year old men"

print(info)


name="aptarshi"
planate="pluto"
info="hi Buddy, my name is {} and i am from {}".format(name,planate)
print(info)

