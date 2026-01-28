class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1   

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


def main():
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    Obj2 = BookStore("Clean Code", "Robert C. Martin")
    Obj2.Display()

    Obj3 = BookStore("Python Crash Course", "Eric Matthes")
    Obj3.Display()


if __name__ == "__main__":
    main()
