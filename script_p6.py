#!/usr/bin/python3
# -*- coding: utf-8 -*-



# importe le csv des noms, prenom et email
import pandas as pd
import fileinput
import os
import sys
from string import Template

path=os.getcwd()
db = pd.read_csv(path+'/final')
print(db)

# ci dessous à utiliser dans le loop
for i in range(len(db)):
    with open(path+'/user.conf', 'r') as f:
        NOM = db.loc[i, "NOM"]
        PRENOM = db.loc[i, "PRENOM"]
        FILENAME = f'{PRENOM}_{NOM}.conf'
        IP = db.loc[i, "ID"]
        PK = db.loc[i, "PRIVKEY"]
        PUB = db.loc[i, "PUBKEY"]
        t = Template(f.read())
        open(FILENAME, 'w').write(t.substitute(IP=IP, PK=PK))
        open(path+'/server.conf', 'a+').write(f'[Peer]\n# {FILENAME}\nPublicKey = {PUB}\nAllowedIPs = 10.0.0.{IP}/32\n') 




