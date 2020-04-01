# list1 = [1, 2, 3, 4, 2, 1, 1, 4, 5] 
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# list1=(list1[1:8:2])
# listTwo=listTwo[1:8:2]

# print(list1)
# print(listTwo)
# for x,y in zip(list1,listTwo):
#     if (x %2==0 and y %2==0):
#         print()



# #  Given a list slice it into a 3 equal chunks and rever each list
# # For Example: sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# # Expected Outcome:

# # Original list  [11, 45, 8, 23, 14, 12, 78, 45, 89]
# # Chunk  1 [11, 45, 8]
# # After reversing it  [8, 45, 11]
# # Chunk  2 [23, 14, 12]
# # After reversing it  [12, 14, 23]
# # Chunk  3 [78, 45, 89]
# # After reversing it  [89, 45, 78]
# sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# sampleList1=sampleList[0:3:1]
# print(sampleList1)
# sampleList1=sampleList1[::-1]
# print(sampleList1)
# z=sampleList[3:6:1]
# print(z)
# z=z[::-1]
# print(z)


# ############################################ Exercise Question 2: Concatenate two lists index-wise   #########################
# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]

# for x,y in zip(list1,list2):
#     print(x+y)

# firstSet  = {2,3, 42, 65, 57, 78, 8,3, 29}
# secondSet = {57, 83, 29, 67, 73, 4,3, 48}

# print("First Set ", firstSet)
# print("Second Set ", secondSet)

# intersection = firstSet.intersection(secondSet)
# print("Intersection is ", intersection)
# for item in intersection:
#   firstSet.remove(item)

# print("First Set after removing common element ", firstSet)



z=int(input("")) 
if z %2==1:
  print("Weird")
if  z in range(3,5):
  if z % 2==0:
    print ("not weird")
if z in range (6,20):
   if z % 2==0:
    print ("weird")
if z>20 and z%2==0:
   print ("not weird")

