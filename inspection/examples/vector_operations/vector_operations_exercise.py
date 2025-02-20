def vectorPrint(vector, msg, sep=' '):
    print(f'{msg}: {vector}')

def vectorAdd(v1, v2):
  result = []
  if len(v1) != len(v2):
    return result
  for i in range(len(v1)):
    result.append(v1[i] + v2[i])
  return result

def vectorSub(v1, v2):
    result = list()
    tmp = list()
    if len(v1) != len(v2):
        return result
    for i in range(len(v1)):
        result.append(v1[i] - v2[i])
    return result

def vectorInverse(vector):
    result = list()
    size = len(vector)
    for i in range(size):
        result.append(vector[size-1-i])
    return result

def vectorScalarProduct(v1, v2):
    result = 0 
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


# Verification

v1 = [1,2,3,4,5,6,7,8,9]
v2 = [10,20,30,40,50,60,70,80,90]

vectorPrint(v1, 'V1')

v_add = vectorAdd(v1, v2)
vectorPrint(v_add, 'V1+V2')
assert [1+10, 2+20, 3+30, 4+40, 5+50, 6+60, 7+70, 8+80, 9+90] == v_add

v_sub = vectorSub(v2, v1)
vectorPrint(v_sub, 'V2-V1')
assert [10-1, 20-2, 30-3, 40-4, 50-5, 60-6, 70-7, 80-8, 90-9] == v_sub

v_inv = vectorInverse(v1)
vectorPrint(v_inv, 'inv(V1)')
assert [9, 8, 7, 6, 5, 4, 3, 2, 1] == v_inv

v_scalar = vectorScalarProduct(v1, v2)
vectorPrint(v_scalar, 'V1 * V2')
assert 1*10 + 2*20 + 3*30 + 4*40 + 5*50 + 6*60 + 7*70 + 8*80 + 9*90 == v_scalar
