import functions.baza_de_date as dbs
import functions.password_generator as pg
import functions.password_manager as pm
import functions.menu as m


def main():
    db = dbs.Database()
    pwm = pm.PasswordManager()
    pwg=pg.PasswordGenerator()

    while True:
        m.main_menu()

        choice = input("Choose one option: ")

        if choice == "1":
            username = input("Add username: ")
            password = input("Add password: ")
            encryption_key=input("Add encryption key: ")
            status = db.log_in(username, password,encryption_key)
            if status:
                print("\nLog In successful\n")

                while True:
                    m.operations()
                    operation_choice = input("Choose one operation: ")

                    if operation_choice == "1":
                        generated_password = pwg.generate_password()
                        print(f"\nGenerated Password: {generated_password}\n")

                    elif operation_choice == "2":
                        service = input("Enter service name: ")
                        username= input("Enter account name: ")
                        password= input("Enter password name: ")

                        pwm.store_account(encryption_key,service,username, password)

                    elif operation_choice == "3":
                        service = input("Enter service name: ")
                        print(pwm.get_password(service,encryption_key))
                        
                    elif operation_choice == "4":
                        break

                    else:
                        print("Invalid operation choice. Please choose a valid option.\n")

            else:
                print("Username or password is incorrect.\n")

        elif choice == "2":
            username = input("Add username: ")
            password = input("Add password: ")

            encryption_key = pwm.generate_encryption_key()
            db.register(username, password, encryption_key)

            print(f"You have been successfully registered\nYour encryption key is {encryption_key}\n")
            while True:
                m.return_menu()
                return_choice = input("Choose one option: ")

                if return_choice == "1":
                    break

                elif return_choice == "2":
                    return  # Exit the program

                else:
                    print("Invalid return choice. Please choose a valid option.\n")

        elif choice == "3":
            break

        else:
            print("Invalid option. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
