from statistics import mode
print('for critical log')
print()
file=open(r"C:\Users\Krithika\Desktop\New folder\crit.log","r")
cnt=0
c=file.readlines()
l=[]
for i in c:
    cnt+=1
    h=i.strip().split(" ")
    l.append(h)
log_number=[]
date_time=[]
desc=[]
desc2=[]
for i in l:
    log_number.append(i[0])
    date_time.append(i[2])
    desc.append(''.join(str(elem) for elem in i[-5:-2]))
    desc2.append(i[0])
print('no.of logs:',len(l))
print()
for i in range (cnt):
    print(log_number[i],"\t",date_time[i],"\t",desc[i])
#to print frequently logged in user
print()
print('Frequent similar logs: ')
for i in l:
    if i[0]==mode(desc2):
        print(' '.join(i))
