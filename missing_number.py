def find_missing(a, b):
	list1 = set(a)
	list2 = set(b)
	odd_number= list1 ^ list2
	missing_id = list(odd_number)
	if missing_id == []:
		return 0
	for result in missing_id:
		return result
