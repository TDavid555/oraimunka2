"""
1.f: kiírjuk 1-50 közötti páratlanokat
2.f: Listába tároljuk felh. által 5db int, hány olyan van ami 3 és 5-tel oszt
3.f: Fv. param kap 2 stringet, térjen vissza a hosszabb szóval
4.f: Elj. listában tároljuk felh. 5 stringet van-e olyan ami a-ra végz(T.K.)
5.f: Fv. Szótárban tárolj 5 int=>string, melyek kezdődnek a-karakterrel, tárold listában
"""

#1.
for x in range(1,51,1):
    if x %2 != 0:
        print(x)

print()

#2.
"""
lista = []
for x in range (1,6,1):
    szamok = int(input("Kérem a számokat: "))
    lista.append(szamok)

for x in lista:
    if x %3 ==0 and x %5 ==0:
        print(x)
"""
print()

#3.
def fugg(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2


print(fugg("szo", "masikszo"))

print()

#4.
def elj():
    lista2 = []
    for x in range (1,6,1):
        stringek = input("Kérem a szavakat: ")
        lista2.append(stringek)

    van=False
    for x in lista2:
        if x[len(x)-1] == "a":
            van = True

    if van:
        print("Van")
    else:
        print("Nincs")


#elj()

print()

#5.
def fugg2():

    lista3 = []
    szotar = {
        1: "string1",
        2: "string2",
        3: "astring3",
        4: "string4",
        5: "astring5"
    }

    for x in szotar:
        if szotar[x][0] == "a":
            lista3.append(szotar[x])

    return lista3

for x in fugg2():
    print(x)






