
a = [16,5,69,36,63,84,27,82,28,60,252,10,2223,2452,9625,22222,23,333,4523]
len1 = len(a)
for i in range(len1-1):
    for j in range(len1-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)



facl = []
def fact(a,b,st):
    facl.append(a)
    c = a+b
    if c < st:
        fact(b,c,st)
    else:
        facl.append(b)
    return facl


print(fact(0,1,50))


def fun(s):
    if len(s)<1:
        return s
    return fun(s[1:])+s[0]

print(fun('python'))


def fun(s):
    l = list(s)
    result = ""
    while len(l)>0:
        result+=l.pop()
    return result

print(fun('Python'))



def fun(s):
    result = ""
    max_index = len(s)-1
    for index,ele in enumerate(s):
        result+=s[max_index-index]
    return result

print(fun('Python'))



for i in range(1,20):
    for j in range(1,33):
        z = 100-i-j
        if z % 3 == 0 and 5*i+3*j+z/3 == 100:
            print(i,j,z)



a = [1,1,2,2,3,3,4,5,5,6]
dict = {}


def fun():
    l = []
    for key in a:
        dict[key] = dict.get(key,0)+1
    for i in dict:
        if dict[i] == 1:
            l.append(i)
    return l

print(fun())


uid = 10012650
s = 'uid=%s'%(uid)
s1 = 'uid={0}'.format(uid)
print(s,s1)
print(type(s),type(s1))

