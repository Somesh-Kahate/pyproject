l = 1
total = 0
name = ""
s = 0
t=0
d=0
j=0


def userName():
    global name
    name = input("Enter your name :")
    print("welcome",name)


def printNotes(m):
    a = [2000,500, 100, 50, 20, 10, 5, 2, 1]
    temp = 0
    i = 0
    temp = m
    for i in range(0, 9):
        if int(temp / a[i]) != 0:
            print(a[i], " notes is:", int(temp / a[i]))
        temp = temp % a[i]


def takeCash():
    cash = int(input("Enter your Cash :"))
    # print("\b/-")
    global total
    if cash > total:
        printNotes(cash - total)

    elif cash < total:
        total -= cash
        print("PLEASE PAY", total, "/- MORE")
        takeCash()


def cupsOrPlats(c):
    if c == 1 or c == 3 or c==4:
        return "plats:"
    if c == 2:
        return "cups:"


def printBill():
    i = 1
    print("ok..", name, "Your Bill :", total)
    print("sr.\t|\tItem\t|\tQty\t|\tPrice\t|\tTotal")
    print("------------------------------------------------------------------------------------")
    if s != 0:
        print(i, "\t|\tSamosa\t|\t", s, "\t|\t20\t|\t", s * 20)
        i += 1
    if t!=0:
        print(i, "\t|\tTea\t|\t",t,"\t|\t10\t|\t",t*10)
        i += 1
    if d!=0:
        print(i, "\t|\tDosa\t|\t",d,"\t|\t35\t|\t",d*35)
        i += 1
    if j!=0:
        print(i, "\t|\tDosa\t|\t",d,"\t|\t35\t|\t",d*20)
        i += 1
    print("------------------------------------------------------------------------------------")
    print("                                                         total :", total)
    takeCash()


def billing(quantity, rate):
    global total
    total = total + quantity * rate


def takingOrder(c, rate):
    pc = cupsOrPlats(c)
    quantity = int(input("How many " + pc))
    billing(quantity, rate)
    print("ok..Anything else...")
    return quantity


def order(c):
    if c == 1:
        print("you have ordered Samosa")
        global s
        s += takingOrder(c, 20)
    elif c == 2:
        print("you have ordered Tea")
        global t
        t +=takingOrder(c, 10)
    elif c == 3:
        print("you have ordered Dosa")
        global d
        d +=takingOrder(c, 35)
    elif c == 4:
        print("you have ordered Idli")
        global j
        j +=takingOrder(c, 20)
    elif c == 0:
        print("you select Exit")
        printBill()
        global l
        l = 0
    else:
        print("Wrong selection")


def menu():
    print('''::MENU::
            1.Samosa 20/-
            2.Tea    10/-
            3.Dosa   35/-
            4.Idli   20/-
            0.Exit
          ''')
    c = int(input("choice :"))
    # print("your",c)
    order(c)
def main():
    print("# Welcome to Somesh Hotel")
    userName()
    while l == 1:
        menu()
    print("Thank you  Visit Again")
main()