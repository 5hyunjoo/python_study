#전달값과 반환값
def deposit(balance, money): # 입금
    print("입금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money): # 출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return(balance)
    
balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)  

def withdraw_night(balnce, money): #저녁에 출금
    commission = 100
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance)) 