import random

list_of_lists = [
    ['!','@','#','$','%','^','&','*','(',')','-','+','=','{','}','[',']','|',':',';','<','>','.','?','/'],
    [1,2,3,4,5,6,7,8,9,0],
    [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ],
    [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
]

passwordList = ""
length = 8

while(length > 0):
    list_number = random.randint(0, 3)
    charecter_number = random.randint(0, len(list_of_lists[list_number]) - 1)
    passwordList += str(list_of_lists[list_number][charecter_number])
    length -= 1

print(passwordList)