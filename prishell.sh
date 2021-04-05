#!/bin/bash

##### SCRIPT POUR CREER DATABASE EMPLOYE AVEC CLEF PUB ET PRIV ##############


#---------------------------------------------------------------------------#
# où se trouve le fichier csv employé à utiliser?
#---------------------------------------------------------------------------#
echo "Quel est le chemin du fichier d'employés à utiliser?"
read file
echo "Vous utilisez le chemin suivant $file" 


#---------------------------------------------------------------------------#
# Transforme ce fichier sans espace et tabulation mais garde lignes
#---------------------------------------------------------------------------#
cat $file | sed 's/[[:space:]]//g' > file


#---------------------------------------------------------------------------#
# compte les lignes de ce fichier
#---------------------------------------------------------------------------#
nb=$(cat file | wc -l)
echo "Vous avez $nb lignes"
let nb+=1


#---------------------------------------------------------------------------#
# Boucle pour créer clef priv et pub en fonction du nombre d'employés
#---------------------------------------------------------------------------#
umask 077
for i in $(seq 2 $nb);
do
	priv=$(wg genkey)
	echo ","$i","$priv","$(echo $priv | wg pubkey) >> pripu
done


#---------------------------------------------------------------------------#
# concatener les 2 fichiers csv + pripu et nettoyage
#---------------------------------------------------------------------------#
paste -d'\0' file pripu > final
rm pripu file


#---------------------------------------------------------------------------#
# Ajoute la ligne d'index de la future base de donnée # attention bash 
#---------------------------------------------------------------------------#
sed -i '' '1s/^/PRENOM,NOM,EMAIL,ID,PRIVKEY,PUBKEY\'$'\n/g' final

# ATTENTION code pour MacOS : pour GNU sed utiliser $ sed -i '1 i\anything' file


#---------------------------------------------------------------------------#
# Ecris le message et excecute le script python
#---------------------------------------------------------------------------#
echo "Votre fichier contenant NOM,PRENOM,ID,PRIVATEKEY,PUBLICKEY est prêt, il s'apelle 'final', Le script python3 script_p6.py se lance"
python3 script_p6.py


