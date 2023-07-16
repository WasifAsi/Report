amount=float(input("Ender the amount (under 1000 Rs)"))

L=[500.00,100.00,50.00,20.00,10.00,5.00,2.00,1.00 ]

for i in L:
    if amount >= i: 
        notes_needed=amount//i
        print(notes_needed,"Note(s) of",i)
        amount-=notes_needed*i

    else:
        print("0 Note(s) of",i)