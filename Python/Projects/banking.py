import random
import sqlite3
from pprint import pprint

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


#  deleteTable, printTable are for debugging
def createTable(table_name: str = 'card') -> None:
    cur.execute(
        f'CREATE TABLE IF NOT EXISTS {table_name} ( \
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            number TEXT, \
            pin TEXT, \
            balance INTEGER DEFAULT 0 \
        );')
    conn.commit()
    table = cur.fetchall()
    print(table)


def deleteTable(table_name: str = 'card') -> None:
    cur.execute(f'DROP TABLE ?;', (table_name,))
    conn.commit()
    # cur.fetchall()


def printTable(table_name: str = 'card') -> None:
    cur.execute(f'SELECT * FROM ?', (table_name,))
    conn.commit()
    pprint(cur.fetchall())


def generateCard() -> None:
    card_number = 4000_00 * 100_0000_000 \
        + random.randrange(10_0000_000, 99_9999_999)
    pin_number = random.randrange(9999)

    luhn_sum = luhnSum(card_number)

    card_number = card_number * 10 + ((10 - (luhn_sum % 10)) % 10)

    cur.execute(f'INSERT INTO card (number, pin) VALUES (?, ?);',
        (card_number, pin_number))
    conn.commit()

    print('\nYour card has been created')
    print('Your card number:')
    print(card_number)
    print('Your card PIN:')
    print(f'{pin_number:04d}')


def login() -> bool:
    login_number = input('\nEnter your card number: ').strip()
    login_pin = input('Enter your PIN: ').strip()

    cur.execute(
        'SELECT id FROM card WHERE number = ? AND pin = ?',
        (login_number, login_pin))
    conn.commit()
    user_id = cur.fetchone()

    if not user_id:
        print('\nWrong card number or PIN!')
        return False

    user_id = user_id[0]

    print('\nYou have successfully logged in!')

    # logged in menu
    while True:
        print('\n1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')

        try:
            login_command = int(input().strip())
        except ValueError: continue

        if login_command == 1: printBalance(user_id)
        elif login_command == 2: addIncome(user_id)
        elif login_command == 3: transfer(user_id)
        elif login_command == 4: deleteAccount(user_id); return False
        elif login_command == 5: return False
        elif login_command == 0: return True


def printBalance(user_id: int) -> None:
    cur.execute(f'SELECT balance FROM card WHERE id = ?;', (user_id,))
    conn.commit()
    user_balance = cur.fetchone()[0]
    print(f'\nBalance: {user_balance}')


def addIncome(user_id: int) -> None:
    income = int(input('\nEnter income: ').strip())

    cur.execute(
        f'UPDATE card SET balance = balance + ? WHERE id = ?;',
        (income, user_id))
    conn.commit()
    print('Income was added!')


def transfer(user_id: int) -> None:
    print('Transfer')
    transfer_number = input('Enter card number: ').strip()

    cur.execute(f'SELECT number, balance FROM card WHERE id = ?;', (user_id,))
    conn.commit()
    user_number, user_balance = cur.fetchone()

    cur.execute(f'SELECT * FROM card WHERE number = ?;', (transfer_number,))
    conn.commit()
    transfer_data = cur.fetchone()

    if luhnSum(int(transfer_number)) % 10 != 0:
        print('Probably you made mistake in the card number. \
            Please try again!')
    elif transfer_number == user_number:
        print("You can't transfer money to the same account!")
    elif not transfer_data:
        print('Such a card does not exist')
    else:
        transfer_amount = \
            int(input('Enter how much money you want to transfer: ').strip())
        if transfer_amount > user_balance:
            print('Not enough money!')
            return

        cur.execute(
            f'UPDATE card SET balance = balance + ? WHERE number = ?;',
            (transfer_amount, transfer_number))
        conn.commit()

        cur.execute(
            f'UPDATE card SET balance = balance - ? WHERE id = ?;',
            (transfer_amount, user_id))
        conn.commit()

        print('Success!')


def deleteAccount(user_id: int) -> None:
    cur.execute('DELETE FROM card WHERE id = ?', (user_id,))
    conn.commit()


def luhnSum(number: int) -> int:
    luhn_digits_1 = [int(i) for i in str(number)]
    luhn_digits_2 = [
        v * 2 if i % 2 == 0 else v 
        for i, v in enumerate(luhn_digits_1)]
    luhn_digits_3 = [i - 9 if i > 9 else i for i in luhn_digits_2]
    return sum(luhn_digits_3)


def menu() -> None:
    done = False
    while True and not done:
        print('\n1. Create an account')
        print('2. Log into account')
        print('0. Exit')

        try:
            user_input = int(input().strip())
        except ValueError: continue

        if user_input == 1: generateCard()
        elif user_input == 2: done = login()
        elif user_input == 0: done = True

    print('\nBye!')


def main() -> None:
    createTable('card')
    menu()
    # deleteTable('card')


if __name__ == '__main__':
    main()
