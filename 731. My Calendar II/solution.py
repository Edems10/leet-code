class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.doublebooked = []
    
    def book(self, start: int, end: int) -> bool:
        for db_start, db_end in self.doublebooked:
            if not (end <= db_start or start >= db_end):  
                return False

        for b_start, b_end in self.bookings:
            if not (end <= b_start or start >= b_end):  
                overlap_start = max(start, b_start)
                overlap_end = min(end, b_end)
                self.doublebooked.append([overlap_start, overlap_end])

        self.bookings.append([start, end])
        return True

def main():
    args1 = ["MyCalendarTwo","book","book","book","book","book","book"]
    
    args2 = [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
    obj = MyCalendarTwo()
    for arg1,arg2 in zip(args1,args2):
        if arg1 == 'book':
            print(obj.book(arg2[0],arg2[1]))
        


if __name__=="__main__":
    main()