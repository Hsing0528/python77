a=int(input('輸入幾筆資料'))
list=['金','銀','銅','優']
list1=[0,0,0,0]
for i in range(a):
    print(list[i],end='')
    list1[i]=int(input())
for i in range(a):
    print('{0}牌得到{1}面'.format(list[i],list1[i]))

# num = int(input("輸入筆數 n:"))
# medals = []
# for i in range(num):
#     medals.append(input().split())
# for medal in medals:
#     print(f"{medal[0]}牌得到 {medal[1]} 面")