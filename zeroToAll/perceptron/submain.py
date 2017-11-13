import element as el

result = el.AND(0,0)
print('AND  0,0:', result)
result = el.AND(0,1)
print('AND  0,1:', result)
result = el.AND(1,1)
print('AND  1,1:', result)

result = el.OR(0,0)
print('OR   0,0:', result)
result = el.OR(0,1)
print('OR   0,1:', result)
result = el.OR(1,1)
print('OR   1,1:', result)

result = el.NAND(0,0)
print('NAND 0,0:', result)
result = el.NAND(0,1)
print('NAND 0,1:', result)
result = el.NAND(1,1)
print('NAND 1,1:', result)
