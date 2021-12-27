import numpy as np

pt = np.array([ [1, 0,-1,0], [0,-1,0,1], [0,1,0,-1], [0,0,1,1], [0,0,-1,1], [0,1,1,0], [0,-1,1,0] ])
print ("PT") 
print (pt)
p = pt.transpose()
print ("P") 
print (p)

x = np.array([ [3, 12,3,4], [3,4,3,4], [3,4,9,4], [3,4,3,1] ])
print ("input") 
print (x)

h = np.array([ [4,4,3,3,4,3,4], [4,4,3,3,4,3,4], [4,4,3,3,4,3,4], [4,4,3,3,4,3,4], [4,4,3,3,4,3,4], [4,4,3,3,4,3,4], [4,4,3,3,4,3,4] ])
print ("filter") 
print (h)

pre1 = pt.dot(x)
print (pre1)
preu = pre1.dot(p)
print ("preu")
print (preu)

mul = np.multiply(preu,h) 
print ("mul")
print (mul)
y = mul + mul + mul + mul + mul + mul + mul;
print ("alu")
print (y)

post = np.array([ [1,0,0,0,0,1,1], [0,0,1,1,1,0,0], [0,1,0,0,0,1,-1], [0,0,0,1,-1,0,0] ])
print (post)
pos = post.transpose()
print (pos)

outt = post.dot(y)
print("pos1")
print (outt)
out = outt.dot(pos)
print (out)
