from collections import OrderedDict
import os


directory = '/Users/sarah_chin_asus/Downloads/CACD2000_400/image'
wri = open('tester.txt', 'w')

dic = {}
lst = []

for folderName, subfolders, filenames in os.walk(directory):
	#folderName = 'CACD2000'
	#subfolders = string of folders in 'CACD'
	#filenames = string of the files in 'CACD'
	for filename in filenames:
		#same person --> #same key
		#new_filename = filename.rsplit('_', 1)[0].split('_', 1)
		#new2_filename = new_filename[1]
		#set --> list
		print(filename)
		lst.extend(filename.rsplit('_', 2)[0].split('_', 1))
if '.DS' in lst:
	lst.remove('.DS')
sett = set(lst[1::2])
print(sett)
lst2 = list(sett)
#print(sett)
for i in range(len(lst2)):
	(key, val) = lst2[i], ic
	dic[key] = val
print(dic)

for folderName, subfolders, filenames in os.walk(directory):
	for filename in filenames:
		for k, v in dic.items():
			if k in filename.rsplit('_', 2)[0].split('_', 1):
				wri.write(filename + ' ' + str(dic[k]))
				wri.write('\n')

wri.close()
