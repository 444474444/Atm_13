balance=  1000
receipts=[]

while True :
    num=  input("사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료):")
    if num == "4":
        break

    if num == '1':
      deposit_amount= int(input('입금할 금액을 입력해주세요'))
      balance+=deposit_amount 
      print(f"입금하신금액은 {deposit_amount}이고, 현재잔액은 {balance}입니다")
      receipts.append(("입금:",deposit_amount,balance))
    
    if num =='2':
        
      withdraw_amount =int(input('출금할 금액을 입력해주세요'))
      withdraw_amount =min(balance,withdraw_amount)
      balance-=withdraw_amount
      print(f"출금 가능하신 금액은 {withdraw_amount}이고,현재잔액은{balance}입니다")
      receipts.append(("출금:",withdraw_amount,balance))
    if num =='3': 
        if receipts:
         for i in receipts:
           print(f"{i[0]}: {i[1]}원 ㅣ 잔액: {i[2]}원")
        else:
            print("영수증 내역이 없습니다.")
print(f"시스템을 종료합니다. 현재 잔액은 {balance}")
