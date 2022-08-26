import sys


print(type(sys.path))
print(sys.path)
print(sys.path[0])

sys.path[0] = '/Beetroot/Lesson 9'
print(sys.path)
print(sys.path[0])
