'''
Ordered
immutable
indexed
allow duplicates
heterogeneous - combination of different strings
'''

t = ()
print(t)

t = ((1,2,3,4,5,6))
print(t)

print(t[::-1])

a = ('int','float','complex','bool','set','dict','list','tuple')
print(a)
print(a[1])
print(a[-2])
print(a[2:5])
print(a[::2])
print(a[:2])
# t[start,end+1,step]
a1 = (1,2,3)
a2 = (4,5,6)
print(a1+a2)
a,b,c = a1
print(a)
print(b)
print(c)
print(a1.count(1))

tes = ['pen','pencil','eraser']
a = ''.join(tes.split(','))
print(a)

