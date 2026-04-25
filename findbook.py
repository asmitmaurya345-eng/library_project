from database import l1
def fbook():
    b=input("Enter book name or book number of the book you want to find:")
    for x,y in l1.items():
        if x==b or y==b:
            print("We have the book u are looking for:",y)
            c=input("enter to continew")