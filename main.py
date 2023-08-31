"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	# print(f'searching list {mylist} for key {key}')
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### 
	# print(mylist)
	# print(f'searching from {left} to {right}')
	# print(f'pivot: {mylist[len(mylist)//2]}')
	if len(mylist) == 1 and mylist[0] != key:
		return -1
	# if mylist[len(mylist)-1] == key:
	# 	# print(right)
	# 	return right
	if mylist[0] == key:
		return left
	else:
		if mylist[len(mylist)//2] > key:
			# print(f'{mylist[len(mylist)//2]} >= {key}!')
			return _binary_search(mylist[:len(mylist)//2],key,left,right-mylist.index(mylist[len(mylist)//2]))
		else:
			# print(f'{mylist[len(mylist)//2]} <= {key}!')
			return _binary_search(mylist[len(mylist)//2:],key,mylist.index(mylist[len(mylist)//2])+left,right)
	###


# print(binary_search([1,2,3,4,5], 5))
# print(binary_search([1,2,3,4,5], 1))
# binary_search([1,2,3,4,5], 5)
# print('*************')
# print(binary_search([1,2,3,4,5], 12))
# print('*************')
# print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13],11)) ##10
assert binary_search([1,2,3,4,5], 5) == 4
assert binary_search([1,2,3,4,5], 1) == 0
assert binary_search([1,2,3,4,5], 6) == -1



def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### 
	start = time.time()
	search_fn(mylist,key)
	end = time.time()
	return (end-start)*1000

	###
# t = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print("**********")
# print(time_search(binary_search,t,10))
# print(time_search(linear_search,t,10))


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	###
	ret = []
	for i in sizes:
		ret.append((i,time_search(linear_search,[j for j in range(0,int(i))],-1),time_search(binary_search,[j for j in range(0,int(i))],-1)))
	return ret
	###


print(compare_search())

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

