shopping_list= ["apples", "water", "yogurt", "banana"]

def add(items):
	items= items.lower()
	if items not in shopping_list:
		return shopping_list.append(items)
	else:
		print "Item already in the list"

def add_multiple(items):
	if items not in shopping_list:
		return shopping_list.extend(items)
	else:
		print "Item already in the list"

def sorting(items):
	items.sort()
	return items

add_multiple(["carrots", "cake", "ice cream"])
print shopping_list

sorting(shopping_list)
print shopping_list

def remove(items):
	items= items.lower()
	if items not in shopping_list:
		print "Item not in list"
	else:
		return shopping_list.remove(items)

remove("water")

print shopping_list
