def showMenu():
    print("WELCOME TO COINLY")
    print("------------------")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Balance")
    print("4.Edit Transaction")
    print("5. Delete Transaction")
    print("6. Exit")


flag = True
while flag:
    showMenu()


option = input("Select an option: ")

match option:
    case "1":
        # Add Transaction logic 
        pass
    case "2":
        # View Transactions logic
        pass
    case "3":
        # View Balance logic
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