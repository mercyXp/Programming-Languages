first_num = int(input("Enter first number: "))
second_num = int(input("Enter second numnber: "))
last_num = int(input("Enter last number: "))

if(first_num > second_num and first_num > last_num):
    print(first_num," is the largest")
elif(second_num > first_num and second_num > last_num):
    print(second_num,"is the largest")
else:
    print(last_num,"is the largest")