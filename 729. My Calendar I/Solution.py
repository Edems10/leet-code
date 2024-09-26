
class MyCalendar:
    def __init__(self):
        self.bookings =[]
    
    def book(self, start: int, end: int) -> bool:
        for existing_start, existing_end in self.bookings:
            if not (end <= existing_start or start >= existing_end):
                return False  # Overlap detected, reject the booking
        
        # No overlap found, add the new booking
        self.bookings.append([start, end])
        return True


def main():
    args1 = ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
    args2 = [[],[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
    obj = MyCalendar()
    for arg1,arg2 in zip(args1,args2):
        if arg1 == 'book':
            print(obj.book(arg2[0],arg2[1]))
        


if __name__=="__main__":
    main()