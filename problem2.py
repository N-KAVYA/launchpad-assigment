print("code for problem2")

arr1=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("the entered number: " +str(arr1))
def ran(arr1):
    array1=[]
    for i in arr1 : 
        if  i < 5: 
            array1.append(i)
    return array1
print(ran(arr1))