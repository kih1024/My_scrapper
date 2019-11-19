# b = 'asdas'
# a = 'asdas'
# c = 'asdas'
# day = ["mon", "tue", "wed"]
# # day = ("mon","tue","wed") 이것은 튜플 변경 불가능.요소 추가,수정,삭제 불가능
# inho = {
#     "age": 21,
#     "name": "inho",
#     "from": "south korea",
#     "fav_food": ["kimchi", "pizza"]
# }

# def func(who):
#     print("hi kim", who)

# def plus(a,b=0):
#     print(a+b)

# def keyword_argument(a,b):
#     return a-b


# def say_hello(name,age):
#     return f"Hello {name} you are {age} years old!"



# hello=say_hello("inho","24")
# print(hello)
# print(keyword_argument(b=10,a=3))
# plus(5)
# day.append("sat")
# day.reverse()
# print(len(day))
# print(day)  
# print(type(day))
# print("mon" in day)
# print(inho)
# print(inho["fav_food"])
# func("inho")

def plus(a,b):
    if type(b) is int or type(b) is float:
        print(a+b)
        return a+b
    else:
        return None

plus(12,5.4)

def age_check(age):
    print(f"you are {age}")
    if age<18:
        print("you cant drink")
    elif age==18:
        print("you are new to this!")
    else:
        print("enjoy your drink")

age_check(29)

days = ["m","T","w","T",'F']

for day in days:
    print(day)

from math import ceil, fsum as sexy

print(ceil(1.2))
print(sexy([1,2,3,4,5,6]))

from cal import plus

print(plus(4.1,9.2))