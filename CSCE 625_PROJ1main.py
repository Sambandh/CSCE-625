import matplotlib.pyplot as plt
import numpy as np
filename = "heatmap_2.txt"

fp = open(filename)       #to open the file

prob_matrix = []
k=[]
l=[]
k1=[]
k2=[]
k3=[]
l1=[]
l2=[]
l3=[]
y=[]
traversedx=[]
traversedy=[]
traversedt=[]
traversedz=[]
traversedprob=0
for i in range(0,100):
    x_entry = []
    for j in range(0,100):
        x_entry.append(0)
    prob_matrix.append(x_entry)

for line in fp:
    entry = fp.readline()
    #print(entry)
    #(x, y, prob) = map(float,entry.split(" "))
    (x, y, prob) = entry.split(" ")
    prob.strip()
    prob_matrix[int(x)][int(y)] = float(prob)
    #print("x=%s y=%s prob=%s" % (str(x), str(y), str(prob)))

for i in range(0,100):          #storing the probabilities in a matrix form 
    for j in range(0,100):
        print("x=%s y=%s prob=%s" % (str(i), str(j), str(prob_matrix[i][j])))
t=0                             #creating a list traversing the first quarter of search space
i=0
for j in range(0,50):              
     if prob_matrix[i][j]>0:
        corner1=prob_matrix[i][j]
        k.append(i)
        l.append(j)
        break
     else:
        i=i+1
print ("the first corner point is",k[0],l[0])
        
i=99    #creating a list traversing the second quarter of search space
for j in range(0,50):
    if prob_matrix[i][j]>0:
        corner2=prob_matrix[i][j]
        k1.append(i)
        l1.append(j)
    else:
        i=i-1
print("the second corner point is",k1[0],l1[0])
        
j=0              #creating a list traversing the third quarter of search space
for i in range(50,100):
    if prob_matrix[i][j]>0:
        corner3=prob_matrix[i][j]
        k2.append(i)
        l2.append(j)
    else:
        j=j+1
print("the third corner point is",k2[0],l2[0])
            
j=99            #creating a list traversing the fourth quarter of search space
for i in range(50,100):
    if prob_matrix[i][j]>0:
        corner4=prob_matrix[i][j]
        k3.append(i)
        l3.append(j)
    else:
        j=j-1
print("the fourth corner point is",k3[0],l3[0])
print (k)
print (l)
print (k1)
print (l1)
print (k2)
print (l2)
print (k3)
print (l3)
p1=k1[0]
p2=l1[0]
p3=k1[1]
p4=l1[1]
p5=k1[len(k1)-1]
p6=l1[len(k1)-1]
p7=k1[len(k1)-2]
p8=l1[len(k1)-2] 
d1=0
prob1=0
for i in range(min(p1,p3,p5,p7),max(p1,p3,p5,p7)):    #traversing the first path taking the coordinates of the 1st,2nd, last and 2nd last points from the first list  
     for j in range(min(p2,p4,p6,p8),max(p2,p4,p6,p8)):
         d1=d1+1
         prob1=prob1+prob_matrix[i][j]
print("time taken for first path",d1)
print("Summation of PDE along path1",prob1)

p9=k2[0]
p10=l2[0]
p11=k2[1]
p12=l2[1]
p13=k2[len(k2)-1]
p14=l2[len(k2)-1]
p15=k2[len(k2)-2]
p16=l2[len(k2)-2] 
d2=0
prob2=0
for i in range(min(p9,p11,p13,p15),max(p9,p11,p13,p15)): #traversing the second path taking the coordinates of the 1st,2nd, last and 2nd last points from the first list  
     for j in range(min(p10,p12,p14,p16),max(p10,p12,p14,p16)):
         d2=d2+1
         prob2=prob2+prob_matrix[i][j]
print("time taken for second path",d2)
print("Summation of PDE along path2",prob2)
prob2=prob2+prob1

p17=k3[0]#traversing the third path taking the coordinates of the 1st,2nd,last and 2nd last points from the third list
p18=l3[0]
p19=k3[1]
p20=l3[1]
p21=k3[len(k3)-1]
p22=l3[len(k3)-1]
p23=k3[len(k3)-2]
p24=l3[len(k3)-2] 
d3=0
prob3=0
for i in range(min(p17,p19,p21,p23),max(p17,p19,p21,p23)):
     for j in range(min(p18,p20,p22,p24),max(p18,p20,p22,p24)):
         d3=d3+1
         prob3=prob3+prob_matrix[i][j]
print("time taken for third path",d3)
print("Summation of PDE along path3",prob3)
prob3=prob3+prob2


r=[]#traversing the fourth path taking the coordinates of the 1st,2nd, last and 2nd last points from the fourth list
s=[]
r1=[]
s1=[]
d4=0
for i in range(0,100):
    for j in range(0,100):
          if i not in k1 or k2 or k3 or k4 and j not in l1 or l2 or l3 or l4:
              if prob_matrix[i][j]!=0:
                            r.append(i)
                            s.append(j)
              else:
                            r1.append(i)
                            s1.append(j)
print (r)
print (s)

p25=r[0]
p26=s[0]
p27=r[1]
p28=s[1]
p29=r[len(r)-1]
p30=s[len(r)-1]
p31=r[len(r)-2]
p32=s[len(r)-2] 
d4=0
prob4=0
for i in range(min(p25,p27,p29,p31),max(p26,p28,p30,p32)):      
     for j in range(min(p26,p28,p30,p32),max(p26,p28,p30,p32)):
         d4=d4+1
         prob4=prob4+prob_matrix[i][j]
print("time taken for fourth path",d4)
print("Summation of PDE along path4",prob4)
prob4=prob4+prob3


p33=r1[0] #traversing the non-traversed nodes
p34=s1[0]
p35=r1[1]
p36=s1[1]
p37=r1[len(r1)-1]
p38=s1[len(r1)-1]
p39=r1[len(r1)-2]
p40=s1[len(r1)-2] 
d5=0
prob5=0
for i in range(min(p33,p35,p37,p39),max(p33,p35,p37,p39)):      
     for j in range(min(p34,p36,p38,p40),max(p34,p36,p38,p40)):
         d5=d5+1
         prob5=prob5+prob_matrix[i][j]
print("time taken for fifth path",d5)
print("Summation of PDE along path5",prob5)
prob5=prob5+prob4


prob=[]
prob=[prob1,prob2,prob3,prob4,prob5]
time=[]
time=[d1,d2,d3,d4,d5]

plt.plot(time,prob) #plotting the graph
plt.xlabel('Time')
plt.ylabel('CDP')
plt.show()



#for i in range(min(r),max(r)):
 #   for j in range(min(s),max(s)):
  #      d4=d4+1
        
#print (k)
#print (l)

#r=min(k)
#s=max(k)
#c=min(l)
#d=max(l)
#print (r,s,c,d)
#i=0
#j=0
#z1=0
#cdp=0
#for i in range(0,len(k)):               #loop for traversing non zero probability nodes
 #   for j in range(0,len(l)):
  #            traversedx.append(k)      #x coordinate of traversed node
   #           traversedy.append(l)      # y coordinate of traversed node
    #          z1=z1+1                   #calculates the no of times iteration runs
#print (traversedx)
#print (traversedy)
#print (z1)

#trx = map(int, traversedx)
#trx2= map(int, traversedy)


#for i in trx:
 #   for j in trx2:
  #         ty=i
   #        by=j
    #       cdp= cdp+ prob_matrix[ty][by]
#print (cdp)

#z2=0
#for i in range(0,100):
 #   for j in range(0,100):
  #      if i not in traversedx and j not in traversedy:
   #         traversedz.append(i)
    #        traversedt.append(j)
     #       z2=z2+1
#print(traversedz)
#print(traversedt)
#print(z2)
#z=z1+z2
#print("the total no of iterations taken for the algorithm to cover all nodes",z)
#pde1=pde2=pdex=0
t#ime1=time2=timex=0
#for i in range(0,99):
 #         for j in range(0,99):
  #            if prob_matrix[i][j]!=0:
   #               pde1=pde1+prob_matrix[i][j]
    #              time1=time1+1
     #         else:
      #            time2=time2+1
#pdex=pde1+pde2
#ro=[]
#ro=[pde1]
#r1=[]
#r1=[time1,time2]
#plt.plot(r1,ro)
#plt.xlabel('Time')
#plt.ylabel('CDP')
#plt.show()

                  
                
    

            
    
        

