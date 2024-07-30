#Commandes du terminal pour mettre en route et éxécuter Python 
    #Ouvrir un terminal -> Python 
    #Quitter l'utilisation de Python -> exit()
#                                   **********
#Utilisation dans le shell ou dans VS
#Ex. dans le shell ->
    #Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
    #Type "help", "copyright", "credits" or "license" for more information.
    #>>> print ("Hello World !")
    # Hello World !
    #>>> (100 + 81) * 11
    #1991
    #>>> exit()
    #PS C:\Users\floal>

#Ex. dans VS -> 
    #Dans VS, écrire print("Hello, world") et print (( 100 + 81 ) * 11 ) dans une nouvelle page
print ("Hello World !")
print ((100 + 81) * 11)
    #Nommer et sauvegarder le fichier 
    #Ouvrir l’invite de commande Windows. 
    #Ecrire "python" et le nom du fichier créé : 
    # -> si il est dans un dossier ne pas oublier de se mettre sur ledit dossier avec la commande cd 
    #(cd.. pour remonter les fichiers)
    #python helloworld.py 
    #Appuyez sur Entrée -> Affiche "Hello World !" dans le terminal

#**************************************************************************************************************

                                            #Les Variables 

#(A écrire en snake case - Les noms sont sensibles à la case - Ne peut pas commencer par un chiffre - 
# Pas d'accents ni caractères spéciaux)
    # Constituées de 3 éléments :
    # Nom
    # Type
    # Valeur
#Ex
    # livre = "Le seigneur des anneaux"
    #  Nom            Variable
    # print (livre)
    
# Pour modifier une variable il suffit de lui assigner une nouvelle valeur
# Ex
livre = "Le seigneur des anneaux"
print (livre)
livre = "Star War" #(Nouvelle valeur de la variable livre)
print (livre)

# Concatenation de variables dans une chaine de caractéres avec f-string
# La chaine de caractères doit etre précédée de f et les varables entre {}
# Ex
nom = "Dupont"
prenom = "Jean"
age = 30
print (f"Bonjour, je suis {prenom} {nom} et j'ai {age} ans. (Avec f-string)") 

# Sans f-string plus long, plus complexe et il ne faut rien oublier en ponctuation :
# Ex
nom = "Dupont"
prenom = "Jean"
age = 30
print("Bonjour, je m'appelle " + prenom +" "+ nom + " et j'ai" + " " + str(age) + " "+ "ans. (Sans f-string)")

                                    # Les types de données, les 4 types de données primitifs :

    # Les entiers (Inregers)
    # Les virgules flottantes (Float)
    # Les chaines de caractères (String)
    # Les booléen

# Attention Python prend des points à la place des virgules
# Python déduit de la variable son type. La fonction type() determine le type de données d'une variable.
# Ex
print ("* Les types primitifs") #(Dans la console)
nombre = 2
phrase = ("Hello World")
booleen = True
type (nombre)
# <class 'int'>
type (phrase)
# <class 'str'>
type (booleen)
# <class 'bool'>

                                                    # Les listes 

# * Création - Elles sont créées avec [] et les éléments sont séparés par , . Ne pas oublier "" pour les strings. 
# Ex
plateforme_sociale = ["Facebook", "IG", "Twitter"]
# => ["Facebook", "IG", "Linkedin"]
    
# Accéder - Pour acceder à un élément de la liste => nom_de_liste[N°Element]
# Ex
plateforme_sociale[1] 
# => "IG"
# Sens inverse avec les négatives
# Ex
plateforme_sociale[-1] 
# => "Twitter"
# On peut aussi l'utiliser pour les chaines de caractères
# Ex
language = "Python"  
language[2] 
# => "T"

# Modification - Remplacer 
# Utiliser l'indice de la place où la donnée doit être remplacée et y affecter une nouvelle valeure avec =
# Ex
plateforme_sociale[1] = "Linkedin" 
print(plateforme_sociale)
# => ["Facebook", "Linkedin", "Twitter"]

# Ajouter
# Pour ajouter, utiliser la methode -> .append()
# Ex
plateforme_sociale.append("TikTok") 
print(plateforme_sociale)  
# => ["Facebook", "Linkedin", "Twitter", "TikTok"]

# Retirer -> .remove'() - .remove() retire seulement la 1ere instance du terme saisi
# Ex
plateforme_sociale.remove("TikTok") 
print(plateforme_sociale) 
# => ["Facebook", "Linkedin", "Twitter"]

# Longueur d'une liste - Tenter d'acceder à un 
# index supérieur ou égal à la taille de la liste provoquera l'erreur -(IndexError)- car n'éxiste pas
# Ex  
len(plateforme_sociale) 
# => 3

# Trier -> .sort()
# Ex
plateforme_sociale.sort() 
print(plateforme_sociale) 
# => ["Facebook", "IG", "Linkedin"]

# Il existe beaucoup d'autres methodes à utiliser avec les listes :
    # extend() -> ajoute plusieurs éléments à la fin de la liste 
    # insert() -> insère un élément à une position donnée dans la liste
    # pop() -> supprime et renvoie lélément à une position donnée de la liste, ou le dernier élément si aucun indice n'est spécifié
    # index() -> renvoie à la 1ere occurence de lélément spécifié
    # count() -> renvoie le nombre d'occurences de lélément spécifié dans la liste
    # reverse() -> inverse l'ordre des éléments de la liste

                                                    # Les crochets
# Pour créer une liste vide
# Ex
ma_liste = []
print(ma_liste)
# => []

# Pour créer une liste d'éléments 
#Ex
ma_liste = ['a', 'b', 'c', 'd']
print(ma_liste)
# =>['a', 'b', 'c', 'd']

# Acceder à un élément suivant son index
# Ex
print(ma_liste[2])
# => c

# Modifier un élément via son index - Attention à ce que l'index existe sinon on aura IndexError
# Ex
ma_liste[2] = 'z'
print(ma_liste)
# => ['a', 'b', 'z', 'd']

# Ajouter un élément 
# Ex
ma_liste.append('e')
print(ma_liste)
# => ['a', 'b', 'z', 'd', 'e']

# Supprimer un élément avec remove - Supprime l'élément entre parenthèses
# Ex
ma_liste.remove('z')
print(ma_liste)
# => ['a', 'b', 'd', 'e']

# Supprimer un élément avec del - Supprime l'élément via son index
# Ex
del ma_liste[0]
print (ma_liste)
# => ['b', 'd', 'e']

# A noter que les chaines de caractères ont aussi des index sur lesquels il est possible de travailler en utillisant les mêmes méthodes

                                                    # Les tupples 

# Autres structure de liste utilisant les () plutôt que les [] - La plupart des propriétés sont similaires aux listes normales
# La différence est que les listes sont modifiables et les tupples immuables ( Non modifiables après création)

# Créer un tuple 
# Ex
mon_tuple = (1, 2, 3, 4)
print(mon_tuple)
# => (1, 2, 3, 4)

# Récuperer un élément
# Ex
print(mon_tuple[2])
# => 3

# On ne peut pas modifier un tuple -> mon_tuple[2] = 5 => error : 'tuple does not support item assignement'
# Cependant on peut créer un nouveau tuple en le concaténant 2 tuple existant
# Ex
mon_tuple_bis = ('cinq', 'six')
mon_nouveau_tuple = mon_tuple + mon_tuple_bis
print(mon_nouveau_tuple)
# => (1, 2, 3, 4, 'cinq', 'six')

# Trouver un élément dans une liste avec in qui retourne true ou false
# Ex
nombres = [1,2,3,4,5]
5 in nombres
# => True
8 in nombres
# => False
                    
                                                        # Les dictionnaires

# Structure de données enregistrées dans des paires clés-valeurs
# Ex : "responsable de campagne" : "Jeanne d'Arc"
#               Clé                     Valeur
# Les dictionnaires sont indiqués par des {}, il y a : entre la clé et la valeur et , à la fin

# Création d'un dictionnaire 
# Ex
nouvelle_campagne =  {
    "responsable_de_campagne" : "Jeanne d'Arc",
    "nom_de_campagne" : "Campagne nous aimons les chats",
    "date_de_debut" : "01-01-2020",
    "influenceurs_important" : ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"],
}
# => >>> ( En attente d'instructions )

# Parcourir un dictionnaire
#Ex
for i in nouvelle_campagne.items() : 
    print (i)
# => >>>
# ('responsable_de_campagne', "Jeanne d'Arc")
# ('nom_de_campagne', 'Campagne nous aimons les chats')
# ('date_de_debut', '01-01-2020')
# ('influenceurs_important', ['@MonAmourDeChien', '@MeilleuresFriandisesPourChiens'])

# Autre possibilité pour parcourir un dictionnaire : 
# Ex
for cle,valeur in nouvelle_campagne.items() :
    print("L'élément de clé", cle, "vaut", valeur)
# => >>>
# L'élément de clé responsable_de_campagne vaut Jeanne d'Arc
# L'élément de clé nom_de_campagne vaut Campagne nous aimons les chats
# L'élément de clé date_de_debut vaut 01-01-2020
# L'élément de clé influenceurs_important vaut ['@MonAmourDeChien', '@MeilleuresFriandisesPourChiens']

# Accéder à une valeur via la clé :
# Ex
nouvelle_campagne["responsable_de_campagne"]
# => "Jeanne d'Arc"

# Ajouter une clé-valeur - Si elle n'éxiste pas, il suffit d'ajouter une nouvelle clé dans le dictionnaire existant
# Ex
nouvelle_campagne["date_de_fin"] = " 31 Décembre"
for i in nouvelle_campagne.items() : print (i)
# => 
# ('responsable_de_campagne', "Jeanne d'Arc")
# ('nom_de_campagne', 'Campagne nous aimons les chats')
# ('date_de_debut', '01-01-2020')
# ('influenceurs_important', ['@MonAmourDeChien', '@MeilleuresFriandisesPourChiens'])
# ('date_de_fin', '31 Décembre')

# Ajouter une clé-valeur - Si la clé existe déjà l'ancienne valeur sera écrasée par la nouvelle valeur
# Ex
nouvelle_campagne["date_de_debut"] = " 1er Janvier"
for i in nouvelle_campagne.items() : print (i)
# =>
# ('responsable_de_campagne', "Jeanne d'Arc")
# ('nom_de_campagne', 'Campagne nous aimons les chats')
# ('date_de_debut', '1er janvier')
#('influenceurs_important', ['@MonAmourDeChien', '@MeilleuresFriandisesPourChiens'])
# ('date_de_fin', '31 Décembre')

# Supprimer une paire clé-valeur - Avec le mot clé 'del
# Ex
del nouvelle_campagne["responsable_de_campagne"]
print (nouvelle_campagne)
# => 
# {'nom_de_campagne': 'Campagne nous aimons les chats', 
# 'date_de_debut': '01-01-2020', 
# 'influenceurs_important': ['@MonAmourDeChien', '@MeilleuresFriandisesPourChiens']}

# Vérifier l'existance d'une clé spécifique - On utilise le mot-clé 'in'. Spécifié la clé recherché + in + nom de la variable du 
# dictionnaire éxaminé. Le résultat renvoie un booléen qui indique si la clé est dans ce dictionnaire
# Ex
"nom_de_campagne" in nouvelle_campagne
# => True

# Autres methodes couramment utilisées pour manipuler les dictionnaires :
# keys() -> ​​Retourne une vue sur les clés du dictionnaire -> nom_du_dictionnaire.keys()
# values() -> Retourne une vue sur les valeurs du dictionnaire -> nom_du_dictionnaire.values()
# items() -> Retourne une vue sur les couples (clé, valeur) du dictionnaire -> nom_du_dictionnaire.items()
# get(clé) -> Retourne la valeur associée à la clé spécifiée. Si la clé n'est pas présente dans le dictionnaire, 
# retourne la valeur None -> nom_du_dictionnaire.get(clés)
# pop(clé) -> Supprime la clé spécifiée et retourne la valeur associée. Si la clé n'est pas présente dans le dictionnaire, 
# retourne la valeur None -> nom_du_dictionnaire.pop(clés)
# clear() -> Supprime tous les éléments du dictionnaire -> nom_du_dictionnaire.clear()