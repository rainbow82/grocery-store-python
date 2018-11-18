prices={
    "banana": 4,
    "apple" : 2,
    "orange": 1.5,
    "pear": 3 
}

stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#print stock list
for key in prices:
    print key
    print "price %s" % prices[key]
    print "stock %s" % stock[key]

#total that could be made 
total = 0
for key in prices:
  print prices[key] * stock[key]
  temp_total = prices[key] * stock[key]
  total = total + temp_total
print total

#total grocery list and reduce inventory
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

shopping_list = ["banana", "orange", "apple"]