def linapprox(f,a,b,n,x):
    intervalLen=b-a
    intervalBtw=(intervalLen)/(n-1)
        
    x1=a
    while x1+intervalBtw<=x:
        x1+=intervalBtw
    x2=x1+intervalBtw
    
    y=f(x1)+(x-x1)*(f(x2)-f(x1))/(x2-x1)
    print "The linear interpolation is: x=",x,"y=",y
    

def f(x):
    return x**2
    
linapprox(f,0,100,5,52)