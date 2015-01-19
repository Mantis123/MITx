s = 'abcdefghijklmnopqrstuvwxyz'
x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
currentLongest=''
totalLongest=''
for i in s:
	if currentLongest=='':
		currentLongest +=i
		if len(currentLongest)>len(totalLongest):
			totalLongest=currentLongest
		continue
	if x.index(i)>=x.index(currentLongest[-1]):
		currentLongest+=i
		if len(currentLongest)>len(totalLongest):
			totalLongest=currentLongest
	else:
		if len(currentLongest)>len(totalLongest):
			totalLongest=currentLongest
		currentLongest=i

	
print 'Longest substring in alphabetical order is:'+totalLongest