a=int(input('輸入西元年:'))
if a%12==0:
    print('猴')
elif a%12==1:
    print('雞')
elif a%12==2:
    print('狗')
elif a%12==3:
    print('豬')
elif a%12==4:
    print('鼠')
elif a%12==5:
    print('牛')
elif a%12==6:
    print('虎')
elif a%12==7:
    print('兔')
elif a%12==8:
    print('龍')
elif a%12==9:
    print('蛇')
elif a%12==10:
    print('馬')
elif a%12==11:
    print('羊')
# year=int(input('请输入年份：'))
# nianfen = ['申猴' ,'酉鸡' ,'戌狗' ,'亥猪' ,'子鼠' ,'丑牛' ,'寅虎' ,'卯兔' ,'辰龙' ,'巳蛇' ,'午马' ,'未羊']
# print('这一年生肖为{}'.format(nianfen[year%12]))