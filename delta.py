a= float(input("add avl:"))
b= float(input("add dovom:"))
c= float(input("add sevom:"))
def javab(a,b,c):
    delta= (b**2)-(4*a*c)
    return delta
def Rishe(a,b,c):
    if javab(a,b,c) > 0:
        print ("2 ta rishe dard")
        return (((-b)+ (javab(a,b,c)**0.5)) / (2*a)) , (((-b)- (javab(a,b,c)**0.5)) / (2*a))
    elif javab(a,b,c) == 0 :
        print("yek rishe dard")
        return ((-b)/ (2*a))
    elif javab(a,b,c) < 0 :
        print("rishe nadard")
print(Rishe(a,b,c))