# Q1
str = "a:b:c:d"
p =str.split(':')
print(type(p))
t = "#".join(p)
print(t)
# Q2
try:
    a = {'A':90, 'B':80}
    a['C']
except:
    print(70)

a = [1, 2, 3]
print(id(a))
a = a + [4,5]
print(id(a))

a = [1, 2, 3]
print(id(a))
a.extend([4,5])
print(id(a))
sum = 0
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
for i in A:
    sum+=i

print(sum)
# sum = 0
# a = input("숫자를 , 를 포함해 나열해주세요:")
# p =a.split(',')
# for i in p:
#     sum += int(i)
# print(sum)

# a = input("구구단을 출력할 숫자를 입력하세요(2~9)")
# for i in range(1,10):
#     print(i*int(a),end=" ")

a = int(input("숫자입력: "))

for i in range(a+1):
    print(i)