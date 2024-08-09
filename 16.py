print('寻找质数')
f1=input('从2到:')
f2=int(f1)
f3=2
f5=0
f6=''
while f3<f2:
    f4=2
    while f4<=f3/2+1:
        if f4>f3/2:
            f5+=1
            if f5%4==0:
                f6+=f'{f3}\n'
            else:
                f6+=f'{f3}\t'
            break
        elif f3%f4==0: 
            break
        else:
            f4+=1 
    f3+=1 
print(f6)           
print(f'共{f5}个')