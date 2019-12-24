#lists in python


li = [1,2,3,4,5] # like array

li2 = ['a','b', 'c']

li3 = [1,2, 'a', True] #mixture of data types

#data structure - a way for us to organize information. 

amazon_cart = ['notebooks', 
'sunglasses',
'toys',
'grapes'
]
print(amazon_cart[0])
print(amazon_cart[1])

#List Slicing  - muttable

print(amazon_cart[0:2])
print(amazon_cart[0::2])
print("After changing the value of index 0 in amazon cart")
amazon_cart[0] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart #new cart points to the memory of amazon cart. so when you change the value in new cart the values changes in amazon cart also

new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)


#matrix, multi dimensioanl array

matrix = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]

print(matrix[0][1]  ) # [row][column]

#list methods

basket = [1,2,3,4,5]
basket.append(100)
#everything in python is a object

#append does not pro


new_list = basket
print(basket)
print(new_list) # result is non
