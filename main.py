"""
Brendon Busker's Ammortization Calculator
for FIN 3309 at Baylor University
"""

def main():
    print()
    print('Welcome To The Ammortization Calculator')
    print('Please Enter The Specified Values Below')
    print('----------------------------------------')

    # loop bool
    loop = True
    yearly = "y"
    
    # Input values
    while loop:
        try:
            beg_balance = float(input('Enter Beginning Balance Amount: '))
            rate = float(input('Enter Rate (MUST BE DECIMAL FORM): '))
            payment = float(input('Enter Payment (GET FROM TVM CALC): '))
            year = int(input('Enter Years/Months: '))
            yearly = str(input("Enter 'y' for yearly, enter 'm' for monthly: "))
            loop = False
        
        except:
            print('You entered something wrong. Please start over.\n')

    # Runs the calculator
    if yearly == 'y':
        calc_yearly(beg_balance, rate, payment, year)
    
    elif yearly == 'm':
        calc_monthly(beg_balance, rate, payment, year)
    
    else:
        print("You did not enter 'y' or 'm' for years/months, run program again.")

def calc_yearly(beg_balance, rate, payment, year):
    print('-' * 86)
    print('YEAR', '|BEGINNING BALANCE', '|TOTAL PAYMENT', '|INTEREST PAYMENT', '|PRINCIPAL PAYMENT', '|ENDING BALANCE', sep = '')
    print('-' * 86)

    total_interest = 0

    for i in range(1, year+1):
        interest = beg_balance * rate
        principal = payment - interest
        end_balance = beg_balance - principal

        print(f'{i:<4}', f'{round(beg_balance,2):<17}', f'{round(payment,2):<13}',
               f'{round(interest,2):<16}', f'{round(principal,2):<17}', round(end_balance,2))

        beg_balance = end_balance
        total_interest += round(interest,2)
    
    print()
    print(f"Total Interest: {round(total_interest,2)}")

def calc_monthly(beg_balance, rate, payment, year):
    print('-' * 87)
    print('MONTH', '|BEGINNING BALANCE', '|TOTAL PAYMENT', '|INTEREST PAYMENT', '|PRINCIPAL PAYMENT', '|ENDING BALANCE', sep = '')
    print('-' * 87)

    total_interest = 0

    for i in range(1, year+1):
        interest = (rate/12) * beg_balance
        principal = payment - interest
        end_balance = beg_balance - principal

        print(f'{i:<5}', f'{round(beg_balance,2):<17}', f'{round(payment,2):<13}',
               f'{round(interest,2):<16}', f'{round(principal,2):<17}', round(end_balance,2))

        beg_balance = end_balance
        total_interest += round(interest,2)
    
    print()
    print(f"Total Interest: {round(total_interest,2)}")

# Runs Program
main()

