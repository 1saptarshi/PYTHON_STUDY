car=("bmw","bugatti","jaguar","mclaren","gtr")
cars=list(car)
cars[2]="kawashaki"
car=tuple(cars)
for car in cars:
    print(car)

 

fruits =("bmw","bugatti","jaguar","mclaren","gtr",)
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
fruits =("bmw","bugatti","jaguar","mclaren","gtr",)
print("bmw" in fruits)


num = 1,2,3,4,5,6,7,8
k=num*2
print(k)


car=("bmw","bugatti","jaguar","mclaren","gtr")
car1,car2,car3,car4,car5=car
print(car1)
print(car2)
print(car3)
print(car4)
print(car5)



num =(1,2,3,4,5)
*first,middle,last = num
print(first)
print(middle)
print(last)


num =(1,2,3,4,56,7,7,7,7,78,8,8,8,8,9,)
print(num.count(7))

num =(1,2,3,4,7,7,7,78,8,8,8,8,9)
print(num.index(8))


 