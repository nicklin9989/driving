country = input('請問你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣' :
    if age >= 18:
        print('你可以考駕照')
    else:
        print('你不能考駕照Ｒ')
elif country == '美國' :
    if age >= 16:
        print('你就可以開車')
    else:
        print('你還太嫩回家跟媽媽要錢吧')
else:
    print('只能輸入 台灣／美國')

