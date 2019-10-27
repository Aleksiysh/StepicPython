with open('dataset_24465_4.txt') as inp, open('out.txt','w') as out:
    a = list()
    for line in inp:
        a.append(line)
    for i in range(len(a)-1,-1,-1):
        out.write(a[i])
