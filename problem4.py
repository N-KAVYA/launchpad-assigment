print("code for problem4")

dupli=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
print("the entered number:" +str(dupli))
def Remove(dupli):
    arr1=[ ]
    for num in dupli:
        if num not in arr1:
            arr1.append(num)
    return arr1

print(Remove(dupli))