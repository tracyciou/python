# 讓使用者輸入5個數字， 1. 算總和 2. 哪個數字最大
# 使用List列表處理

n1 = input("enter a number:")
n2 = input("enter a number:")
n3 = input("enter a number:")
n4 = input("enter a number:")
n5 = input("enter a number:")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)

data = [n1, n2, n3, n4, n5]

sum = sum(data)
print(sum)

max = max(data)
print(max)