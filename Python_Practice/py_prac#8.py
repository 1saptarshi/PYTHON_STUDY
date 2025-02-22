person={"namw":"saptarshi","age":100}
print(type(person))
print(person)


ed ={}
print(type(ed))
print(ed)

edx=dict(name="saptarshi",age=100,date=23/7/2002)
print(type(edx))
print(edx)

edy=dict(name="saptarshi",age=100,date=23,plannet="pluto")
print(edy["name"])
print(edy["age"])
print(edy["plannet"])
print(edy.get("name"))
print(edy.get("vaicle","notfound"))
edy["age"]=200
edy["name"]="@1saptarshi_"
edy["gender"]="alian"
edy.pop("gender")
del edy["date"]
edy.popitem()


print(edy)


