data = []
count = 0
with open('reviews.txt', 'r') as f :
    for line in f :
        data.append(line)
        count = count + 1
        if count % 1000 == 0 :
            print(count)


print(len(data))
print(--------------------------------------------------------------------------------------------------)
print(data[0])
