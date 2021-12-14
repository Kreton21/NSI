Nous sommes le 15 octobre 2021 et le repertoire Github du projet est cree.
La prochaine fois ou je vais reouvrir ce journal sera 2j avant la date de retour.
Mon frere de projet est Eliez et il est extremement motive pour ce projet.

# Jeudi 4 Novembre:
J'ai enfin de de la connexion internet pour pouvoir travailler sur le projet (Les montagnes Roumaines ne sont pas reputees pour leur 4G). On va se servir d'un site appele Repl.it pour collaborer sur le projet. On as compris le projet et a present on va pouvoir commencer a travailler dessus. Il est 16h07 et on va ecrire la premiere ligne de code.

Une demi-heure plus tard on avait un prototype fonctionel mais qui ne montrais pas les o et les # quand les les nombres etaient bien trouves ou bien placees. Une erreur survenait tres souvent quand on essait de modifier une variable globale au sein d'une fonction. Je pensait qu'une variable une fois declaree en tant que globale il ne faut pas la r'appeler au sein de la fonction pour la modifier:

global a 
def exemple():      = Erreur
    a+=1    

global a
def exemple():      = Ca marche
    global a
    a+=1

En effet une variable globale peut etre lue sans etre rappele mais pas modifee. 
Une heure plus tard tous les bugs on ete corrigees et le jeu est 100% fonctionel mais sans avoir lu la consigne on se rend compte que l'on as respecte aucune des consignes et le jeu n'est pas compatible avec les fonctions du poly. On doit alors tout refaire a 0.



Erreurs indentations fonction posistion () qui renvoie -2 tt le temps (Return a linterieur de la fonction)