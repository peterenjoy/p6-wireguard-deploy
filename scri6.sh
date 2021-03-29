#!/bin/bash

# où se trouve le fichier à utiliser
echo "Quel est le chemin du fichier d'employés à utiliser?"
read file
echo "Vous utilisez le chemin suivant $file"

nb=$(cat $file | wc -l)

echo "Vous avez $nb lignes"
umask 077
for i in $(seq 0 $nb);
do
	priv=$(wg genkey)
	echo $i","$priv","$(echo $priv | wg pubkey) >> pripu
	cat pripu
done

# concatener les 2 fichiers csv + pripu
paste $file pripu | final
echo "Votre fichier contenant NOM, PRENOM, EMAIL, ID, PRIVKEY, PUBKEY est prêt"

