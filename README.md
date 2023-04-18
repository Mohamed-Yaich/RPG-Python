# Empire-Of-Chaos

## Histoire du jeu

Légende de l'Eternel : Selon la légende, il y a de nombreux univers, chacun régi par un élément distinct : l'eau, le feu, la terre et l'air. Ces univers sont gouvernés par des êtres puissants comme des monstres et d'autres créatures mystérieuses. Chaque univers est habité par un maître qui détient une pierre et qui a le pouvoir de contrôler leur univers respectif, mais sont également liés les uns aux autres par une force mystérieuse connue sous le nom de "Pierres Anciennes".

Il existe un cinquième univers, caché et sombre, connu sous le nom de "Ténèbres". Cet univers est régi par Ouroboros, le plus puissant de tous. Selon la légende, si le Boss ultime parvient à réunir les Pierres Eternelles de chaque univers, il pourra invoquer une force destructrice capable de mettre fin au monde tel que nous le connaissons.

Pour protéger le monde, un héros courageux s'est lancé dans une quête pour rassembler les Pierres Anciennes avant Ouroboros. Chaque pierre confère au héros un pouvoir spécial lié à l'univers d'où elle provient, et pour battre Ouroboros le seul moyen de le vaincre et d'utiliser les 4 pierres qui, assemblées, deviennent la pierre de lumière et ainsi sauver le monde.

## But Du Jeu

Rassembler les 4 pierres des 4 boss pour avoir la pierre de lumière et vaincre Ouroboros le boss final

# DEV

## Créer un dossier d'environement

Un dossier d'environement va contenir toute les lib utile au projet sans avoir a les installer sur l'ordinateur

Pour créer le dossier d'environement virtuel, tapez dans le terminal :

```git
python3 -m venv + nom-du-dossier
```

si il y a un problème avec le dossier venv

```git
sudo apt install python3-venv
```

Ensuite pour installer des lib dans l'environnement virtuel, il faut l'activer avec la commande :

sous linux :

```git
. venv/bin/activate
```

sous Windows :

```git
source venv\Scripts\activate
```

Après avoir tapez la commande ci-dessus, nous voila dans l'environement virtuel pour installer les lib néssécaire au projet

Tapez la commande suivante toutes les lib :

```git
pip install -r reqs.txt
```

## Structure du code

```py

def start_game():
  return

def inventory():
  return

def Menu():
  # Afficher les options du menu
  # demander à l'utilisateur
  # en fonction du choix appeler une des 4 fonctions du dessous

def start_game():
  # afficher le contexte et le début de l'histoire
  # ask_name()
  # move()

def ask_name():
  # demander le nom
  return name

def load_game():
  # charger des datas en mémoire
  start_game()

def credits():
  # print afficher des infos sur la teams
  Menu()

def exit():
  # quitter le jeu

def move():
  # print les propositions de déplacement
  # recupérer le choix de l'utilisateur
  # En fonction du choix appeler une fonctionnalité

def fight():
  # présentation du combat
  # print propositions d'actions du joueur
  # en fonction du choix du joueurs appeler la fonction qui correspond
  # action de l'ennemis


def find_object():
  return

def event():
  return

```
