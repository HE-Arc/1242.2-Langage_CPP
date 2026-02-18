---
title: "Prise en main de Visual Studio 2026"
author: "Benoit Le Callennec"
date: 2026-02-10
tags : ["Visual Studio 2026", "Général"]
draft: false
---

## Installation
Vous pouvez télécharger Visual Studio 2026 Community Edition ici : [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

{{< figure src="images/DownloadVS2026.png#center" width="100%">}}

Durant l'installation, il faut choisir "Développement Desktop en C++" :

{{< figure src="images/InstallVS2026.png#center" width="100%">}}

## Créer un nouveau projet
{{< figure src="images/CreateVS2026Project.png#center" width="100%">}}

## Ajouter un fichier source **`main.cpp`**
Dans le fenêtre **`explorateur de solutions`**, clic droit sur **`Fichiers sources`**, puis **`Ajouter`** -> **`Nouvel élément`** -> **`main.cpp`**

## Développement
Durant le développement, vous pouvez utiliser les raccourcis clavier suivants :
- mode plein écran : **`Alt+Shift+Enter`**
- formater tout le code : **`Ctrl+K, Ctrl+D`**
- formater le code sélectionné : **`Ctrl+K, Ctrl+F`**
- commenter le code sélectionné : **`Ctrl+K, Ctrl+C`**
- décommenter le code sélectionné : **`Ctrl+K, Ctrl+U`**
- compiler le fichier courant : **`Ctrl+F7`**
- compiler **tout** le programme : **`Ctrl+Shift+B`** 
- éditer plusieurs lignes de code à la fois : **`Shift` + `Alt` + flèches du bas (ou haut)** (pour choisir les lignes à éditer en parallèle)

## Exécuter le programme
Pour exécuter le programme, vous pouvez utiliser les raccourcis clavier suivants :
- exécuter le programme : **`Ctrl+F5`**

## Debugger
Pour lancer le programme en vue de le débugger, vous pouvez utiliser les raccourcis clavier suivants :
- exécuter le programme en mode Debug : **`F5`**
- mettre un breakpoint : **`F9`**
- avancer pas à pas : **`F10`**
- rentrer dans une fonction : **`F11`**

Lorsque le programme atteint un breakpoint, il s'arrête.
Les variables visibles à cet instant du programme sont affichées dans la fenêtre dédiée :
{{< figure src="images/DebugVS2026.png#center" width="100%">}}
