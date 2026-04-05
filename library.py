class lib():
    no_book=0
    books=[]

    def add_book(self):
        new_book=input("enter the book that ypu wanted to add")
        self.books.append(new_book)
        print("book added")


    def tot_books(self):
        book_count=0
        for books in self.books:
            book_count+=1
        print("Total number of books: ",book_count)

    def bor(self):
        borrowed=input("enter the book that you wanted to borrow")
        if borrowed in self.books:
            print(borrowed," has been borrowed")
            self.books.remove(borrowed)
        else:
            print("book not available")
while True:
    op=int(input("What do you want to do? \n 1) add books \n 2)check number of books \n 3) borrow books\n"))
    pbj=lib()
    if op==1:
        pbj.add_book()
    elif op==2:
        pbj.tot_books()
    elif op==3:
        pbj.bor()
    else:
        print("invalid input")
    choice=int(input("do you want to do some other operation? 1(yes) 0 (no)"))
    if choice==1:
        continue
    else:
        break
