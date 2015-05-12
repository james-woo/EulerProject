m=1
n=2
for i in range(100):
	n=2
	for j in range(100):
    	a = n*n - m*m
    	b = 2*n*m
    	c = n*n + m*m
    	if a>0:
        	p = (a,b,c)
    	if(p[0] + p[1] + p[2] == 1000):
        	print p[0], p[1], p[2]
        	print p[0] * p[1] * p[2]
    	n+=1
	    m+=1