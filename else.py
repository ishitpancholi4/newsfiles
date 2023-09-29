sub1 = int(input("Enter the mark= "))
sub2 = int(input("Enter the mark= "))
sub3 = int(input("Enter the mark= "))

Total = sub1+sub2+sub3
percentage = Total/3
print(percentage)

if percentage >= 90:
    print("Distinction")
elif percentage >= 60:
    print("first class")
elif percentage >= 40:
    print("second class")
else:
    print("fail")




