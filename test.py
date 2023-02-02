import librerialj as cplx
import math

passed = 0
failed = 0

##Suma de complejos

c1 = (3,-8)
c2 = (4,6)
resp = cplx.sumacplx((3,-8),(4,6))

if resp[0] == 7 and resp[1] == -2:
    passed += 1
else:
    failed += 1

c1 = (-3,1)
c2 = (2,-4)
resp = cplx.sumacplx((-3,1),(2,-4))

if resp[0] == -1 and resp[1] == -3:
    passed += 1
else:
    failed += 1

##Multiplicación de complejos

c1 = (3,-2)
c2 = (1,2)
resp = cplx.multcplx((3,-2),(1,2))
if resp[0] == 7 and resp[1] == 4:
    passed += 1
else:
    failed += 1

c1 = (-3,-1)
c2 = (1,-2)
resp = cplx.multcplx((-3,-1),(1,-2))
if resp[0] == -5 and resp[1] == 5:
    passed += 1
else:
    failed += 1

##Resta de complejos

c1 = (-2,1)
c2 = (1,2)
resp = cplx.rescplx((-2,1),(1,2))
if resp[0] == -3 and resp[1] == -1:
    passed += 1
else:
    failed += 1

c1 = (4,5)
c2 = (7,3)
resp = cplx.rescplx((4,5),(7,3))
if resp[0] == -3 and resp[1] == 2:
    passed += 1
else:
    failed += 1

##División de complejos

c1 = (0,3)
c2 = (-1,-1)
resp = cplx.divcplx((0,3),(-1,-1))
if resp[0] == -3/2 and resp[1] == -3/2:
    passed += 1
else:
    failed += 1

c1 = (4,2)
c2 = (-3,-3)
resp = cplx.divcplx((4,2),(-3,-3))
if resp[0] == -18/18 and resp[1] == 6/18:
    passed += 1
else:
    failed += 1

##Módulo

c = (4,-3)
resp = cplx.moducplx((4,-3))
if resp == 5:
    passed += 1
else:
    failed += 1

c = (3,7)
resp = cplx.moducplx((3,7))
if resp == 762/100:
    passed += 1
else:
    failed += 1

##Conjugado

c = (5,2)
resp = cplx.conjugado((5,2))
if resp[0] == 5 and resp[1] == -2:
    passed += 1
else:
    failed += 1

c = (2,-4)
resp = cplx.conjugado((2,-4))
if resp[0] == 2 and resp[1] == 4:
    passed += 1
else:
    failed += 1

##Polar a cartesiano

c = (3,math.pi)
resp = cplx.polycar((3,math.pi))
if resp[0] == -3 and resp[1] == 0:
    passed += 1
else:
    failed += 1

c = (2,math.pi/2)
resp = cplx.polycar((2,math.pi/2))
if resp[0] == 0 and resp[1] == 2:
    passed += 1
else:
    failed += 1

##Cartesiano a polar

c = (1,1)
resp = cplx.carypol((1,1))
if resp[0] == 141/100 and resp[1] == 45:
    passed += 1
else:
    failed += 1

c = (2,-3)
resp = cplx.carypol((2,-3))
if resp[0] == 361/100 and resp[1] == -5631/100:
    passed += 1
else:
    failed += 1

##Fase

c = (1,1)
resp = cplx.fasecplx((1,1))
if resp == 45:
    passed += 1
else:
    failed += 1

c = (2,3)
resp = cplx.fasecplx((2,3))
if resp == 5631/100:
    passed += 1
else:
    failed += 1

print("passed:", passed, "failed", failed)
