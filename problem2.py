print("code for problem1]2")

arr1=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
print ("entered list : " + str(arr1)) 
arr_res= [] 
for i in range(0, len(arr1)) : 
    if arr1[i] == 2 : 
        arr_res.append(i) 
          
print ("indices list : " + str(arr_res))