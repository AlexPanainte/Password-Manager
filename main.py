import functions.password_generator as pg
import functions.password_manager as pm

def main():
    pw = pm.PasswordManager()
    password_generator = pg.PasswordGenerator()

    while not pw.logged_in:
        username = input("Introduceți numele de utilizator: ")
        password = input("Introduceți parola: ")
        encryption_key = input("Adăugați cheia de criptare: ")
        pw.login(username, password, encryption_key)

    while True:
        print("--------------------------------")
        print("1. Generare parolă puternică")
        print("2. Stocare parolă")
        print("3. Obținere parolă")
        print("4. Ieșire")
        print("--------------------------------")

        choice = input("Introduceți opțiunea: ")

        if choice == "1":
            password = password_generator.generate_strong_password()
            print("--------------------------------")
            print(f"Parolă generată: {password}")
            

        elif choice == "2":
            service = input("Introduceți numele serviciului asociat parolei: ")
            username = input("Numele de utilizator asociat parolei: ")
            password = input("Parola de stocat: ")

            pw.store_password(service, username, password)

        elif choice == "3":
            print("--------------------------------")
            service = input("Introduceți numele serviciului pentru care este necesară parola: ")
            password = pw.retrieve_password(service)

            if password:
                print("--------------------------------")
                print(f"Parola pentru {service}: {password}")
                
            else:
                print("--------------------------------")
                print(f"Nicio parolă găsită pentru {service}")
                

        elif choice == "4":
            break
        else:
            print("Opțiune invalidă. Vă rugăm să alegeți o opțiune validă.")

if __name__ == "__main__":
    main()
