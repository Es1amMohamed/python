while True:    
    number1 = input(" Please Enter Your Number Her ")
    try:
        number1 = int(number1)
        if number1 % 2 == 0:
            print(" It's Even Number")  
        else:
            print("It's Ood Number")
        op = input(" Do you Want to End The Game ? [ 'Y' , ' N '] ").capitalize().strip()
        if op == 'Y' :
            pass
        elif op == 'N':
            print(" Thank you ")
            break
        
    except ValueError:
        print("erroe")
        
        
    