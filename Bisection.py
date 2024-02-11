f=[1,-2,0,4]

def fx(x,f):
    result=0
    n=len(f)-1
    for i in range(len(f)):
        result+=f[n]*x**i
        n-=1
    return result
def bisection(xl,xu,f,epsilon):
    fxl=fx(xl,f)
    fxu=fx(xu,f)
    if fxl*fxu>=0:
        print("invalid")
        return None
    while True:
        xm=(xu+xl)/2
        fxm=fx(xm,f)
        error=abs((xm-xl)/xm)*100
        if fxl*fxm<0:
            xu=xm
        else:
            xl=xm
        if error<=epsilon or abs(xu-xl)<epsilon:
            return xm

print(bisection(55,-32,f,0.005))