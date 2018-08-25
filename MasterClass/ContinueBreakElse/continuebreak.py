# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break
#
#     print("Buy " + item)


# Modify this loop to stop when i is exactly divisible by 11
for i in range(0, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        if i != 0:
            print(i)