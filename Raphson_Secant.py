f = [1,-2,0,4]
df = [3,-4,0]
def funcx(x,array):
    n=len(array)-1
    result=0
    for i in range(n+1):
        result+=array[i]*x**n
        n-=1
    return result

def raphson(f,df,guess,epsilon):
    x0=guess
    while True:
        fx=funcx(x0,f)
        fdx=funcx(x0,df)
        x1=x0-(fx/fdx)
        error= abs((x1-x0)/x1)*100
        if error<epsilon:
            return x1
        x0=x1

result=raphson(f, df, 5, 0.00001)
print(funcx(result,f))

def secant(f,xc,xp,epsilon):
    while True:
        fxc= funcx(xc,f)
        fxp=funcx(xp,f)
        xn=xc-((fxc*(xc-xp))/(fxc-fxp))
        error=abs((xn-xc)/xn)*100
        if error<epsilon:
            return xn
        xp=xc
        xc=xn

result2 = secant(f, 5, 7,  0.00001)

print(funcx(result2,f))