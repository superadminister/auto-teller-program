"""
ATM Program
"""

from os import system


def clear():
    system('clear')


clear()
print("""
ATM PROGRAM -
[1] Read Amounts
[2] Send Amounts
\n""")

amount = 100000
while True:
    option_atm = input('your query? : ')

    if option_atm == str(1):
        print('your amount now:', amount)
    elif option_atm == str(2):
        amounts = input('input amounts (numbers): ')
        try:
            if int(amounts) > amount:
                print('values input is too high, your amount is:', amount)
            else:
                print('send success, your amount now:', amount - int(amounts))
                amount = amount - int(amounts)
        except Exception as exceptions:
            print('bad query .. |', exceptions, ', please number input!')

    else:
        print('bad query ..')
