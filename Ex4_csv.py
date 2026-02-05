import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez le module csv



def charger_csv(p_chemin_fichier: str) -> list[list[str]]:
    """
    Ouvre un fichier CSV et retourne toutes les lignes sous forme de liste,
    en ignorant la ligne d'en-têtes.
    """
    # Créez une variable "lignes" qui est une liste de listes
    # ouvrir le p_chemin_fichier en mode lecture
        # crée un lecteur de csv
        # sauter les en-têtes
        # pour chaque ligne du lecteur
        # ajouter la ligne à la variable  "lignes"
    #retourner  "lignes"


def filtrer_offres_par_diplome(p_lignes: list[list[str]]) -> list[list[str]]:
    """
    Retourne uniquement les lignes où le diplôme (index 4)
    est 'Dec' ou 'Non déterminé'.
    """
    # Créez une variable "offre" qui est une liste de listes
    # Passé à travaers p_lignes
             # ajouté toutes les offres avec "Dec" ou "Non déterminé" comme Diplôme requis




def afficher_offres(p_lignes: list[list[str]]) -> None:
    """Affiche les lignes d'offres filtrées."""




if __name__ == "__main__":
    
    # Nous avons des offres de stages and le fichier "Ex4 Emplois Reseautique.csv"
    # Faites un petit script qui ouvre le fichier csv en mode lecture et qui affiche uniquement les offres ou la demande de Diplôme a la valeur 'Dec' ou 'Non déterminé'
    
    # Regardez le contenu du fichier "Ex4 Emplois Reseautique.csv"
    #     Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
    #             Poste;Compagnie;Ville;Expérience;Diplôme;Salaire
    #     Certains champs ont la valeur "Non déterminé"


    fichier_a_lire = os.path.join("csvs", "Ex4 Emplois Reseautique.csv")
    # Q1
    # Commencez par complètez la fonction "charger_csv"
    # Appelez-là et capturer le retour. Cela vous donne toutes les données dans le csv.

    # Q2
    # Complètez "filtrer_offres_par_diplome" et appelez la fonction. capturez le retour

    # Q3
    # finalement complèter affichier_offres, qui va simplement imprimer les offres passer en paramètre.
    # Appelez la fonction et passé-lui le résultat de "filtrer_offres_par_diplome"







