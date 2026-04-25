from database import l1,l2
def rbook():
    b=input("Enter number of the book you want return:")
    c=input("Enter name of the book you want return:")
    if b in l2:
        l1[b]=c
        d=l1.pop(b)
        print("thank you for returning our book")
    else:
        print("Sorry sir but u have not issued this book from us")
    c=input("enter to continew")