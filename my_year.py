year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    
    print('Leap Year')
    
elif year % 400 == 0:
    
    print('Leap year')
    
elif year <= 1582:
    
    print('Not within the Gregorian calendar period')
    
else:
    
    print('Common year')