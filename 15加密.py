x=input('輸入一組四位數')
list=[]
for i in x:
        ans=(int(i)+7)%10
        list.append(ans)   
for i in list: 
    print(i,end="")

    
# num = input("輸入一組四位數字為:")
# ans = [(int(i)+7)%10 for i in num  ]
# print(str(ans[2])+str(ans[3])+str(ans[0])+str(ans[1]))

# s =input("輸入一組4位數字為:")
# print("輸出加密後的數字為:",end="")
# print((int(s[2])+7)%10,end="")
# print((int(s[3])+7)%10,end="")
# print((int(s[0])+7)%10,end="")
# print((int(s[1])+7)%10,end="")