f=[1,-2,0,4]

def funcx(x,array):
    n=len(array)-1
    result=0
    for i in range(n+1):
        result+=array[i]*x**n
        n-=1
    return result
#print(funcx(-32,f))

def bisection(xl,xu,f,epsilon):
    fxl=funcx(xl,f)
    fxu=funcx(xu,f)
    if fxl*fxu>=0:
        print("Invalid")
        return None
    while True:
        xm=(xl+xu)/2
        #fxl=funcx(xl,f)
        #fxu=funcx(xu,f)
        fxm=funcx(xm,f)
        error=abs((xm-xl)/xm)*100
        if fxl*fxm<0:
            xu=xm
        else:
            xl=xm
        if error<=epsilon or abs(xu-xl) <epsilon:
            return xm
print(bisection(55,-32,f,0.005))
#print(funcx(-1.129974365234375,f))