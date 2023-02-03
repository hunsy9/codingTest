import numpy as np;
import matplotlib.pylab as pl;

#np.array
a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
c=np.array([1,2,3,4,5] ,ndmin=2)
d=np.array([1,2,3],dtype=complex)
#np.arange
e = np.arange(5)
f = np.arange(3,9,2) #3부터 9까지 2씩증가 단,9는 제외
g = np.zeros(5)
h = np.ones(5)
#np.eye #identity matrix 생성
i=np.eye(3)
j=np.eye(3,4)
k=np.linspace(10,20,5) #10과 20사이에 등간격5개
l=e.reshape(5,1)
x=np.arange(-2,2.5,0.01)
# x = np.random.rand(3,3)
print(x)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(l[:,1])