import Base

d1=Base.Deck()
d1.create()
d1.shuffle()

def inp():

    nm=input("Enter the name of Player:")
    nm=Base.Player()
    return(nm)

def draw_card(nm,n):

    for i in range(0,n):
        nm.draw(d1)


def check_val(curt,vari):
    if Base.Cards.re_val(curt)==Base.Cards.re_val(vari):
        return True
    else:
        return False

def check_sui(curt, vari):
    if Base.Cards.re_sui(curt) == Base.Cards.re_sui(vari):
            return True
    else:
            return False
def comp_throw():

    for car in comp.hand:
        if check_sui(curt,car)==True or check_val(curt,car)==True:
            curr.append(car)
            comp.hand.remove(car)
            return True
            break
def player_throw():

    num=int(input("Enter the Card Position or Enter 100 to draw:"))
    if num==100:

        return False

    elif check_sui(curt, p1.hand[num]) == True or check_val(curt, p1.hand[num]) == True:
        curr.append(p1.hand[num])
        p1.hand.remove(p1.hand[num])
        return True

    else:
        print("Wrong Card")
        return False


comp=Base.Player()
draw_card(comp,4)
comp.show()
p1=inp()
draw_card(p1,4)
print("Starting Game")

curr=[]
curr.append(d1.draw())   #Drawing First card
curt=curr.pop()
Base.Cards.show(curt)


while len(p1.hand)!=0 and len(comp.hand)!=0:
    print("Players Cards:")
    p1.show()

    if player_throw()==False:
        draw_card(p1,1)
    else:
        curt=curr.pop()

    print("Top of the Card:")
    Base.Cards.show(curt)

    print("Computer Cards:")
    comp.show()
    if comp_throw()!=True:
        draw_card(comp,1)
    else:
        curt=curr.pop()
    print("Top of the Card:")
    Base.Cards.show(curt)

if len(p1.hand)==0 :
    print("Player Won,Computer Lost")
else:
    print("Computer Won,Player Lost")




