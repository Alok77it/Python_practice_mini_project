a = input("enter the number: ")
print(f"multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a) * i }")
except:
    print("invalid Input")