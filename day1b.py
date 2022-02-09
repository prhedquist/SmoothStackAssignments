x = 50 + 50
y = 100 - 10
print(x)
print(y)
print("Hello World : 10")
s = "hello world"
print("\n")

p = 800000      #this is the original price of the house
op=p            #this is a copy of the original price. will be used to determine total cost of house, set to p
r = 0.06        #this is the interest rate percentage
o_r = r*100     #this is the interest rate, just a whole number (for readability purposes at the end)
m = 10000       #this is the original monthly payment, will stay this number till the last month since the last month will be less
om = m          #this is the original monthly payment, set to m
count = 0       #a counter to count the months it will take

while p > 0:                    #this is the while loop. once the payment price (p) reaches 0, it will terminate
    ir = p * (r/12)             #this is the interest rate
    p = (p + ir) - m            #this is the new payment price after the monthly payment (m) has been paid (subtracted from p)
    if p < m:                   #this triggers when p is less than m
        ir = p * (r/12)         #interest payment is calculated the same as before
        m = int(p + ir)         #m is casted to an integer to round up
        p = m - m               #p is set to 0 (if our calculations were correct)
        tcount = count + 2      #count is set to total count, then the loop exits (we use a +2 here)

    count = count + 1           #count is incremented by 1
t = count*om + m                #total cost is the count*original monthly payment price, + the final months payment since it is less than om
mp = t/tcount                   #the monthly payment is set by dividing total cost by total months


print("input: ")
print(str(op) + " " +  str(int(o_r)) + " " + str(tcount))
print("output: ")
print(int(mp))