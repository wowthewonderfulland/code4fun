
#%%
#list and tuple
t = (1,2)
t = (1,)

x = list()
x = ["a", "b", "c"]
for s in range(len(x)):
    print(s)
    print(x[s])
x[-1]
x.append("d")
x.insert(1, "e")
del x[0]
print(x)
x.pop() #last 
x.pop(1)
print(x)
x.count("b")
x.extend(["1","2"]) # return original list x, not x + y return a new list
print(x)
x.remove("e")
x.reverse()
x.sort()

#%%
# list like related operations
x = [1]
y = [2]
x * 2
z = x+y
# slicing
x = [1,2,3,4,5,6]
x[0:2] #[0,2)
x[:2]
x[:-1]
x[-1:]
x[-2:-1] #[-2:-1)
x[:] # copy
x[1:5:2]
x[5:1:-2]
7 in x

#%% 
#list comprehensions
list(range(1,11))
list(x * x for x in range(1,11))
list(x for x in range(1,11) if x % 2 == 0)
list(x+y for x in range(1,3) for y in range(7,15))
L = {"X": "A", "Y":"B"}
[k+"="+v for k,v in L.items()]
dict_comp = {x:chr(65+x) for x in range(1, 11)}
{x ** 3 for x in range(10) if x % 2 == 0}

#%%
# generator --> not comprehension, create one by one
sum(x*2 for x in range(2))
gen = (x*2 for x in range(2))
for x in gen:
    print(x)
#######################
mylist = ["a", "b", "c"]
gen = (elem + "1" for elem in mylist)
mylist.clear()
print(mylist)
for y in gen: print (y)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)

#%%
# iterable / iterator
#Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have __next__() method, which returns the next item of the object.
def iterable(obj): 
    try: 
        iter(obj) 
        return True
          
    except TypeError: 
        return False
  
# Driver Code      
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:             
    print(element, " is iterable : ", iterable(element)) 

#%%
#string related 
title = "Monty Python's Flying Circus"
title.find("python")
t = ["a", "b", "c"]
".".join(t)
m = title.split(" ")
title.lower()
title.replace("Monty", "Sucker")
"    strip is not trim    ".strip()
#translate
table = str.maketrans("cs", "kz")
"this is a an incredibel test".translate(table)
"this is a an incredibel test".replace("s", "z", -1) # not support multi replace

b'ABC'.decode("ascii")
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print('%.2f' % 3.1415926)
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

#%%
#dict
d = {1: "x", 2: "y", 3:"z"}
m = dict(n = "name", a = 12)
len(d)
d[1]
del d[2]
2 in d # HIGHLIGHT : key in dict
d[2] = "y"
d
m.clear()
m = d.copy() # shallow copy
m
{}.fromkeys([1,2])
m.get(4)
m.get(4,"N/A")
m.items()
m.items() is list # false for python 3
list(m.items()) is list # false for python 3
m.pop(1)
m.popitem()
d.setdefault(4,"N/A")
print(m)
print(d)
m[3] = "m"
m[5] = "t"
d.update(m)
print(d)
d.values() is list

#%%
#set 
l = [1,2,3,1]
s = set(l)
s.add(5)
s.remove(5)
s2 = set([2,3,8])
s | s2
s & s2

#%% 
#loop, condition
x = [1,2]
y = [1,2]
x is y
x == y
a, b, c = 1, 2, 3 
a, b, c = c, a, b # sequence unpacking
a = 1 if b == 2 else 3
assert a == 3
for i in x:
    print(i)
d = {1:"a",2:"b"}
for k in d:
    print(k)
for k, v in d.items():
    print("%d+%s"%(k,v))
y.append(5)
for t1,t2 in zip(x,y):
    print(t1)
    print(t2)
for idx, n in enumerate(x):
    print(n)
    print(idx)
sorted(x)
reversed(y)
for n in range(1,19):
    print(n)
else:
    print(-n)

#%%
# basic function and operations 
ord("a")
chr(66)
str(1)

#%%
# function basic 


#%%
#high-level functions
def f(x):
    return x*x
r = map(f, [1,2,3,4,5,6])
list(r)

from functools import reduce

#%%
# OO Programing


#%% 
# Handle error


#%%
#IO

#%% 
#multi threading


#%%
# inbuild module
