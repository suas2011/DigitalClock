#Nested Loop Digital Clock
for i in range(0,24): #for hours
    for j in range(0,60): # for minutes
        for k in range(0,60): # for seconds
            for l in range(0,20000): #for milliseconds/nanoseconds
             print('{0:02}:{1:02}:{2:02}'.format(i,j,k),end='\r') 

#00:00:01
