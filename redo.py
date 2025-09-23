class Resident:
    def __init__(self,name,room_no):
        self.name = name
        self.room_no = room_no

class Visitor:
    def __init__(self,name,visitor_id):
        self.name= name 
        self.visitor_id = visitor_id
        

class Hostel:
    def __init__(self,name):
        self.name = name
        self.visits=[]

    def record_visit     