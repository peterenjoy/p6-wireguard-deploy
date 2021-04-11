#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import fileinput
import os
import sys
import subprocess
from string import Template
from tkinter import Tk
from tkinter.filedialog import askopenfilename
path=os.getcwd()


#---------------------------------------------------------------------------#
# où se trouve le fichier csv employés à utiliser?
#---------------------------------------------------------------------------#
print ('Choisissez un fichier à traiter')
file = askopenfilename()
print ('Vous avez choisi '+file)


#---------------------------------------------------------------------------#
# compte les lignes de ce fichier et +1
#---------------------------------------------------------------------------#
nb = sum(1 for line in open(file))
nb+=2

#---------------------------------------------------------------------------#
# Transforme ce fichier sans espace et tabulation mais garde lignes
#---------------------------------------------------------------------------#
with open(file, 'r') as i:
    d=i.read()
    d=d.replace('\t','')
    d=d.replace(' ','')
open('file','w').write(d)


#---------------------------------------------------------------------------#
# Créé le fichier pubkey/privkey venant de bash (commande 'wg') 
#---------------------------------------------------------------------------#
for i in range (2, nb):
    output = subprocess.check_output('priv=$(wg genkey) ; echo $priv","$(echo $priv | wg pubkey)', shell=True)
    wg = output.decode('ascii')
    open('wg','at+').write(f',{i},{wg}')


#---------------------------------------------------------------------------#
# concatener les fichiers employés et wg , puis ajoute une ligne
#---------------------------------------------------------------------------#
with open('wg') as wg, open('file') as f, open('data','w') as da:
    wg_l=wg.readlines()
    f_l=f.readlines()
    da.write('PRENOM,NOM,EMAIL,ID,PRIVKEY,PUBKEY\n')
    for i in range(len(wg_l)):
        line=f_l[i].strip() + wg_l[i]
        da.write(line)
os.remove('wg')
os.remove('file')


#---------------------------------------------------------------------------#
# Vérifier que la base de donnée ne contient pas de valeurs manquantes
#---------------------------------------------------------------------------#
db = pd.read_csv('data')
print(db)

nb=db.isnull().sum().sum()
nb_list=db.isnull().sum().tolist()
obj_list=db.columns.tolist()
if nb==0:
    print('Votre Base de donnée est complète')
else:
    for i in range(len(nb_list)):
        print(f'Il vous manque {nb_list[i]} élement(s) dans {obj_list[i]}')
    print("Merci de modifier votre base de données pour qu'elle soit complète")
    exit()


#---------------------------------------------------------------------------#
# Créé les fichiers conf et les mets dans un dossier files:
#---------------------------------------------------------------------------#
os.makedirs(path+'/files')
files=path+'/files'
for i in range(len(db)):
    with open(path+'/user.conf', 'r') as f:
        NOM = db.loc[i, "NOM"]
        PRENOM = db.loc[i, "PRENOM"]
        FILENAME = f'{PRENOM}_{NOM}.conf'
        IP = db.loc[i, "ID"]
        PK = db.loc[i, "PRIVKEY"]
        PUB = db.loc[i, "PUBKEY"]
        t = Template(f.read())
        open(files+'/'+FILENAME, 'w').write(t.substitute(IP=IP, PK=PK))
        open(path+'/server.conf', 'a+').write(f'[Peer]\n# {FILENAME}\nPublicKey = {PUB}\nAllowedIPs = 10.0.0.{IP}/32\n') 




