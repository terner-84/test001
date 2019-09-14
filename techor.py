print('one')
s = 'příliš žluťoučký kůn úpěl ďábelské ódy'
print(s[3:8])
print(chr(69))
print(ord('š'))

sumas = 0
my_dict = {}
for x in s:
    print(x + ' has code ' + str(ord(x)))
    sumas += ord(x)
    if x in my_dict:
        my_dict[x] += 1
    else:
        my_dict[x] = 1 

print('co {:.2f}'.format((sumas / len(s))))
print(my_dict)
print('x' in my_dict)


cont = []
with open('vlk.txt', mode='rb') as f:
    cont = f.readlines()

print("some changes")
print("another c2 change")

print(cont)