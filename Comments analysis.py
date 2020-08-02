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








print(data[0])
print('--------------------------------------------------------------------------------------------------')
print(data[1])
