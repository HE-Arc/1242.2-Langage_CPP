---
title: "Page Template"
type: docs
weight: 10
draft: false
---
# Titre de la page
{{<teaservideo "https://benoitlecallennec-hes.github.io/template_website_course/videos/Chapter6_final.mp4">}}
Ceci est une "teaser video" : une vidéo qui se lance automatiquement quand on arrive sur la page, muette, et sans contrôles visibles.

## Titre de niveau 2

### Titre de niveau 3

#### Titre de niveau 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut gravida lorem.

{{< slide >}}
## Titre de niveau 2

### Titre de niveau 3

#### Titre de niveau 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut gravida lorem.
{{< /slide >}}

## Formattage du texte
*Ceci est un texte en italique.*

**Ceci est un texte en gras.**

***Ceci est un texte en gras italique.***

> Ceci est une citation.
> 
> Elle peut être sur plusieurs lignes. Elle peut être sur plusieurs lignes. Elle peut être sur plusieurs lignes. Elle peut être sur plusieurs lignes.
>

{{< slide >}}
## Formattage du texte
*Ceci est un texte en italique.*

**Ceci est un texte en gras.**

***Ceci est un texte en gras italique.***

> Ceci est une citation.
> 
> Elle peut être sur plusieurs lignes. Elle peut être sur plusieurs lignes. Elle peut être sur plusieurs lignes. Elle peut être sur plusieurs lignes.
>
{{< /slide >}}

## Emojis
📌 Une note qui demande à être approfondie

📚 Une référence à étudier pour aller plus loin

⇒ Implication de la ligne précédente

{{< slide >}}
## Emojis
📌 Une note qui demande à être approfondie

📚 Une référence à étudier pour aller plus loin

⇒ Implication de la ligne précédente
{{< /slide >}}

## Hints
### Bonne pratique
**Code**
```
{{</* bonne_pratique */>}}
Il faut faire ceci, c'est une bonne pratique.
{{</* /bonne_pratique */>}}
```
**Affichage**
{{<bonne_pratique>}}
Il faut faire ceci, c'est une bonne pratique.
{{</bonne_pratique>}}

### À noter
**Code**
```
{{</* a_noter */>}}
Il faut noter ceci !!!
{{</* /a_noter */>}}
```
**Affichage**
{{<a_noter>}}
Il faut noter ceci !!!
{{</a_noter>}}

### Pour aller plus loin
**Code**
```
{{</* aller_plus_loin */>}}
Approndissement optionel de la notion.
{{</* /aller_plus_loin */>}}
```
**Affichage**
{{<aller_plus_loin>}}
Si vous souhaitez approfondir cette notion...
{{</aller_plus_loin>}}

### Notion avancée
**Code**
```
{{</* notion_avancee */>}}
Il s'agit d'une notion avancée.
{{</* /notion_avancee */>}}
```
**Affichage**
{{<notion_avancee>}}
Il s'agit d'une notion avancée.
{{</notion_avancee>}}

### Attention
**Code**
```
{{</* attention */>}}
Il faut faire attention à ce point en particulier.
{{</* /attention */>}}
```
**Affichage**
{{<attention>}}
Il faut faire attention à ce point en particulier.
{{</attention>}}

### À éviter
**Code**
```
{{</* a_eviter */>}}
Il ne faut surtout pas faire ceci !!!
{{</* /a_eviter */>}}
```
**Affichage**
{{<a_eviter>}}
Il ne faut surtout pas faire ceci !!!
{{</a_eviter>}}

### À faire
**Code**
```
{{</* a_faire */>}}
- Serie 1
- TP 1 : parties 1, 2 et 3
- TP 2 : parties 1, 2 et 3
{{</* /a_faire */>}}
```
**Affichage**
{{<a_faire>}}
- Serie 1
- TP 1 : parties 1, 2 et 3
- TP 2 : parties 1, 2 et 3
{{</a_faire>}}

{{< slide >}}
## Hints
{{<bonne_pratique>}}
Il faut faire ceci, c'est une bonne pratique.
{{</bonne_pratique>}}

{{<a_noter>}}
Il faut noter ceci !!!
{{</a_noter>}}

{{<aller_plus_loin>}}
Si vous souhaitez approfondir cette notion...
{{</aller_plus_loin>}}

{{<notion_avancee>}}
Il s'agit d'une notion avancée.
{{</notion_avancee>}}
{{< /slide >}}

{{< slide >}}
## Hints
{{<attention>}}
Il faut faire attention à ce point en particulier.
{{</attention>}}

{{<a_eviter>}}
Il ne faut surtout pas faire ceci !!!
{{</a_eviter>}}

{{<a_faire>}}
- Serie 1
- TP 1 : parties 1, 2 et 3
- TP 2 : parties 1, 2 et 3
{{</a_faire>}}
{{< /slide >}}

## Images
### Avec une image dans le répertoire local ***static/images***
**Code**
```
{{</* figure src="/images/AE_Fork.png#center" width="100%" caption="Légenge" */>}}
```

**Affichage**
{{< figure src="images/AE_Fork.png#center" width="100%" caption="Un screenshot">}}

### Avec une image sur le web
{{< figure src="https://www.he-arc.ch/wp-content/uploads/2021/09/ARCLogoLumineux.jpg" width="100%">}}

{{< slide >}}
## Images
### Avec une image

{{< figure src="images/AE_Fork.png#center" width="40%" caption="Un screenshot">}}

{{< figure src="https://www.he-arc.ch/wp-content/uploads/2021/09/ARCLogoLumineux.jpg" width="30%">}}

{{< /slide >}}

## Boutons
{{< button href="https://www.he-arc.ch" >}}HE-Arc{{< /button >}}

{{< button href="https://www.he-arc.ch" >}}HE-Arc{{< /button >}}

{{< button href="https://www.he-arc.ch" >}}HE-Arc{{< /button >}}

## Tabs
{{< tabs "id" >}}
{{< tab "MacOS" >}} MacOS Content {{< /tab >}}
{{< tab "Linux" >}} Linux Content {{< /tab >}}
{{< tab "Windows" >}} Windows Content {{< /tab >}}
{{< /tabs >}}

## UML Diagrams (avec PlantUML)
Le code PlantUML doit être placé entre les balises ***{{</* plantuml */>}}*** et ***{{</* /plantuml */>}}***.

### Exemple de diagrammes PlantUML
{{<attention>}}
Les id des graphes PlantUML doivent être différents.
{{</attention>}}

**Code**
```
{{</* plantuml id="eg1" */>}}
@startuml
skin rose
skinparam classAttributeIconSize 0
class Hero {
   - strength : int
   - agility : int
   - intelligence : int
   - hp : double
   - name : std::string

   + show() : void
   + interact(const Hero &) : void
   + getAgility(): int
}
@enduml
{{</* /plantuml */>}}
```
**Affichage**

{{< plantuml id="eg1">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
class Hero {
   - strength : int
   - agility : int
   - intelligence : int
   - hp : double
   - name : std::string

   + show() : void
   + interact(const Hero &) : void
   + getAgility(): int
}
@enduml
{{< /plantuml >}}

{{<slide >}}
## PlantUML Diagrams
{{< plantuml id="eg1">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
class Hero {
   - strength : int
   - agility : int
   - intelligence : int
   - hp : double
   - name : std::string

   + show() : void
   + interact(const Hero &) : void
   + getAgility(): int
}
@enduml
{{< /plantuml >}}
{{< /slide >}}

## LaTeX

Il suffit de mettre le code LaTeX entre les balises ***{{</* katex */>}}*** et ***{{</* /katex */>}}***.

### Quelques exemples
**Code**
```
{{</* katex */>}}\alpha \beta \gamma \rho \delta \epsilon{{</* /katex */>}}
```
**Affichage**

{{< katex >}}\alpha \beta \gamma \rho \delta \epsilon{{< /katex >}}
<br><br>

**Code**
```
{{</* katex */>}}\Alpha \Beta \Gamma \Rho \Delta \Epsilon{{</* /katex */>}}
``` 
**Affichage**

{{< katex >}}\Alpha \Beta \Gamma \Rho \Delta \Epsilon{{< /katex >}}
<br><br>

**Code**
```
{{</* katex */>}}\times \otimes \oplus \cup \cap{{</* /katex */>}}
```
**Affichage**

{{< katex >}} \times \otimes \oplus \cup \cap{{< /katex >}}
<br><br>

**Code**
```
{{</* katex */>}}\sum_{i=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}}{{</* /katex */>}}
```
**Affichage**

{{< katex >}} \sum_{i=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}} {{< /katex >}}
<br><br>

**Code**
```
{{</* katex */>}}\sum_{n=1}^{\infty} 2^{-n} = 1{{</* /katex */>}}
```
**Affichage**

{{< katex >}}\sum_{n=1}^{\infty} 2^{-n} = 1{{< /katex >}}
<br><br>

**Code**
```
{{</* katex */>}}
\begin{pmatrix}
1 & 2 & 3\\
a & b & c
\end{pmatrix}
{{</* /katex */>}}
```
**Affichage**
{{< katex >}}
\begin{pmatrix}
1 & 2 & 3\\
a & b & c
\end{pmatrix}
{{< /katex >}}
<br><br>

On peut mettre des formules LaTeX dans le texte : {{<katex>}} x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} {{</katex>}}.

On peut aussi mettre des équations sur des lignes séparées :

{{<katex>}} x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} {{</katex>}}

## Code

### Directement dans le texte
On peut mettre du code directement dans le texte : **`int i = 0;`**.

```cpp
int i = 100;
char c = static_cast<char>(i); // int -> char  

float f = 100.0f;
i = static_cast<int>(f); // float -> int
 
class Base{};
class Deri : public Base{};
Deri  *d = new Deri;
Base *b = static_cast<Base*>(d); // Deri* -> Base*
```

On peut aussi mettre du code avec des lignes en surbrillance :
{{< highlight csharp "linenos=table,hl_lines=8 14">}}
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloWorld : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
{{< / highlight >}}

{{< slide class="code-medium" >}}
## Code
### Dans le texte
Sur une même ligne `int i = 0;`, ou sur plusieurs :
```c++
int i = 100;
char c = static_cast<char>(i); // int -> char  
float f = 100.0f;
i = static_cast<int>(f); // float -> int
class Base{};
class Deri : public Base{};
Deri  *d = new Deri;
Base *b = static_cast<Base*>(d); // Deri* -> Base*
```
{{< /slide >}}

### Avec un fichier de snippet
On peut inclure des snippets de code depuis des fichiers sources.

**Code**
<!-- We must use inline code to prevent the preprocessor from interpreting the line -->
`<!-- SNIPPET:INCLUDE source_file=hello.c id=hello_world -->`
  
Ensuite, il faut exécuter le préprocesseur Hugo pour inclure le code :
```powerhell
python .\tools\hugo_preprocessor.py
```

**Affichage**
<!-- SNIPPET:BEGIN source_file=hello.c id=hello_world -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```c
int main(void)
{
	printf("Hello World\n");

	return 0;
}
```
<!-- SNIPPET:END -->
<br><br>

On peut aussi nettoyer le code automatiquement inclus et revenir à la balise de snippet d'origine grâce à la commande suivante :
```powerhell
python .\tools\hugo_preprocessor.py clean
```

## Listes

Voici une liste non-ordonnée :
- élément 1;
- élément 2;
- élément 3.

Voici une liste ordonnée :
1. élément 1;
2. élément 2;
3. élément 3.

## Référence
Voici un texte avec une référence listée en bas de page [^hearc].

## Vidéos
### Youtube
{{<youtube kWLO4ISf3bA>}}
{{<attention>}}
Il faut prendre l'id uniquement. En particulier, il ne faut pas mettre les guillemets.
{{</attention>}}

### Playlist Youtube
{{<youtubelist PLc3qvmVjY5p-x4EzSS50FCk6qzXG9JEHP>}}
{{<attention>}}
Il faut prendre l'id uniquement. En particulier, il ne faut pas mettre les guillemets.
{{</attention>}}

### Vidéo MP4 hébergée ailleurs
{{<video "https://benoitlecallennec-hes.github.io/template_website_course/videos/Chapter6_final.mp4">}}


## PDFs
### Avec un PDF dans le répertoire local ***static/pdfs***
**Code**
```
{{</*pdf src="/pdfs/n4849.pdf"*/>}}
```
**Affichage**
{{<pdf src="/pdfs/n4849.pdf">}}

### Avec un PDF sur le web
**Code**
```
{{</*pdf src="https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3088.pdf"*/>}}
```
**Affichage**
{{<pdf src="https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3088.pdf">}}

## Reveal.js Slides
{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/00_Organisation.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/00_Organisation.html?print-pdf)

## Colonnes
{{< columns >}} <!-- begin columns block -->
# Left Content
Lorem markdownum insigne...

<---> <!-- magic separator, between columns -->

# Mid Content
Lorem markdownum insigne...

<---> <!-- magic separator, between columns -->

# Right Content
Lorem markdownum insigne...
{{< /columns >}}


## Barre de progression
{{<progress_bar 0 250>}}

{{<progress_bar 125 250>}}

{{<progress_bar 250 250>}}

## Références
[^hearc]: [HE-Arc](https://www.he-arc.ch/)


