def loadData(N):
	fo=open("list.txt","w")	
	fo.write(str(N))
	fo.write("\n")
	for i in range(int(N)):
		din = input("Enter service name, speed(mph), minutesDelayToPickUp: ")
		while din =='':			
			din = input("Invalid entry -  Enter service name, speed(mph), minutesDelayToPickUp: ")
		fo.write(din)
		fo.write("\n")	
	fo.close()
