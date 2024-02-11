f = [1,0,1,-2]

def funcx(x,array):
    n=len(array)-1
    result=0
    for i in range(n+1):
        result+=array[i]*x**n
        n-=1
    return result
def falsePosition(a,b,f,epsilon):
    x0=0
    while True:
        fa=funcx(a,f)
        fb=funcx(b,f)
        x1=((a*fb-b*fa)/(fb-fa))
        fx1=funcx(x1,f)
        if fa*fx1<0:
            b=x1
        else:
            a=x1
        error= abs((x1-x0)/x1)*100
        if error<=epsilon:
            return x1
        x0=x1

x=falsePosition(-2,2,f,0.005)

print(funcx(x,f))