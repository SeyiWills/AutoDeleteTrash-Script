# Import required module

import winshell

#covert the objects returned by recycle_bin()
#into list and stored in recycleBin_items

recycleBin_items = list(winshell.recycle_bin())

#print no. of elements in recycle bin 

print(len(recycleBin_items),
      "Items are present in recycle bin")

#print name of all items with their recycled date

for item in recycleBin_items:
    print(item)