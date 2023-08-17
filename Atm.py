class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
    def menu(self):
        
        user_input = input('''
                           
                         Hello, How Would You Like To Proceed ?
                         
                         1.Enter 1 to Create Pin
                         2.Enter 2 to Deposit
                         3.Enter 3 to Withdraw
                         4.Enter 4 to Check balance
                         5.Enter 5 to Exit
                         
                           ''')
        
        if user_input == "1":
            self.create_pin()
            
        elif user_input == "2":
            self.deposit()
        
        elif user_input == "3":
            self.withdraw()
        
        elif user_input == "4":
            self.check_balance()
        
        else:
            print("BBYE ")
    
    def create_pin(self):
        self.pin = input("Enter Your Pin : ")
        print("Pin set successfully")
        
    def deposit(self):
        temp = input("Enter your pin : ") 
        if temp == self.pin:
            amount = int(input("Enter Your Amount : "))
            self.balance = self.balance + amount
            print("Deposit successfull")
        else:
            print("Invalid pin")
    
    def withdraw(self):
        temp = input("Enter your pin : ")  
        if temp == self.pin:
            amount = int(input("Enter Your Amount : "))
            if amount<self.balance:
                self.balance = self.balance - amount
                print("Operation Successfull")
            else:
                print("Insufficiant funds")
        else:
            print("Invalid pin")
    
    def check_balance(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
            
            


sbi = Atm()
sbi.create_pin()
sbi.deposit()
sbi.withdraw()
sbi.check_balance()