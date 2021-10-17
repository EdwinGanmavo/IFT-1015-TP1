import turtle
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
def carree(largeurCase):
    for i in range(4):
         turtle.lt(90)
         turtle.fd(largeurCase)
def positionnement(largeurCase):
    for b in range(1):
        turtle.pu()
        turtle.fd(largeurCase)
        turtle.pd()
def positionnement2(largeurCase,nx):
    turtle.pu()
    turtle.lt(180)
    turtle.fd(nx*largeurCase)
    turtle.rt(270)
    turtle.fd(largeurCase)
    turtle.lt(90)
    turtle.fd(largeurCase)
    turtle.pd()
def grille(largeurCase,nx,ny):
    for a in range(ny-1):
         for y in range(nx-1):
            carree(largeurCase)
            positionnement(largeurCase)
         for b in range(1):
            carree(largeurCase)
         positionnement2(largeurCase,nx)
    for s in range(1):
        for y in range(nx - 1):
            carree(largeurCase)
            positionnement(largeurCase)
        for b in range(1):
            carree(largeurCase)
grille(20,5,5)
