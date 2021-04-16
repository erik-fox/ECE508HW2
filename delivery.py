def delivery(who, distance):
	fo=open("hw2.txt","r")	
	N=int(fo.readline())
	best=[]
	inquiry=[]
	for i in range(N):
		din=fo.readline()
		din=din.rstrip('\n')
		din=din.split(",")
		if i == 0:
			best.append(din)
			if who==din[0]:
				inquiry.append(din)
		else:
			if (((float(distance)/float(best[0][1]))*float(60))+float(best[0][2]))>(((float(distance)/float(din[1]))*float(60))+float(din[2])):
				best.pop(0)
				best.append(din)
			if who== din[0]:
				inquiry.append(din)
	print('{} would get the package there in {} minutes' .format(inquiry[0][0],str(((float(distance)/float(inquiry[0][1]))*float(60))+float(inquiry[0][2]))))
	if who!=best[0][0]:
		print('BEST CHOICE: {} would get the package there in {} minutes' .format(best[0][0],str(((float(distance)/float(best[0][1]))*float(60))+float(best[0][2]))))

