def loadData(N):
	fo=open("hw2.txt","w")	
	fo.write(str(N))
	fo.write("\n")
	for i in range(int(N)):
		din = input("Enter service name, speed(mph), minutesDelayToPickUp: ")
		fo.write(din)
		fo.write("\n")	
	fo.close()
