---
title: "Getting Started"
type: docs
weight: 10
draft: true
---
# Gettings Started

## Récupérer le template
1. Se rendre sur **[le git contenant un template](https://gitlab-etu.ing.he-arc.ch/benoit.lecallen/template_website)**.
2. Cliquer sur le bouton **`Fork`**.
{{< figure src="/images/AE_Fork.png#center" >}}
3. Éditer le champ **`Project name`** (voir Figure ci-dessous).
4. Dans le champ **`Select a namespace`**, choisir votre espace personnel (voir Figure ci-dessous).
{{< figure src="/images/AE_ForkedProject.png#center" >}}
**ATTENTION :** bien laisser la visibilité du projet sur **`Internal`**.
5. Cliquer sur le bouton **`Fork project`**.
6. Se rendre dans son espace personnel et cloner son repository.

## Installer Hugo
1. Télécharger [l'exécutable **`Hugo`**](/hugo.zip) et le dézipper dans le répertoire **`bin`** à la racine du site.

## Lancer le site en local
1. Ouvrir un Terminal dans Visual Studio Code.
2. Se rendre dans le répertoire du site.
3. Lancer la commande **`bin/hugo server`**.
4. Ouvrir un navigateur et se rendre sur l'adresse **`http://localhost:1313`**.

## Configurer le site en local
1. Éditer le fichier **`config.toml`**.

## Éditer le site en local
1. Utiliser la page **`Page Template`** comme base.
Elle regroupe les commandes les plus courantes.
2. Cacher les pages **`Page Template`** et **`Getting Started`** en les marquant comme **`Draft`**.
Ainsi, elles seront visibles en mode **`Debug`** (grâce à l'option -D dans **`Hugo`**), mais pas en mode **`Release`**.
2. Exécuter les commandes **`git`** nécessaires pour mettre à jour le site.
3. Vérifier que le site se met à jour correctement en ligne.

## Éditer le site en ligne
1. Se rendre sur le site du gitlab de la HE-Arc.
2. Se rendre dans le répertoire du site.
3. Éditer les fichiers nécessaires.
4. Vérifier que le site se met à jour correctement en ligne.

## Quand on est prêt
Une fois que le site est prêt à être publié pour les étudiants, il faut contacter le LabInfo pour transférer le site de votre espace personnel au répertoire **`Enseignement`**.