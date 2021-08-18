print ("Enter your name : \n(1 for Harry)\n(2 for Hammad)\n(3 for Rohan)")
name = int(input())
print ("What you want to do : \n (1 for Retrive ) \n (2 for Log)")
want = int(input())
def getdate():
        import datetime
        return datetime.datetime.now()
def log(want):
        if want == 2:
                print("What you want see \n(1 for Diet)\n(2 for Exercise)")
        need = int(input())
        if need == 1 and name == 1:
                m = open("harry_diet.txt")
                print(m.read())
                m.close()
        if need == 2 and name == 1:
                n = open("harry_exrcice.txt")
                print(n.read())
                n.close()
        if need == 1 and name == 2:
                o = open("hammad_diet.txt")
                print(o.read())
                o.close()
        if need == 2 and name == 2:
                p = open("hammad_exrcice.txt")
                print(p.read())
                p.close()
        if need == 1 and name == 3:
                q = open("rohan_diet.txt")
                print(q.read())
                q.close()
        if need == 2 and name == 3:
                r = open("rohan_exrcice.txt")
                print(r.read())
                r.close()

def retrive(want):
        if want == 1:
                print('What wou want to add \n(1 for Diet)\n(2 for Exercise)')
        choose = int(input())
        if choose == 1 and name == 1:
                print("Type what you eat :")
                food = input()
                f = open("harry_diet.txt", "a")
                f.write(food)
                f.close()
        if choose == 2 and name == 1:
                print("Type what you do :")
                exercise = input()
                f = open("harry_exrcice.txt", "a")
                f.write(exercise)
                f.close()
        if choose == 1 and name == 2:
                print("Type what you eat :")
                food = input()
                f = open("hammad_diet.txt", "a")
                f.write(food)
                f.close()
        if choose == 2 and name == 2:
                print("Type what you do :")
                exercise = input()
                f = open("hammad_exrcice.txt", "a")
                f.write(exercise)
                f.close()
        if choose == 1 and name == 3:
                print("Type what you eat :")
                food = input()
                f = open("rohan_diet.txt", "a")
                f.write(food)
                f.close()
        if choose == 2 and name == 3:
                print("Type what you do :")
                exercise = input()
                f = open("rohan_exrcice.txt", "a")
                f.write(exercise)
                f.close()
if want==1:
        name2 = retrive(want)
        name4 = getdate()
elif want == 2:
        name3 = log(want)
