# Cours Bool
## Intro
### Definition:
On appele booleen toute variable definie sur un ensemble a deux elements

* Exemple: {True,False} ou {0,1}
***

## I/ Operateurs de base
### 1) Negation

La negation est un operateur unaire. La sortie est le contraire de l'entree.

* La negation de a se note, |a, !a voir not a

Sa table de verite est donee par: 
| a | !a |
| ------------- | ------------- |
| 0  | 1  |
| 1  | 0  |

### 2) L'operateur ET

Et est un operateur *binaire* (il s'applique a deux booleans). Sa sortie vaut 1 si, et seulement si les deux entrees valent 1.
* La negation se note a ET b, a AND b, a X b voir a*b

Sa table de verite se note:
| a | b | a X b|
| ------------- | ------------- | ------------|
|0|0|0|
|1|0|0|
|0|1|0|
|1|1|1|

### 3) L'operateur OU
Ou est un operateur binaire. Sa sortie vaut 1 si, et seulement si l'une des entrees vaut 1.

* Ou se note a OU b, a+b, avb, a|b voir a || b
Sa table de verite se note:

| a | b | a OR b|
| ------------- | ------------- | ------------|
|0|0|0|
|1|0|1|
|0|1|1|
|1|1|1|
***

### 4) Regles de calcul
* ### Commutativite
   - a+b = b+a
   - axb = bxa
* ### Element neutre
   - a+0=0+a=a
   - ax1=1xa=a
* ### Distributivite
    - aX(b+c)=aXb+aXc
    - a+(bXc)=(a+b)X(a+c)
* ### Associativite
    - (a+b) + c = a+(b + c)
    - (ab)c = a(bc)
* ### Absorbtion
    - 0 X a = a X 0 = 0
    - 1 + a = 1
* ### Idempotence
    - a+a+a+a+a.....+a = a
    - aXaXaXaXa.....Xa = a
* ### Involution
    - NOT NOT a = a
* ### Tiers Exclus
    - a + NOT a = a
* ### Non contradiction
    - a NOT a = 0
* ### Loi de Morgan
    - NOT (a + b) = NOT a X NOT b 
    - NOT (a X b) = NOT a + NOT b
* ### Simplification 
    - a + NOT a b = a+b
    - a(NOT a + b)= ab
* ### Redondance
    - ab + NOT a c = ab+NOTa c + bc
___
