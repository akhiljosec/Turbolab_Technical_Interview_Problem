W = int(input("Enter the Weight Capacity of Bag : "))
N = int(input("Enter the Total Items available in the Shop : "))
Weights = []
Prices = []

for i in range(N):
    Weights.append(int(input(f"Enter the weight of item {i+1} : ")))
    
for i in range(N):
    Prices.append(int(input(f"Enter the price of item {i+1} : ")))

##Case 1
##W = 14
##N = 5
##Weights = [12, 2, 1, 4, 1]
##Prices = [4, 2, 1, 10, 2]
##Ouput 17

##Case2
##W = 2
##N = 3
##Weights = [1, 1, 1]
##Prices = [2, 3, 5]
##Ouput 8

##Case3
##W = 3
##N = 4
##Weights = [2, 3, 1, 4]
##Prices = [10, 9, 3, 16]
##Ouput 14


price_per_kg = []

##Calculating the price per KG
for i in range(N):
    price_per_kg.append(Prices[i]/Weights[i])

##Creating a list with weight, price and price per kg of each item stored as tuple
items = []
for i in range(N):
    items.append((Weights[i], Prices[i], price_per_kg[i]))

##Sorting items, so that item with highest price per kg appears in the beginning
sorted_items = sorted(items, reverse=True, key=lambda x:x[2])

##print(items)
##print(sorted_items)

robbed_weight = 0
profit = 0
remaining_weight = W
i = 0

##Check whether robbers bag can carry another item and also there are still items in the shop
while remaining_weight > 0 and i < N:
    remaining_weight = W-robbed_weight

##Check if the remaining weight that Robbers Bag can carry is greater than the total weight of current item    
    if remaining_weight > sorted_items[i][0]:
        robbed_weight += sorted_items[i][0]
        profit += sorted_items[i][1]
##Else only a part of current item is taken which is equal to the remaining weight that robbers bag can carry
    else:
        robbed_weight += remaining_weight
        profit += remaining_weight*sorted_items[i][2]
    i += 1

print(profit)
print(f"Maximum Profit that can be obtained by Robber is {profit}")
