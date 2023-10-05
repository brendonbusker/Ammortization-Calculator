"""
Brendon Busker's Ammortization Calculator
for FIN 3309 at Baylor University
"""

def main():
    print()
    print('Welcome To The Ammortization Calculator')
    print('Please Enter The Specified Values Below')
    print('----------------------------------------')
    
    # Input values
    beg_balance = float(input('Enter Beginning Balance Amount: '))
    rate = float(input('Enter Rate (MUST BE DECIMAL FORM): '))
    payment = float(input('Enter Payment (GET FROM TVM CALC): '))
    year = int(input('Enter Years: '))
    

    # Runs the calculator
    calc(beg_balance, rate, payment, year)

def calc(beg_balance, rate, payment, year):
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
        total_interest += interest
    
    print()
    print(f"Total Interest: {round(total_interest,2)}")

# Runs Program
main()

