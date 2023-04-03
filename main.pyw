from tkinter import *
from random import randint
from time import time
from math import sqrt

def mousebuttondown(event) :
    global l_objets
    global l_pheromones
    global c_attente
    global grab
    non = ""
    for i in range (len(l_objets["noeuds"])) :
        if l_objets["noeuds"][i][0]-rayon_objets < event.x < l_objets["noeuds"][i][0]+rayon_objets and l_objets["noeuds"][i][1]-rayon_objets < event.y < l_objets["noeuds"][i][1]+rayon_objets :
            non = i
            break
    if non != "" :
        if event.num == 1 :
            grab = non
            if outil.get() == "4" :
                c_attente += [non]
                if len(c_attente) == 2 :
                    if not c_attente in l_objets["chemins"] and c_attente[0] != c_attente[1] : l_objets["chemins"],l_pheromones = l_objets["chemins"]+[c_attente],l_pheromones+[0]
                    c_attente = []
        elif event.num == 3 :
            del l_objets["noeuds"][non]
            i = 0
            while i < len(l_objets["chemins"]) :
                if non in l_objets["chemins"][i] :
                    del l_objets["chemins"][i]
                    del l_pheromones[i]
                else :
                    if "nid" != l_objets["chemins"][i][0] != "nourriture" and l_objets["chemins"][i][0] > non : l_objets["chemins"][i][0] -= 1
                    if "nid" != l_objets["chemins"][i][1] != "nourriture" and l_objets["chemins"][i][1] > non : l_objets["chemins"][i][1] -= 1
                    i += 1
    elif len(l_objets["nid"]) > 0 and l_objets["nid"][0]-rayon_objets < event.x < l_objets["nid"][0]+rayon_objets and l_objets["nid"][1]-rayon_objets < event.y < l_objets["nid"][1]+rayon_objets :
        if event.num == 1 :
            grab = "nid"
            if outil.get() == "4" :
                c_attente += ["nid"]
                if len(c_attente) == 2 :
                    if not c_attente in l_objets["chemins"] and c_attente[0] != c_attente[1] : l_objets["chemins"],l_pheromones = l_objets["chemins"]+[c_attente],l_pheromones+[0]
                    c_attente = []
        elif event.num == 3 :
            l_objets["nid"] = []
            i = 0
            while i < len(l_objets["chemins"]) :
                if "nid" in l_objets["chemins"][i] :
                    del l_objets["chemins"][i]
                    del l_pheromones[i]
                else : i += 1
    elif len(l_objets["nourriture"]) > 0 and l_objets["nourriture"][0]-rayon_objets < event.x < l_objets["nourriture"][0]+rayon_objets and l_objets["nourriture"][1]-rayon_objets < event.y < l_objets["nourriture"][1]+rayon_objets :
        if event.num == 1 :
            grab = "nourriture"
            if outil.get() == "4" :
                c_attente += ["nourriture"]
                if len(c_attente) == 2 :
                    if not c_attente in l_objets["chemins"] and c_attente[0] != c_attente[1] : l_objets["chemins"],l_pheromones = l_objets["chemins"]+[c_attente],l_pheromones+[0]
                    c_attente = []
        elif event.num == 3 :
            l_objets["nourriture"] = []
            i = 0
            while i < len(l_objets["chemins"]) :
                if "nourriture" in l_objets["chemins"][i] :
                    del l_objets["chemins"][i]
                    del l_pheromones[i]
                else : i += 1
    elif event.num == 1 :
        if outil.get() == "1" : l_objets["nid"] = [event.x,event.y]
        elif outil.get() == "2" : l_objets["nourriture"] = [event.x,event.y]
        elif outil.get() == "3" : l_objets["noeuds"] += [[event.x,event.y]]
    if b_pause["text"] == ">" : affich()

def mousebuttonup(event) :
    global grab
    grab = ""

def mousemotion(event) :
    global l_objets
    global c_attente
    if grab != "" :
        c_attente = []
        if type(grab) == str : l_objets[grab] = [event.x,event.y]
        else : l_objets["noeuds"][grab] = [event.x,event.y]
    if b_pause["text"] == ">" : affich()

def keydown_return_intervalle(event) :
    global param
    try : param["intervalle"] = float(entree_intervalle.get())
    except : ""

def keydown_return_taux_r(event) :
    global param
    try : param["taux_r"] = float(entree_taux_r.get())
    except : ""

def keydown_return_taux_d(event) :
    global param
    try : param["taux_d"] = float(entree_taux_d.get())
    except : ""

def keydown_return_sortie(event) :
    global param
    try : param["sortie"] = float(entree_sortie.get())
    except : ""

def keydown_return_fps(event) :
    global param
    try : param["fps"] = float(entree_fps.get())
    except : ""

def keydown_return_rayon_objets(event) :
    global rayon_objets
    try : rayon_objets = float(entree_rayon_objets.get())
    except : ""

def keydown_return_largeur_chemins(event) :
    global largeur_chemins
    try : largeur_chemins = float(entree_largeur_chemins.get())
    except : ""

def keydown_return_rayon_fourmis(event) :
    global rayon_fourmis
    try : rayon_fourmis = float(entree_rayon_fourmis.get())
    except : ""

def change_pause() :
    global b_pause
    if b_pause["text"] == "| |" : b_pause["text"] = ">"
    else :
        b_pause["text"] = "| |"
        mouv_fourmis()
        effets()

def mouv_fourmis() :
    global l_fourmis
    i = 0
    while i < len(l_fourmis) :
        coords1,coords2 = l_objets[l_fourmis[i][4]] if type(l_fourmis[i][4]) == str else l_objets["noeuds"][l_fourmis[i][4]],l_objets[l_fourmis[i][2]] if type(l_fourmis[i][2]) == str else l_objets["noeuds"][l_fourmis[i][2]]
        l_fourmis[i][0] += 1
        if l_fourmis[i][0] >= sqrt((coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2) :
            if l_fourmis[i][1] == 0 :
                l_fourmis[i][0],direc = 0,choix_direction(l_fourmis[i][2],l_fourmis[i][4])
                if l_fourmis[i][2] == "nourriture" :
                    l_fourmis[i][1],l_fourmis[i][2],l_fourmis[i][4] = 1,l_fourmis[i][3][-1],l_fourmis[i][2]
                    del l_fourmis[i][3][-1]
                elif direc == "" :
                    l_fourmis[i][1],l_fourmis[i][2],l_fourmis[i][4] = 2,l_fourmis[i][3][-1],l_fourmis[i][2]
                    del l_fourmis[i][3][-1]
                else : l_fourmis[i][2],l_fourmis[i][3],l_fourmis[i][4] = direc,l_fourmis[i][3]+[l_fourmis[i][2]],l_fourmis[i][2]
            else :
                if l_fourmis[i][1] == 1 :
                    if [l_fourmis[i][2],l_fourmis[i][4]] in l_objets["chemins"] : l_pheromones[l_objets["chemins"].index([l_fourmis[i][2],l_fourmis[i][4]])] += param["taux_d"]
                    elif [l_fourmis[i][4],l_fourmis[i][2]] in l_objets["chemins"] : l_pheromones[l_objets["chemins"].index([l_fourmis[i][4],l_fourmis[i][2]])] += param["taux_d"]
                if l_fourmis[i][2] == "nid" :
                    del l_fourmis[i]
                    i -= 1
                else :
                    l_fourmis[i][0] = 0
                    l_fourmis[i][2],l_fourmis[i][4] = l_fourmis[i][3][-1],l_fourmis[i][2]
                    del l_fourmis[i][3][-1]
        i += 1
    affich()
    if b_pause["text"] == "| |" :
        try : canvas.after(int(1000/param["fps"]),mouv_fourmis)
        except : canvas.after(50,mouv_fourmis)

def effets() :
    global l_fourmis
    global l_pheromones
    global time_generation
    global time_pheromones
    if len(l_objets["nid"]) > 0 and time()-time_generation >= param["sortie"] :
        direc,time_generation = choix_direction("nid",""),time()
        if direc != "" : l_fourmis += [[0,0,direc,["nid"],"nid"]]
    if time()-time_pheromones >= param["intervalle"] :
        time_pheromones = time()
        for i in range (len(l_pheromones)) :
            l_pheromones[i] -= param["taux_r"]
            if l_pheromones[i] < 0 : l_pheromones[i] = 0
    if b_pause["text"] == "| |" : canvas.after(10,effets)

def choix_direction(position,chemin_arrivee) :
    l_possib = []
    for i in range (len(l_objets["chemins"])) :
        if position in l_objets["chemins"][i] and not chemin_arrivee in l_objets["chemins"][i] : l_possib += [i]
    if len(l_possib) > 0 :
        c = []
        for i in l_possib :
            for j in range (int(l_pheromones[i]+1)) :
                c += [i]
        c = c[randint(0,len(c)-1)]
        if l_objets["chemins"][c][0] == position : return l_objets["chemins"][c][1]
        else : return l_objets["chemins"][c][0]
    else : return ""

def affich() :
    canvas.delete("all")
    for i in l_objets["chemins"] :
        pos = [l_objets["nid"] if i[j] == "nid" else l_objets["nourriture"] if i[j] == "nourriture" else l_objets["noeuds"][i[j]] for j in range (2)]
        canvas.create_line(pos[0][0],pos[0][1],pos[1][0],pos[1][1],fill="white",width=largeur_chemins)
    for i in l_objets["noeuds"] :
        canvas.create_oval(i[0]-rayon_objets,i[1]-rayon_objets,i[0]+rayon_objets,i[1]+rayon_objets,fill="blue",outline="blue")
    if len(l_objets["nid"]) > 0 : canvas.create_oval(l_objets["nid"][0]-rayon_objets,l_objets["nid"][1]-rayon_objets,l_objets["nid"][0]+rayon_objets,l_objets["nid"][1]+rayon_objets,fill="green",outline="green")
    if len(l_objets["nourriture"]) > 0 : canvas.create_oval(l_objets["nourriture"][0]-rayon_objets,l_objets["nourriture"][1]-rayon_objets,l_objets["nourriture"][0]+rayon_objets,l_objets["nourriture"][1]+rayon_objets,fill="red",outline="red")
    for i in l_fourmis :
        coords1,coords2 = l_objets[i[4]] if type(i[4]) == str else l_objets["noeuds"][i[4]],l_objets[i[2]] if type(i[2]) == str else l_objets["noeuds"][i[2]]
        x,y = coords1[0]+(coords2[0]-coords1[0])/sqrt((coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2)*i[0],coords1[1]+(coords2[1]-coords1[1])/sqrt((coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2)*i[0]
        canvas.create_oval(x-rayon_fourmis,y-rayon_fourmis,x+rayon_fourmis,y+rayon_fourmis,fill="black",outline="black")
    for i in range (len(l_objets["chemins"])) :
        x1,x2,y1,y2 = l_objets[l_objets["chemins"][i][0]][0] if type(l_objets["chemins"][i][0]) == str else l_objets["noeuds"][l_objets["chemins"][i][0]][0],l_objets[l_objets["chemins"][i][1]][0] if type(l_objets["chemins"][i][1]) == str else l_objets["noeuds"][l_objets["chemins"][i][1]][0],l_objets[l_objets["chemins"][i][0]][1] if type(l_objets["chemins"][i][0]) == str else l_objets["noeuds"][l_objets["chemins"][i][0]][1],l_objets[l_objets["chemins"][i][1]][1] if type(l_objets["chemins"][i][1]) == str else l_objets["noeuds"][l_objets["chemins"][i][1]][1]
        canvas.create_text((x1+x2)/2,(y1+y2)/2,text=str(l_pheromones[i]),font="Arial 12",fill="purple")

fenetre = Tk()
fenetre.resizable(width=False,height=False)

canvas = Canvas(fenetre,width=500,height=500,bg="grey")
canvas.pack(side=LEFT,padx=0,pady=0)
canvas.bind("<ButtonPress>",mousebuttondown)
canvas.bind("<ButtonRelease>",mousebuttonup)
canvas.bind("<Motion>",mousemotion)

cadre_droite = LabelFrame(fenetre,borderwidth=0,padx=0,pady=0)
cadre_droite.pack(side=LEFT,fill="both",expand="yes")

cadre_outil = LabelFrame(cadre_droite,text="Outils :",borderwidth=1,padx=0,pady=0)
cadre_outil.pack(side=TOP,fill="both",expand="no")

outil = StringVar()
b_outil1 = Radiobutton(cadre_outil,text="Nid",variable=outil,value=1,state=ACTIVE).pack(side=TOP,anchor="w",padx=0,pady=0)
b_outil2 = Radiobutton(cadre_outil,text="Nourriture",variable=outil,value=2,state=ACTIVE).pack(side=TOP,anchor="w",padx=0,pady=0)
b_outil3 = Radiobutton(cadre_outil,text="Noeud",variable=outil,value=3,state=ACTIVE).pack(side=TOP,anchor="w",padx=0,pady=0)
b_outil4 = Radiobutton(cadre_outil,text="Chemin",variable=outil,value=4,state=ACTIVE).pack(side=TOP,anchor="w",padx=0,pady=0)
outil.set("1")

cadre_param = LabelFrame(cadre_droite,text="Paramètres :",borderwidth=1,padx=0,pady=0)
cadre_param.pack(side=TOP,fill="both",expand="no")

cadre_intervalle = LabelFrame(cadre_param,borderwidth=0,padx=0,pady=0)
cadre_intervalle.pack(side=TOP,fill="both",expand="no")
Label(cadre_intervalle,text="Intervalle retrait phéromones : ").pack(side=LEFT,padx=0,pady=0)
entree_intervalle = Entry(cadre_intervalle,width=5)
entree_intervalle.pack(side=LEFT,padx=0,pady=0)
entree_intervalle.insert(0,"2")
entree_intervalle.bind("<Return>",keydown_return_intervalle)
Label(cadre_intervalle,text="s").pack(side=LEFT,padx=0,pady=0)

cadre_taux_r = LabelFrame(cadre_param,borderwidth=0,padx=0,pady=0)
cadre_taux_r.pack(side=TOP,fill="both",expand="no")
Label(cadre_taux_r,text="Taux phéromone retiré : ").pack(side=LEFT,padx=0,pady=0)
entree_taux_r = Entry(cadre_taux_r,width=5)
entree_taux_r.pack(side=LEFT,padx=0,pady=0)
entree_taux_r.insert(0,"1")
entree_taux_r.bind("<Return>",keydown_return_taux_r)

cadre_taux_d = LabelFrame(cadre_param,borderwidth=0,padx=0,pady=0)
cadre_taux_d.pack(side=TOP,fill="both",expand="no")
Label(cadre_taux_d,text="Taux phéromone déposé : ").pack(side=LEFT,padx=0,pady=0)
entree_taux_d = Entry(cadre_taux_d,width=5)
entree_taux_d.pack(side=LEFT,padx=0,pady=0)
entree_taux_d.insert(0,"1")
entree_taux_d.bind("<Return>",keydown_return_taux_d)

cadre_sortie = LabelFrame(cadre_param,borderwidth=0,padx=0,pady=0)
cadre_sortie.pack(side=TOP,fill="both",expand="no")
Label(cadre_sortie,text="Intervalle sortie fourmis : ").pack(side=LEFT,padx=0,pady=0)
entree_sortie = Entry(cadre_sortie,width=5)
entree_sortie.pack(side=LEFT,padx=0,pady=0)
entree_sortie.insert(0,"1")
Label(cadre_sortie,text="s").pack(side=LEFT,padx=0,pady=0)
entree_sortie.bind("<Return>",keydown_return_sortie)

cadre_fps = LabelFrame(cadre_param,borderwidth=0,padx=0,pady=0)
cadre_fps.pack(side=TOP,fill="both",expand="no")
Label(cadre_fps,text="FPS : ").pack(side=LEFT,padx=0,pady=0)
entree_fps = Entry(cadre_fps,width=5)
entree_fps.pack(side=LEFT,padx=0,pady=0)
entree_fps.insert(0,"20")
entree_fps.bind("<Return>",keydown_return_fps)

b_pause = Button(cadre_param,text="| |",command=change_pause)
b_pause.pack(side=TOP,anchor="w",padx=0,pady=0)

cadre_graphique = LabelFrame(cadre_droite,text="Paramètres visuels :",borderwidth=1,padx=0,pady=0)
cadre_graphique.pack(side=TOP,fill="both",expand="no")

cadre_rayon_objets = LabelFrame(cadre_graphique,borderwidth=0,padx=0,pady=0)
cadre_rayon_objets.pack(side=TOP,fill="both",expand="no")
Label(cadre_rayon_objets,text="Rayon des objets : ").pack(side=LEFT,padx=0,pady=0)
entree_rayon_objets = Entry(cadre_rayon_objets,width=5)
entree_rayon_objets.pack(side=LEFT,padx=0,pady=0)
entree_rayon_objets.insert(0,"10")
entree_rayon_objets.bind("<Return>",keydown_return_rayon_objets)

cadre_largeur_chemins = LabelFrame(cadre_graphique,borderwidth=0,padx=0,pady=0)
cadre_largeur_chemins.pack(side=TOP,fill="both",expand="no")
Label(cadre_largeur_chemins,text="Largeur des chemins : ").pack(side=LEFT,padx=0,pady=0)
entree_largeur_chemins = Entry(cadre_largeur_chemins,width=5)
entree_largeur_chemins.pack(side=LEFT,padx=0,pady=0)
entree_largeur_chemins.insert(0,"10")
entree_largeur_chemins.bind("<Return>",keydown_return_rayon_objets)

cadre_rayon_fourmis = LabelFrame(cadre_graphique,borderwidth=0,padx=0,pady=0)
cadre_rayon_fourmis.pack(side=TOP,fill="both",expand="no")
Label(cadre_rayon_fourmis,text="Rayon des fourmis : ").pack(side=LEFT,padx=0,pady=0)
entree_rayon_fourmis = Entry(cadre_rayon_fourmis,width=5)
entree_rayon_fourmis.pack(side=LEFT,padx=0,pady=0)
entree_rayon_fourmis.insert(0,"2")
entree_rayon_fourmis.bind("<Return>",keydown_return_rayon_fourmis)

# x,y
# x,y
# [x,y],[x,y]
# [n1,n2],[n1,n2]

# emplacement,etat,direction,[chemin empreinté]
l_objets,l_pheromones,l_fourmis,c_attente,grab,rayon_objets,largeur_chemins,rayon_fourmis,time_generation,time_pheromones,param = {"nid" : [],"nourriture" : [],"noeuds" : [],"chemins" : []},[],[],[],"",10,10,2,time(),time(),{"intervalle" : 2,"taux_r" : 1,"taux_d" : 1,"sortie" : 1,"fps" : 20}

mouv_fourmis()
effets()

fenetre.mainloop()