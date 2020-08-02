data = []
count = 0
with open('reviews.txt', 'r') as f :
    for line in f :
        data.append(line)
        count = count + 1
        if count % 10000 == 0 :
            print(count)
print('The file total number of line:', count)

sum = 0
for d in data:
    sum = sum + len(d)
    avg = sum / len(data)
print('The average length is', avg)

new = []
for d in data :
    if len(d) < 100 :
        new.append(d)
print('There are ', len(new), 'data less then 100')
print(new[0])
print(new[1])

good = []
for d in data :
    if 'good' in d :
        good.append(d)
print('There are ', len(good), ' good in the comments')
print(good[0])




#print(data[0])
#print('--------------------------------------------------------------------------------------------------')
#print(data[1])
