class Library:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def check_out(self):
        if self.availability == True:
            self.availability = False
            print(f"{self.title} of the author {self.author} has been checked out")
        else:
            print(f"{self.title} of the author {self.author} is not available")

    def display_status(self):
        if self.availability == True:
            print(f"{self.title} of the author {self.author} is available")
        else:
            print(f"{self.title} of the author {self.author} is not available")

    def return_book(self):
        if self.availability == False:
            self.availability = True
            print(f"{self.title} has been returned and is available again")
        else:
            print(f"{self.title} was not checked out")


books = [
    Library("1984", "George Orwell"),
    Library("to kill a Mocking Bird", "Harper Lee")
]

while True:
    print("\nHello! Welcome To our Library.")
    print("1 : Issue a book")
    print("2 : Return a book")
    print("3 : Check a book")
    print("4 : Quit")

    choice = int(input("Choose a option: "))

    if choice == 1:
        for i, bk in enumerate(books, start=1):
            print(f"{i} : {bk.title}")
        ch = int(input("Which Book you want: "))

        if ch == 1:
            books[0].check_out()
        elif ch == 2:
            books[1].check_out()
        else:
            print("Invalid Option")

    elif choice == 2:
        for i, bk in enumerate(books, start=1):
            print(f"{i} : {bk.title}")
        ch = int(input("Which Book you want to return: "))

        if ch == 1:
            books[0].return_book()
        elif ch == 2:
            books[1].return_book()
        else:
            print("Invalid Option")

    elif choice == 3:
        for bk in books:
            bk.display_status()

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid option")