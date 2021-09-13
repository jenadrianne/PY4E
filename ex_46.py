#do the computation of pay in a function called computepay() and use the function to do the computation. 
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function.

def computepay(h,r):
    if h < 0 or r < 0:
        return None
    elif h > 40:
        return (40*r+(h-40)*1.5*r)
    else:
        return (h*r)
    

hrs = input("Enter Hours:")
hour = float(hrs)
r = input("please input your rate:")
rate = float(r)
p = computepay(hour,rate)
print("Pay " + str(p))
