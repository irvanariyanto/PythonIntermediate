class MyClass:
    number = 0
    name = "noname"

def Main():
    me = MyClass()
    me.name = "Irvan"
    me.number = 1335

    friend = MyClass()
    friend.name = "Steve"
    friend.number = 3

    print "Name: "+ me.name +", Favorite Number: "+ str(me.number)
    print "Name: "+ friend.name +", Favorite Number: "+ str(friend.number)

if __name__ == "__main__":
    Main()
