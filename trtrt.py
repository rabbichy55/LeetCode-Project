a = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
v = {"IV" : 4,
     "IX" : 9,
     "XL" : 40,
     "XC" : 90,
     "CD" :400,
     "CM": 900
     }
s = 0
loop = 0
data = input()
for i in range(len(data)):
     if data[i:i+2] in v:
         s += v[data[i:i+2]]
         s -= a[data[i+1]]
     else:
         ind = data[i]
         s += a[ind]

print(s)

