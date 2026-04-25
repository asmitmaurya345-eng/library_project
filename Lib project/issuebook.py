from database import l1,l2
def ibook():
    b=input("Enter book name or book number of the book you want to issue:")
    for x,y in l1.items():
        if x==b or y==b:
            d=l1.pop(x)
            print("here is your book:",d)
            l2[x]=y
            break
    else:
        print("sorry we don't have that book")
    c=input("enter to continew")