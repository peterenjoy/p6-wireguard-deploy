#!/bin/bash

############# SCRIPT POUR CREER DATABASE EMPLOYE AVEC CLEF PUB ET PRIV ######################


# où se trouve le fichier csv employé à utiliser?
echo "Quel est le chemin du fichier d'employés à utiliser?"
read file
echo "Vous utilisez le chemin suivant $file" 


# Transforme ce fichier sans espace et Tab mais garde lignes
cat $file | sed 's/[[:space:]]//g' > file 


# compte les lignes de ce fichier 
nb=$(cat file | wc -l)
echo "Vous avez $nb lignes"


# Boucle pour créer clef priv et pub en fonction du nombre d'employés
umask 077
for i in $(seq 1 $nb);
do
	priv=$(wg genkey)
	echo ","$i","$priv","$(echo $priv | wg pubkey) >> pripu
done


# concatener les 2 fichiers csv + pripu
paste -d'\0' file pripu > final


# nettoyage
rm pripu file
echo "Votre fichier contenant NOM,PRENOM,ID,PRIVATEKEY,PUBLICKEY est prêt, il s'apelle final"
