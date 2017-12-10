#A function to find acceleration.

v= 25
u=0
t=10

def acc(v, u, t):
    a=(v-u)/t
    print("Value of acceleration is {}m/s".format(a))

acc(v,u,t)