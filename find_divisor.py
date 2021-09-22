i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        count += 1
        print(i)
       
    
    i += 1

print(f'120의 약수는 총 {count}개 입니다.')
print(f'120 has total {count} divisors.')
