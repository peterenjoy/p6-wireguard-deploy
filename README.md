# p6-wireguard-deploy

> Pourquoi ce nom étrange?
> * _P6_ : pour le numéro de mon projet 
> * _Wireguard_ : le nom du logiciel qui soutend mon script 
> * _Deploy_ : comme déploiement (...en grand nombre)

## Genèse
Dans le cadre de mon projet 6 OpenClassroom, nous avions pour mission d'identifier une tache répétitive et chronophage (et sujette à erreur...).
Dans mes précédents projets j'avais eu quelques difficultés avec le VPN Wireguard et ses fichiers de configurations. Je me suis dit qu'un script automatisant
la création de fichier de configuration écarterait les erreurs d'écriture de configuration mais aussi ferait gagner un temps précieux lorsqu'il faudra générer des dizaines de fichiers pour les clients

## Pourquoi ce script?
Pour aller plus vite! En effet, si vous avez à déployer sur des dizaines voire centaines d'ordinateurs des fichiers de configurations pour Wireguard
**et** en parallèle créer un ficher "server.conf" avec autant de lignes de configurations, alors... ce script est fait pour vous.
[Wireguard](https://www.wireguard.com/install) permet simplement de créer un VPN: Votre client n'aura qu'a installer une version de Wireguard sur sa machine (PC, mac, Linux...) et utiliser le fichier de configuration qui aura été généré pour lui/elle.

## Installation
Pour faire tourner ce script, il faut tout d'abord avoir installé Wireguard et Python3 sur votre ordinateur
* Sur MacOS : `brew install wireguard-tools python3`
* Sur Linux : `apt-get install wireguard python3`

## Prérequis
Il vous faut au préalable avoir préparé un fichier au format CSV avec comme délimiteur ",". Ce fichier contiendra la liste de vos clients avec 3 informations (colonnes) à la sujet : PRENOM,NOM,EMAIL. <u>Il ne faut pas<u> rajouter ces infos. Listez simplement vos clients.
  
## Utilisation
1. Avec votre terminal ou shell, se placer dans le répertoire où vous avez téléchargé le programme
2. lancer le programme via la commande ```bash python3 script_p6.py```
3. Votre terminal vous demande de sélectionner un fichier
4. Le programme vous demande si vous voulez ajouter d'autres clients à une configuration précédente. répondez "oui" ou "non".
5. Si oui, tapez oui puis "entrer" puis indiquez les dernièrs chiffres de l'addresse IP de votre dernier client dans votre fichier server.conf (ex : 10.0.0.42, tapez 42)
6. Si non, tapez non
7. et voilà ! Vos fichiers de configuration sont prêt
8. Les fichiers de configuration à envoyer à vos clients sont dans le dossier _"files"_
9. Le fichier de configuration pour votre serveur Wireguard se trouve dans votre dossier courant! **Bonne utilisation!**

## Licence

[MIT](https://github.com/peterenjoy/p6-wireguard-deploy/blob/701bd02b6ad1e0070a3b6aac8dd17860ecfea7b9/LICENSE)
> C'est tout à vous!
> 










_`Pierre Hellequin - Avril 2021 - Dans le cadre de ma formation Openclassroom`_
