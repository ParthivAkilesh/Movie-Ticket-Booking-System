class Account:
    
    def __init__(self,adb):
        self.adb = adb
        
        
    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name in self.adb.users:
            if self.adb.users[name] == password:
                print("Login Successful")
                print("Welcome", name)
                self.adb.current = name
            else:
                print("Incorrect Password")
        else:
            print("User not found")
            
            print("Try again")
            self.login()
        
        
    def register(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.adb.users[name] = password
        print("Registration Successful")
        print("You can now login")
        self.login()
        
    def admin_login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name in self.adb.admin:
            if self.adb.users[name] == password:
                print("Login Successful")
                print("Welcome", name)
            else:
                print("Incorrect Password")
        else:
            print("User not found")
            
            print("Try again")
            self.admin_login()