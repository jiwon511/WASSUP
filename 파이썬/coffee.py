#coffee.py
coffee=10
while True:
    money =int(input("돈을 넣어 주세요: "))
    if money == 300:
        print ("커피 제공")
        coffee=coffee-1
        print("남은 커피의 양은 %d개 입니다" % coffee)
    elif money >= 300:
        print("거스름돈 %d를 주고 커피 제공" % (money-300))
        coffee=coffee-1
        print("남은 커피의 양은 %d개 입니다" % coffee)
    else:
        print("돈을 다시 돌려주고 커피를 제공하지 않습니다")
        print("남은 커피의 양은 %d개 입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break