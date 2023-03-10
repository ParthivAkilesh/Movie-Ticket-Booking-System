class AdminDatabase:
    
    
    def __init__(self):
        
        self.users = {"asd": "asd"}
        
        self.admin = {"admin": "admin"}
        
        self.current = None
        
        self.status = {}
        
        self.movies = ["movie1", "movie2"]
      
      
      
class PVR:
    
    def __init__(self):
        
        self.movies = {
            
            "movie1" : {
                "ticketsMS" :{
                        "A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "B": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "C": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "D": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "E": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       },
        
                "ticketsES" : {
                        "A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "B": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "C": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "D": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "E": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       },
        
                "ticketsNS" : {
                        "A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "B": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "C": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "D": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "E": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "F": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "G": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       }
            }
        }
        
        self.booked = {}
        
        self.cancelled = {}
        
        
class INOX:
    
    def __init__(self):
        
        self.movies = {
            
            "movie1" : {
                "ticketsMS" :{
                        "A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "B": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "C": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "D": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "E": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       },
        
                "ticketsES" : {
                        "A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "B": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "C": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "D": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "E": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       },
        
                "ticketsNS" : {
                        "A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "B": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "C": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "D": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "E": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "F": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        "G": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       }
            }
        }
        
        self.booked = {}
        
        self.cancelled = {}

