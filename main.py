expenses = []
books = {}
count = 0

def add():
    global count

    name = input("Enter expense: ")
    cat = input("Enter category: ")
    amt = int(input("Enter amount: "))
    date = input("Enter date: ")

    count += 1

    books[count] = (count, name, cat, amt, date)
    expenses.append(amt)

    print("Expense added.")
    print("Expense ID:", count)


def show():
    if len(books) == 0:
        print("No expenses.")
        return

    print("\n===== EXPENSES =====")

    for n in books:
        x = books[n]

        print("ID:", x[0])
        print("Expense:", x[1])
        print("Category:", x[2])
        print("Amount: Rs.", x[3])
        print("Date:", x[4])
        print()


def search():
    if len(books) == 0:
        print("No expenses.")
        return

    n = int(input("Enter expense ID: "))

    if n in books:
        x = books[n]

        print("\nExpense found")
        print("ID:", x[0])
        print("Expense:", x[1])
        print("Category:", x[2])
        print("Amount: Rs.", x[3])
        print("Date:", x[4])
    else:
        print("Expense not found.")


def delete():
    if len(books) == 0:
        print("No expenses.")
        return

    n = int(input("Enter expense ID: "))

    if n in books:
        x = books[n]

        expenses.remove(x[3])
        del books[n]

        print("Expense deleted.")
    else:
        print("Expense not found.")


def report():
    if len(expenses) == 0:
        print("No expenses.")
        return

    total = 0

    for x in expenses:
        total = total + x

    high = expenses[0]
    low = expenses[0]

    for x in expenses:
        if x > high:
            high = x

        if x < low:
            low = x

    print("\n===== REPORT =====")
    print("Total expenses:", len(expenses))
    print("Total amount: Rs.", total)
    print("Highest expense: Rs.", high)
    print("Lowest expense: Rs.", low)


def main():
    while True:
        print("\n===== EXPENSE MANAGER =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Expense Report")
        print("6. Exit")

        n = int(input("Enter choice: "))

        if n == 1:
            add()

        elif n == 2:
            show()

        elif n == 3:
            search()

        elif n == 4:
            delete()

        elif n == 5:
            report()

        elif n == 6:
            print("Thank you!")
            break

        else:
            print("Wrong choice.")


main()
