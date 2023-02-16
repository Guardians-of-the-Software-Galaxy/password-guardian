

fp = open('data.txt', 'r')
list = []    # use heap or list?
for i in fp:
    list.append(i)
    print(list)
fp.close()
