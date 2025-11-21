import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
print(type(a))
print(a.shape)
print(len(a))

b = np.array([1.3, 2, 3, 'Mathematics', 50])
print(b)
print(type(b))
print(len(b))
print(b[3])
print(b[3][-6:])

a[0][4] = 50
print(a)
a[0, 4] = 500
print(a)
print(a[0, 4])

print(np.zeros((3, 3)))
print(np.zeros((3, 3), dtype='int'))
print(np.ones((3, 3), dtype='int'))

print(np.full((3, 3), 15, dtype='float'))

print(np.random.rand(4, 4))
print(np.random.randint(1, 10, size=(3, 3)))
print(np.random.uniform(1, 10, size=(3, 3)))
