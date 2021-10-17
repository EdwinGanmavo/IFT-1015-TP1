def iota(n):
    if n >= 0:
        return range(n)
    else:
        print("error, n must be a negative Integer")

def contient(tab, x):
    return x in tab

def ajouter(tab, x):
    if x >= 0 and not x in tab:
        tab.append(x)
        return tab
    else:
        print("error, x must be a positive integer and not already included in tab, nothing added")
        return tab

def retirer(tab, x):
    if x in tab:
        del tab[tab.index(x)]
        return tab
    else:
        print("error, x must be in tab, nothing have been deleted")
        return tab
def voisins(x,y,nX,nY):
    list=[]
    list.append(x + (y - 1) * nX)
    list.append(x-1+y*nX)
    list.append(x+(y+1)*nX)
    list.append(x + 1 + y * nX)

    if x==0:
        list.pop(1)
    elif y==0:
        list.pop(0)
    elif y-1==nY:
        list.pop(2)
    elif x+1==nX:
        list.pop(3)


    return list
print(voisins(6,2,8,4))

