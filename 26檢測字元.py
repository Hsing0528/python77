s = input("檢測的字串(end結束):")
while s != "end":
    s = input("\n檢測的字串(end結束):")
    char = input("檢測的單一字元:")
    print(f"字元 {char} 出現次數為:{s.count(char)}")
print("檢測結束")