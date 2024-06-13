import time
print("pleace insert the card")
time.sleep(5)
password=1234
pin=int(input("Enter your ATM pin "))
balance=5000
if pin==password:
    while True:
        print("""
              1 == Balance
              2 == withdraw balance
              3 == deposit balance
              4 == exit
              """)
        try:
            option=int(input("Pleace enter your choice"))
        except:
            print("pleace enter valid option ")

        if option==1:
            print(f"Your current balance is {balance}")
            print("==============================================================================")
            print("==============================================================================")
            print("==============================================================================")

        if option==2:
            withdraw_amount=int(input("Pleace enter withdraw amount "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is depited form your account ")
            print("==============================================================================")
            print("==============================================================================")
            print(f"your updated balance is {balance} ")
            print("==============================================================================")
            print("==============================================================================")
        if option==3:
            deposit_amount=int(input("pleace enter deposit_amount "))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your amount")
            print("==============================================================================")
            print("==============================================================================")
            print(f"your updated balance is {balance}")
            print("==============================================================================")
            print("==============================================================================")
        if option==4:
            break
else:
    print("wrong pin pleace try again")
