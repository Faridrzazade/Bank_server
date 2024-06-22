
import time
import os

from datetime import datetime




class BankAccount:
    def __init__(self, name, sur_name, quantity, annual_interest, password, year, month, day):
        self.name = name
        self.sur_name = sur_name
        self.quantity = quantity
        self.annual_interest = annual_interest
        self.password = password
        self.year = year
        self.month = month
        self.day = day
    
    def display_information(self):
        print(f"Name: {self.name},\nSur_name: {self.sur_name},\nQuantity: {self.quantity},\nAnnual_interest: {self.annual_interest},\nYear: {self.year}, \nMonth: {self.month},\nDay: {self.day}")

    def check_password(self, entered_password):
        if self.password == entered_password:
            print("Password is correct")
            return True
        else:
            return False
            os.system("clear")
def calculate_interest(bank_account, today_year, today_month, today_day):
    calculation_year = today_year - bank_account.year
    calculation_month = today_month - bank_account.month
    calculation_day = today_day - bank_account.day

    year_the_day = abs(calculation_year) * 365
    month_the_day = abs(calculation_month) * 30
    day_the_day = abs(calculation_day)
    total_days = year_the_day + month_the_day + day_the_day

    total_month = total_days / 365 * 12
    
    calculation_interest = bank_account.quantity * bank_account.annual_interest / 100
    calculation = total_month * calculation_interest
    
    bank_account.quantity += calculation

    print("Interest calculated and added to the account.")

current_datetime = datetime.now()
today_year = current_datetime.year
today_month = current_datetime.month
today_day = current_datetime.day


user_password = input("Enter your password\n: ")
user_name = input("Enter your name\n: ")
user_sur_name = input("Enter your sur name\n: ")
user_quantity = int(input("Enter your quantity\n: "))


bank_account = BankAccount(user_name, user_sur_name, user_quantity, 5, user_password, 1996, 9, 18)

check_password_input = input("Enter your password to login \n:")
time.sleep(2)

if bank_account.check_password(check_password_input):
    calculate_interest(bank_account, today_year, today_month, today_day)
    
    try:
        check_quantity = int(input("Enter the amount you want to withdraw: "))
        if bank_account.quantity >= check_quantity:
            new_quantity = bank_account.quantity - check_quantity
            bank_account.quantity = new_quantity
            print("Your new balance:", new_quantity)
        else:
            print("Insufficient funds.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
else:
    print("Password is incorrect")
os.system("clear")
bank_account.display_information()
