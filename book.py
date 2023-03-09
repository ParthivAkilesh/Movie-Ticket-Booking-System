import pickle as pkl

class Book:
    
    
    def __init__(self, mv, show, adb, db):
        self.mv = mv
        self.show = show
        self.adb = adb
        self.db = db
        
        if show == 1:
            self.showKey = "ticketsMS"
        elif show == 2:
            self.showKey = "ticketsES"
        elif show == 3:
            self.showKey = "ticketsNS"
        
    def printTicket(self, bookedData):  
        
        showsName = ["Morning Show (10:00 AM)", "Evening Show (4:00 PM)", "Night Show (8:00 PM)"]
        print(bookedData)
        print(f"{bookedData[0]}".center(30))
        print(f"{showsName[bookedData[1]-1]}".center(30))
        print(f"Seats Booked: {bookedData[2]}".center(30))
        
    def book(self):
        seats = int(input("Enter the number of seats: "))
        print("Screen View".center(25))
        for i in self.db.movies[self.mv][self.showKey]:
            print(i, *self.db.movies[self.mv][self.showKey][i])
        
        print("Enter the seat number you want to book")
        print("FORMAT EXAMPLE : 'A5', 'D3' ")   
        print(" '#' - Denotes Booked Seat")
        
        for i in range(seats):
            
            sno = input("Enter the seat number: ")
            if sno[0] in self.db.movies[self.mv][self.showKey]:
                data = self.db.movies[self.mv][self.showKey][sno[0]]
                if data[int(sno[1])] == "#":
                    print("Seat already booked")
                    print("Choose another seat")
                    continue
                else:
                    data[int(sno[1])] == "#"
                    
                if self.adb.current not in self.db.booked:
                    self.db.booked[self.adb.current] = [self.mv, self.show, [sno]]
                else:
                    self.db.booked[self.adb.current][2].append(sno)
        
        print("Seats Booked".center(30))
        self.printTicket(self.db.booked[self.adb.current])
        # pkl.dump(self.db, open("pvr.pkl", "wb"))
        # self.adb.current = None
        return
    
    
    def cancel(self):
        
        cdata = self.db.booked[self.adb.current]
        for i in cdata[2]:
            self.db.movies[self.mv][self.showKey][i[0]][int(i[1])] = i[1]
            
        print("Seats Cancelled".center(30))
            
        return
            
        
    def save(self, dbase):
        
        pkl.dump(self.db, open(f"{dbase}.pkl", "wb"))  