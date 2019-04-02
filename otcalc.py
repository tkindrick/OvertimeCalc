def computepay(h,r):
    if h>40.0:
        extra_time=(h-40.0)#how many extra hours worked
        
        thalf=extra_time*(1.5*r)#1.5 rate times extra hours worked
      
        base=40*r # hard coded in because 40 is base hours
        total=base+thalf# added the base plus the extra time
        return total
    elif h<=40.0:
        total2=h*r
        return total2
        
 

hrs = input("Enter Hours:")
rate = input("Enter Wage:")

our=float(hrs)
reight=float(rate)





p = computepay(our,reight)
print(p)