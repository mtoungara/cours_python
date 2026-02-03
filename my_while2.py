c0 = int(input("Enter a number to run Collatz Sequence: "))

if c0 > 1:
    steps = 0
while c0 != 1:
    if c0 %2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3* c0 +1
    print(c0)
    steps += 1
print("steps =",steps)

#else:  
        
print("Please enter a number larger than 1.")