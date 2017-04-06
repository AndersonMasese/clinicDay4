class BinarySearch(list):
	def __init__(self, list_len, level):
		self.tuple_index = range(0+level, list_len*level+1, level)
		list.__init__(self, self.tuple_index)
 		self.length = len(self.tuple_index)
 	
	def search(self, object_item):
        try:
            counter = 0
            item_last = len(self.tuple_index) - 1
            item_found = False
            item_first = 0

            if object_item not in self.tuple_index:
                return {'counter': counter, 'index' : -1}
            else:
                while item_first <= item_last and not item_found:
                    midpoint = (item_first + item_last) // 2
                    
                    if self.tuple_index[item_first] == object_item:
                        return {'counter': counter, 'index' : item_first}
                    elif self.tuple_index[item_last] == object_item:
                        return {'counter': counter, 'index' : item_last}
                    elif self.tuple_index[midpoint] == object_item:
                        counter += 1
                        item_found = True
                    else:
                        if object_item < self.tuple_index[midpoint]:
                            counter += 1
                            item_last = midpoint - 1
                        else:
                            counter += 1
                            item_first = midpoint + 1
                return {'counter': counter, 'index' : self.tuple_index.index(object_item)}
        except ValueError:
            print("not  working for some reason only known to you")
        finally:
            print("complete")