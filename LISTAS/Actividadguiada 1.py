milistapor2=[]
milista=[1,2,3,4,5]
maximo=max(milista)
minimo=min(milista)
suma=sum(milista)

#for i in range(len(milista)):
    #calculo=milista[i]*2
    #milistapor2.append(calculo)

for i in milista:
    milistapor2.append(i*2)

#milistapro=[n*2 for i in milista]

print(milista)
print(f"maximo:{maximo}")
print(f"minimo:{minimo}")
print(f"suma total:{suma}")
print(milistapor2)
