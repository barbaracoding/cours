
import re

# version longue :

y = re.findall('[0-9]+', open('regex_sum_42.txt', 'r').read())
z = list()
for item in y:
    item = int(item)
    z.append(item)
print(sum(z))

# version courte :

y = re.findall('[0-9]+', open('regex_sum_263701.txt', 'r').read())
z = list()
for item in y:
    item = int(item)
    z.append(item)
print(sum(z))
