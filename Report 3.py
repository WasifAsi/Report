# variable
amount=0
notes_needed=0
i=0 # variable for number in L

#input
amount=float(input("Ender the amount (under 1000 Rs) : "))

L=[500.00,100.00,50.00,20.00,10.00,5.00,2.00,1.00 ]

#Process and output
if (amount<1000):
    for i in L:
        if amount >= i: 
            notes_needed=int(amount//i)
            print(notes_needed,"Note(s) of",i)
            amount-=notes_needed*i
        
        else:
            print("0 Note(s) of",i)
else:
    print("You Have to input under 1000 R.s ")
