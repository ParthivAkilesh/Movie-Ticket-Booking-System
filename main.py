import os
import pickle as pkl
from database import PVR, INOX, AdminDatabase
from cancel import Cancel
from book import Book
from account import Account

dbase = ""

if os.path.exists("db.pkl") and os.path.exists("adb.pkl"):   
    adb = pkl.load(open("adb.pkl", "rb"))
    # db = pkl.load(open("db.pkl", "rb"))
   
else: 
    # db = Database()
    adb = AdminDatabase()
    
def login():
    
    c = int(input("1. Login\n2. Register\n3. Admin Login\n4. Exit\n"))
    ac = Account(adb)
    if c == 1:
        ac.login()
        return True
    elif c == 2:
        ac.register()
        return True
    elif c == 3:
        ac.admin_login()
        return True
    else:
        print("INVALID CHOICE")
        return False
  
  
def booking(flag = "book"):
    
    global dbase
        
    for i in adb.movies:
            print(i, " - Shows available")
    mv = input("Enter the movie name: ")
    if mv in adb.movies:
        print("Shows available")
        place = int(input("Enter the Theatre: \n1. PVR\n2. INOX\n"))
        if place == 1:
            dbase = "pvr"
            if os.path.exists("pvr.pkl"):
                db = pkl.load(open("pvr.pkl", "rb"))
            else:
                db = PVR()
        elif place == 2:
            dbase = "inox"
            if os.path.exists("inox.pkl"):
                db = pkl.load(open("inox.pkl", "rb"))
            else:
                db = INOX()
        else:
            print("INVALID CHOICE")
        show = int(input("1. Morning Show (10:00 AM)\n2. Evening Show (4:00 PM)\n3. Night Show (8:00 PM)\n"))
        b = Book(mv, show, adb, db)
        adb.status[adb.current] = [db, b]
        if show == 1:
            b.book()
        elif show == 2:
            pass
        elif show == 3:
            pass
        else:
            print("INVALID CHOICE")  
 
def cancellation():
    
    adb.status[adb.current][1].cancel()
    
       
    
def main():
    
    print("Welcome to Book My Show")
    print("Login to book tickets")
    if login():
        ch = int(input("1. Book Tickets\n2. Cancel Tickets\n3. View Tickets\n4. Exit\n"))
        while ch in [1, 2, 3, 4]:
            if ch == 1:
                booking()
            elif ch == 2:
                cancellation()    
            elif ch == 3:   
                adb.status[adb.current][1].printTicket(adb.status[adb.current][0].booked[adb.current])
            else:
                adb.status[adb.current][1].save(dbase)
                print("Thank you for using Book My Show")
                break
            ch = int(input("1. Book Tickets\n2. Cancel Tickets\n3. View Tickets\n4. Exit\n"))
        
    
            
        
        
        
        
    
        
        
        
if __name__ == '__main__':
    main()