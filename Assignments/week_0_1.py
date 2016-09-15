def p(x,coeff):
    sum=0
    for i,index in enumerate(coeff):
        sum+=index*(x**i)
    print sum
    
p(2,[2,3,4])
    