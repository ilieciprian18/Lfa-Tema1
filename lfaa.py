def evalueaza(cuv,states):
    nou = states
    replaceold = set()
    while replaceold!=nou:
        replaceold=nou
        for x in replaceold:
            if 'la' in l[x]:
                nou = nou.union(l[x]['la'])
    if cuv=="":
        return fin.intersection(nou)!=set()
    else:
        aux = set()
        for x in nou:
            if cuv[0] in l[x]:
                aux=aux.union(l[x][cuv[0]])
        return evalueaza(cuv[1:],aux)
def afis(cuvant):
    print("Rezultatul pentru cuvantul " + cuvant + "este : ")
    print(evalueaza(cuvant, test))
f = open("testee")
n = int(f.readline())
char = [x for x in f.readline().split()]
q0 = int(f.readline())
fin = {int(x) for x in f.readline().split()}
l=[{} for i in range(n)]
st = f.readline()
while st!="":
    (a,b,c)=[x for x in st.split()]
    if b not in l[int(a)]:
        l[int(a)][b]=set()
    l[int(a)][b].add(int(c))
    st=f.readline()
test = set()
test.add(q0)
afis('abxyyyxyby')
afis('bcax')
afis('bcbxxy')
afis('abyyxz')
afis('abyyxyx')
