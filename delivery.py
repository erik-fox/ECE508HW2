def delivery(who, distance):
	fo=open("hw2.txt","r")	
	N=int(fo.readline())
	array=[]
	for i in range(N):
		din=fo.readline()
		din=din.split(",")
		array.append(din)
	print(array)
