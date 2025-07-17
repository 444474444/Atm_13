balance=1000

while True :
    num=  input("사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료):")
    if num == "4":
        break

    if num == '1':
      deposit_amount= int(input('입금할 금액을 입력해주세요'))
      balance+=deposit_amount 
      print(f"입금하신금액은 {deposit_amount}이고, 현재잔액은 {balance}입니다")
    if num =='2':
        pass

    if num =='3':
        pass
    
print(f"시스템을 종료합니다. 현재 잔액은 {balance}")

c