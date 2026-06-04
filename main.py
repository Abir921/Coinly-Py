from datetime import date

def showMenu():
    
    print("------------------")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Balance")
    print("4. Edit Transaction")
    print("5. Delete Transaction")
    print("6. Exit")


transactions = []
flag = True
values = {
    "date": "",
    "amount": 0.0,
    "category": "",
    "description": ""
}


print("\nWELCOME TO COINLY")
while flag:
    showMenu()
    option = input("Select an option: ")
    match option:
        case "1":
            # Add Transaction logic
            today = date.today()
            values["date"] = today
            values["amount"] = float(input("Enter amount: "))
            values["category"] = input("Enter category(income/expense): ")
            values["description"] = input("Enter description: ")
            transactions.append(values.copy())
            print("\nTransaction added successfully!")
            
        case "2":
            # View Transactions logic
            for tx in transactions:
                print(f"DATE: {tx['date']},\n AMOUNT: {tx['amount']},\n CATEGORY: {tx['category']},\n DESCRIPTION: {tx['description']}\n")
            
        case "3":
            # View Balance logic
            balance = 0.0
            balance += sum(tx["amount"] for tx in transactions if tx["category"] == "income")
            balance -= sum(tx["amount"] for tx in transactions if tx["category"] == "expense")
            print(f"\nCurrent Balance: {balance}")
            pass
        case "4":
            # Edit Transaction logic
            pass
        case "5":
            # Delete Transaction logic
            pass
        case "6":
            # Exit logic
            flag = False
            
        case _:
            print("Invalid option. Please try again.")


