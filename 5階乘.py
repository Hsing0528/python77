m=int(input('輸入階乘值'))
ans=1
for i in range(1,m):
    ans*=i
    if ans>=m:
        break
print('超過m為{0}的階乘值為{1}'.format(m,i))
