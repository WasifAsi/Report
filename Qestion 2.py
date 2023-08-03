#variable
out=""
count=""
text=""
new_text=""
no_alpha=0

#Input
text=str(input("Enter the text : "))

#process and output
list_1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text=text.lower()
list_2=[]


for char in list_1:
    num_count=new_text.count(char)
    if num_count > 0:
        list_2.append(str(char)+"="+str(num_count))
    else:
        continue

for out in list_2:
    print(out)

for count in new_text:
    if count not in list_1 and count != " ":
            no_alpha= no_alpha + 1
        
print("Non alphabetical count=",no_alpha)
