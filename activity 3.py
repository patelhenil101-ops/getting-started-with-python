a=7
b=2.54
c='8'
d=4.5
print('Before typecasting')

print("The datatype of {0} and {1}".format(a,type(a)))
print("The datatype of {0} and {1}". format(b,type(b)))
print("The datatype of {0} and {1}". format(c,type(c)))
print("The datatypr of {0} and {1}". format(d,type(d)))

print('After typecasting')
a=float(a)
print("The datatype of {0} and {1}".format(a,type(a)))
b=int(b)
print("The datatype of {0} and {1}". format(b,type(b)))
c=float(c)
print("The datatype of {0} and {1}". format(c,type(c)))
d=int(d)
print("The datatypr of {0} and {1}". format(d,type(d)))