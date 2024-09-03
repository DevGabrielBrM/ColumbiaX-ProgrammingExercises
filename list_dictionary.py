a = [i for i in range(5)]
print(a)

#%%
b = [i for i in range(20) if i%2==1]
print(b)

#%%
c = [(x,y) for x in ["a","b","c","d","e"] for y in "!@#$%"]
print(c)

#%%
d= []
for i in range(5):
    d.append(i)

print(d)
# %%
e = []
for i in range(20):
    if i%2==1:
        e.append(i)

print(e)

# %%
f = []
for x in "abcdef":
    for y in [1,2,3,4,5]:
        f.append((x,y))


print(f)

# %%

g = [(i,i**3,i**4) for i in range(10) if i%2==1]
print(g)
# %%

h = []

for i in range(10):
    if i%2==1:
        h.append((i,i**3,i**4))

print(h)
# %%

x = 2

x = x**2 if x%2==0 else "odd"
print(x)
#%%
y = [i if i%2==0 else "odd" for i in range(20)]
print(y)
# %%

import string

string.punctuation
s = "A man, a plan, a canal: Panama!"
letters = "".join([x for x in s if not x in string.punctuation and not x in string.whitespace]).lower()
print(letters)
if letters == letters[::-1]:
    print("It's a Palindrome")

# %%

frase = "abcd"
list_of_tuples = [(i,frase[i]) for i in range(len(frase))]
print(list_of_tuples)
print(dict(list_of_tuples))

# %%
dict = {i:frase[i] for i in range(len(frase))}
print(dict)
#%%
dict = {i:"abcde"[i] for i in range(len("abcde"))}
print(dict)
# %%
