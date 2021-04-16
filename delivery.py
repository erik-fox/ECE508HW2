def delivery(who, distance):
	fo=open("hw2.txt","r")	
	N=int(fo.readline())
	if N == 0:
		print("empty document")
		return
	best=[]
	inquiry=[]
	dictionary=[]
	for i in range(N):
		din=fo.readline()
		din=din.rstrip('\n')
		din=din.split(",")
		d={'name': din[0],'mph': din[1], 'delay': din[2]}
		dictionary.append(d)
		if i == 0:
			best.append(din)
			if who==d['name']:
				inquiry.append(din)
		else:
			if (((float(distance)/float(best[0][1]))*float(60))+float(best[0][2]))>(((float(distance)/float(d['mph']))*float(60))+float(d['delay'])):
				best.pop(0)
				best.append(din)
			if who== d['name']:
				inquiry.append(din)
	print('{} would get the package there in {} minutes' .format(inquiry[0][0],str(((float(distance)/float(inquiry[0][1]))*float(60))+float(inquiry[0][2]))))
	if who!=best[0][0]:
		print('BEST CHOICE: {} would get the package there in {} minutes' .format(best[0][0],str(((float(distance)/float(best[0][1]))*float(60))+float(best[0][2]))))
