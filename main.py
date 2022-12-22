# x = 7
# y = 10
# result = y % x
# # result = int(y / x)
# # result = y // x
# print(result)

# print("Hi " , end='\n ')
# print("world")

# number = int(input("Number: "))
# print(number - 5)
# https://github.com/mrbadri/basic_python.git
# print(type("test"))

# str = "heLLo".lower().count('l')
# print(str)


# x = "hello"
# y= 3
# print(x + y)

# True 
# False


# == 
# != 
# <= 
# >=
# <
# >

# x = "Hello"
# y= 'HelLo'
# print(x != y)

# print('a' > 'z')
# print(ord('ab'))
# print(ord('Z'))

# x = 7
# y = 8
# z = 0

# r1 = x == y
# r2 = y > x
# r3 = z < x + 2

# # or
# # and 
# # not
# print(not (False and True or True))


# x = input("Name: ")

# if( x == "Tim"):
#     print("You are great!")
# elif (x == "Joe"):
#     print("By Joe")
# else: 
#     print('No')

# print("Always do this")


# x = [4, True, 'hi']
# # y= "hi"
# # x.append("hello")
# # x.extend([1,2,3,4,5])
# print(x.pop(0))
# # print(len(x)  , len(y))
# y = x[:]
# x[0] = "hello"

# print(x , y)

# x = (1,2,3,4)

# print(x[0])




# for i in range(10): 
#     print(i)





# i = 0

# while True: 
#     print(i)
#     i += 1
#     if i == 10:
#         break


# arr = [1,2,3,4,5,6,7,8]

# result = arr[1:9:2]
# result = arr[::3]
# result = arr[5::-1]
# result = arr[len(arr)::-2]

# # Start:Stop:Step

# print(result)



# x = set()
# s = {1,2,3,4,5}
# s2 = {1,2,31,4,15}

# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))

# s.add(6)

# print(s)
# print(3 in s)


#  --------------------
# def test(num1, num2=4):
#     for i in range(num1):
#         for j in range(num2):
#             print('b')
            
        
#     return num1 * num2

# test(2 , 2)

# print('%9f'% 10)


#  --------------------
# import math

# def test(a ,b ,c):
#     p = (a + b + c) / 2
#     r = p * (p - a ) * (p - b) * (p - c)
    
#     print(round(math.sqrt(r) , 9))
#     print(round(r**0.5 , 2))
#     print("%.5f" % r**0.5)
    

# test(2 , 2 , 3)

# a , b , c = map(int, input().split())
# print(a)


#  --------------------
#  for get multi input
while True:
    s = ''
    line = 0
    chars = 0
    
    try:
        s = input("enter")
    except:
        break
    
    cnt = 0
    for c in s:
        # if c.isalpha():
        if (ord('a') <= ord(c) and ord(c) <= ord('z')) or ord('A') <= ord(c) and ord(c) <= ord('Z'):
            cnt += 1
    if cnt > 0:
        line += 1
        
    chars += cnt
    
    print(line)
    print(chars)
    
    
    









    