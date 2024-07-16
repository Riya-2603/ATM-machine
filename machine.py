import time
# Here we are describing that what u r going to do first

print("Please Insert your Card")
time.sleep(5)

# Here we have defined the password for the user

password = 6789

#Here we have to enetr the pin number 

pin = int(input("Enter PIN Number: "))

Account_balance = int(input("Enter your Account Balance: "))

Transaction_history = []

if pin == password:
    
    # Here we have defined that what u want to check in yur account you can make the choices here
    
    while True:
        
        print("""
            1 == Account balance 
            2 == Cash withdrawal
            3 == Cash deposit
            4 == PIN change
            5 == Transaction history
            6 == Exit
            """)
        
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Please enter a valid option")
            
            # Here you can check the account balance 
            
        if option == 1:
            print(f"Your account balance is {Account_balance}")
            Transaction_history.append(f"Checked account balance: {Account_balance}")
            
        # Here you will check the account balance and how much you have withdraw from your account
        
        elif option == 2:
            withdraw_amount = int(input("Please enter your amount: "))
            Account_balance = Account_balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your current balance is {Account_balance}")
            Transaction_history.append(f"Withdraw: {withdraw_amount}")
            
        # Here you will check the account balance and how much you have deposited in your account
        
        elif option == 3:
            deposit_amount = int(input("Please enter your amount: "))
            Account_balance = Account_balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your current balance is {Account_balance}")
            Transaction_history.append(f"Deposited: {deposit_amount}")
            
            # Here you can change your pin in your atm machine
        
        elif option == 4:
            old_pin = int(input("Enter your old PIN: "))
            
            if old_pin == pin:
                new_pin = int(input("Enter your new PIN: "))
                pin = new_pin
                print("PIN successfully changed.")
                Transaction_history.append("PIN changed")
            else:
                print("Incorrect old PIN.")
                Transaction_history.append("Failed PIN change attempt due to incorrect old PIN")
                
                #Here you can check your transaction history
        
        elif option == 5:
            if Transaction_history:
                print("\nTransaction History:")
                for transaction in Transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
        
        elif option == 6:
            print("Thank you for using our ATM")    
            break
        
        else:
            print("Invalid choice. Please try again.")
            
else:
    print("Please enter a valid pin number")
