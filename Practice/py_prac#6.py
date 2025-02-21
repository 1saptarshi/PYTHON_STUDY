phone=["apple","sumsung","vivo","oppo","oeplus","redmi"]

print(phone[0])
print(phone[1])
print(phone[-1])
print(phone[2])
print(phone[-2])
print(phone[3])
print(phone[-3])
print(phone[+1])
print(phone[+3])
phone[+1]="mango"
phone[-1]="banana"
print(phone)
print(len(phone))
phone.append("xiomi")
phone.append("Nokia")
phone.insert(2,"pinapel")
phone.extend(["copi","phonu","lappy"])
phone.remove("phonu")
phone.pop(2)
del phone[3]

print(phone)
