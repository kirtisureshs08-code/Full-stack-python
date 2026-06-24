class Lib:
    def __init__(self,id,title,author,copies):
        self.id=id
        self.title=title
        self.author=author
        self.copies=copies
    def issue_book(self):
        if self.copies>0:
            self.copies-=1
            print("book issued")
        else:
            print("book not available")
    def return_book(self):
        self.copies+=1
        print("book returned")
    def display_d(self):
        print(self.id)
        print(self.title)
        print(self.author)
        print(self.copies)
l=Lib(12,"Jivan","ABC",2)
l.issue_book()
l.return_book()
l.display_d()