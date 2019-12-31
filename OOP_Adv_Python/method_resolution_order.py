# MRO : Method Resolution Order is a order that python follows when there are multiple inheritance
# the rule to follow, a method in a heirarchy of classes
# the algorithm for MRO is Depth First Search


class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C): #inherits from B, C
    pass


print(D.num)

#to see how python goes thorugh the heirarchy use MRO()

print(D.mro()) # D -> B -> C -> A -> Object 

#the diagram of the multiple inheritance


#       A
#    /    \
#   /       \
#   B        C
#   \       /
#     \   /
#       D


#another example


class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__)