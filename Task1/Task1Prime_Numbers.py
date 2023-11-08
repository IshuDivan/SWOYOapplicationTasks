import math 
def prime_numbers(low, high):
    if(high<1):
        return []
    if(low<1):
        low=1
    length=high-low+1
    limit_of_step=int(math.sqrt(high))
    is_prime=[]
    for i in range(high+1):
        is_prime.append(True)
    for step in range(2,limit_of_step+1):
        x0=low//step
        x0=x0*step
        while (x0<=high):
            if(x0>step):
                is_prime[x0]=False
            x0=x0+step
    prime_list=[]
    for i in range(low,high+1):
        if is_prime[i]==True:
            prime_list.append(i)
    return prime_list      

