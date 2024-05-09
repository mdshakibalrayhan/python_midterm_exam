class Star_cinema:
    __hall_list = []

    def entry_hall(self,ob):
        self.__hall_list.append(ob)

class Hall(Star_cinema):
    def __init__(self,row,col,hall_no):
        self.__row = row
        self.__col = col
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

        self.entry_hall(self)

    def getRow(self):
        return self.__row
    
    def getCol(self):
        return self.__col
        
    def entry_show(self,id,movie_name,time):

        self.id = id
        self.movie_name = movie_name
        self.time = time
        
        arr = [[0]*self.__col for _ in range(self.__row)]
        self._seats[id] = arr

        self.t = (self.id,self.movie_name,self.time)
        self._show_list.append(self.t)

    def book_seats(self,id,*args):
        for i in args:
            a,b = i

            if self._seats[id][a][b] == 0 :
                self._seats[id][a][b] = 1


    
    def view_show_running(self):
        for i in self._show_list:
            print('Movie name :',i[1],', Show_ID :',i[0],',Time :',i[2])

    def view_available_seats(self,id):
        for i in self._seats[id]:
            print(i)


h = Hall(5,6,111)
h.entry_show(1224,'jawan','22-3-2024 10:00 AM')
h.entry_show(45545,'hawa','12-4-2024  2:00 PM')
h.entry_show(7777,'spiderman','1-8-2024  8 PM')

legal_ids = []

for i in h._show_list:
    legal_ids.append(i[0])


while True:
    print('1. press 1 to see all  shows today.')
    print('2.press 2 to see available seats in a show.')
    print('3.press 3 to book ticket for a show.')
    print('4.press 4 to exit the system.')
    print('choose an action:')

    n = int(input())

    if n == 1:

        h.view_show_running()
        print('')

    elif n == 2:

        print('Enter show_ID to see availanble seats:')
        id = int(input())


        while id not in legal_ids:

            print('Wrong show_ID , enter correct one:')
            id = int(input())
            print('')


        h.view_available_seats(id)
        print('')


    elif n == 3:

        print('Enter show_ID:')
        id = int(input())

        while id not in legal_ids:
            print('Wrong show_ID, choose correct one:')
            id = int(input())

        print('enter how many tickets:')
        c = int(input())

        for i in range(c):
            
            print('enter row no: (must be in the range of 0 -',h.getRow() - 1,')')
            r = int(input())

            while r < 0 or r >= h.getRow():
                print('invalid row no! enter valid row no:')
                r = int(input())
                print('')

            print('enter column no:(must be in the range of 0-',h.getCol() - 1,')')
            cl = int(input())

            while cl < 0 or cl >= h.getCol():
                print('invalid column no! enter valid column no:')
                cl= int(input())
                print('')
            if(h._seats[id][r][cl] == 1):
                print('sorry ! this seat is already booked!')    
            h.book_seats(id,(r,cl))
            
        print('')

    elif n == 4:
        break
