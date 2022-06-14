x=input('輸入數列').split()
half='NO'
for num in x:
    if x.count(num)>len(x)/2:
        half=num   
        break
print(f'過半元素為:{num}')

