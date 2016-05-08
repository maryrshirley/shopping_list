shopping_list =["apple", "orange", "banana"]

# def add_list(a):
# 	a= a.lower()
# 	if a not in shopping_list:
# 		return shopping_list.extend([x])
# 	else:
# 		print "item already exists in the list"

# add_list("carrot")
# # print shopping_list
# print sorted(shopping_list)

# def sorting(s):
# 	s.sort()
# 	return s
# print sorting(shopping_list)

def remove_item(r):
	r= r.lower()
	if r in shopping_list:
		shopping_list.remove(r)
		print r, "has been removed from your list."
		print "Here is your new list", sorted(shopping_list)
	else:
		print r, "is not in your list."
remove_item("orange")
