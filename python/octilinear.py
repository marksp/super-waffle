import math

ax = 0
ay = 0
bx = 4
by = 0
# cx =

print(abs(ay - by))
print(abs(ax - bx))

print(abs(ay - by)/abs(ax - bx))


# Octilinearity Criterion
octo = abs(math.sin(4*(math.atan(abs(ay - by)/abs(ax - bx)))))

print(octo)
#
print(abs(math.sin(4*(math.atan(1/2)))))

# Angular Resolution Criterion



# Edge Length Criterion
'''
e = edge length
l = preferred multiple
g = grid spacing
'''

edge = (e / (l * g)) - 1

'''

diagram(G) = (stations(V), edges(E), labels(L)
snapStations(V)

'''