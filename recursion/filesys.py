import os

def diskUse(path_):
	''' recursively computes the total file size a project directory '''

	total = os.path.getsize(path_) #get size of current folder
	print(path_)

	if os.path.isdir(path_):
		contents = os.listdir(path_) #list all contents in folder
		for item in contents:
			childpath = os.path.join(path_, item)
			total += diskUse(childpath)

	return total

print(diskUse('D:/LEARN/code/msft'), " bytes")
