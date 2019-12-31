# MRO : Method Resolution Order is a order that python follows when there are multiple inheritance


class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C): #inherits from B, C
    pass



#the diagram of the multiple inheritance


#       A
#    /    \
#   /       \
#   B        C
#   \       /
#     \   /
        D