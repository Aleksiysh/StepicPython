import os
import os.path

dirictories  = set()
fout = open('out6.txt','w')
for curent_dir,dirs,files in os.walk('./main'):
    for file in files:
        if file[-3:] =='.py':
            dirictories.add(curent_dir[2:])
            break
for dir in sorted(dirictories):
    print(dir,file = fout)



fout.close()

pass