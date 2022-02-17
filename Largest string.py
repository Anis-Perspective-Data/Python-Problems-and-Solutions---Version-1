def largest(str):
	str=max(str.split(),key=len)
	return str
list='this is python'
print(largest(list))
