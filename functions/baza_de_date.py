import mysql.connector
class Database:
    def __init__(self):
        self.connect = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Afd3ufy250137@",  # Schimbă această parolă cu parola reală a bazei de date
                        database="accounts")
        self.cursor = self.connect.cursor()

    def register(self, username, password, encryption_key):
        try:
            # Folosește parametri în loc de interpolarea directă a șirurilor pentru a evita SQL Injection
            query = "INSERT INTO REGISTERED_USERS (username, password, encryption_key) VALUES (%s, %s, %s);"
            data = (username, password, encryption_key)
            
            self.cursor.execute(query, data)
            self.connect.commit()
            print("Utilizator înregistrat cu succes!")
        except mysql.connector.Error as err:
            print(f"Eroare la înregistrarea utilizatorului: {err}")
        finally:
            self.cursor.close()
            self.connect.close()

    def select_info_for_log_in(self):
        querry="SELECT USERNAME,PASSWORD,ENCRYPTION_KEY FROM accounts.registered_users;"
        self.cursor.execute(querry)

        rows = self.cursor.fetchall()
        usernames = [row for row in rows]
        return usernames
    
    def log_in(self,username,password,key):
        info=self.select_info_for_log_in()

        for db_username,db_password,db_key in info:
            if username == db_username and password == db_password and key==db_key:
                return True
        return False
    

    
        

        
    

        

       

        





