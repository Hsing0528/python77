a=int(input('輸入一個度數'))
one=120*2.1
two=210*3.02,210*2.68
three=170*4.39,170*3.61
four=200*5.63,200*4.5
if a<=120:
    yes=no=a*2.1
elif 120<a<=330:
    a-=120
    yes=one+a*3.02
    no=one+a*2.68
elif 330<a<=500:
    a-=330
    yes=one+two[0]+a*4.39
    no=one+two[1]+a*3.61
elif 500<a<=700:
    a-=500
    yes=one+two[0]+three[0]+a*4.97
    no=one+two[1]+three[1]+a*4.01
elif a>700:
    a-=700
    yes=one+two[0]+three[0]+four[0]+a*5.63
    no=one+two[1]+three[1]+four[1]+a*4.5
print('夏月電費:%.2f'%yes)
print('非夏月電費:%.2f'%no)