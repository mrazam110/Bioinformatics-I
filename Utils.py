def removeDuplicates(Items):
    TempItems = []
    for item in Items:
        if item not in TempItems:
            TempItems.append(item)
    return TempItems

def printItems(Items):
    for i in Items:
        print(i, end = " ")