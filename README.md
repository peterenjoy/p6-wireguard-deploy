# p6-wireguard-deploy

## Genèse
Dans le cadre de mon projet 6 OpenClassroom, nous avions pour mission d'identifier une tache répétitive et chronophage (et sujette à erreur...).
Dans mes précédents projets j'avais eu quelques difficultés avec le VPN Wireguard et ses fichiers de configurations. Je me suis dit qu'un script automatisant
la création de fichier de configuration écarterait les erreurs mais aussi ferait gagner un temps précieux lorsqu'il faudra générer des dizaines de fichiers
pour les clients

## Pourquoi ce script?
Pour aller plus vite! En effet, si vous avez à déployer sur des dizaines voire centaines d'ordinateur des fichiers de configurations pour Wireguard
et en parallèle créer un ficher "server.conf" avec autant de lignes de configurations, alors... ce script est fait pour vous.
[Wireguard](https://www.wireguard.com/install) permet simplement de créer un VPN: Votre client n'aura qu'a installer une version de Wireguard sur sa machine (PC, mac, Linux...)
et utiliser le fichier de configuration qui aura été généré pour lui/elle.


## Installation
Pour faire tourner ce script, il faut tout d'abord avoir installé Wireguard et Python3 sur votre ordinateur
* Sur MacOS : `brew install wireguard-tools python3`
* Sur Linux : `apt-get install wireguard python3`

## Utilisation
1. sdgf


Contributing
