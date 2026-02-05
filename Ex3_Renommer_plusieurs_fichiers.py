# importez os
import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.



def renommer_fichiers(p_répertoire:str) -> None:
    """Renome tous les fichiers dans le répertoire passé en paramètre.
    Passe de  '{sujet} _ {cours} _ {numéro}.mp4' à '{numéro}-{sujet}-{cours}.mp4'"""
    # # allez dans le dossier passé en paramètre (avec os.chdir())
    # # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
        # # utilisez os.path.splitext pour obtenir le filename et l'extension
        # # utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
        # # utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
        # # en plus utilisez du slicing et zfill pour remplir le numéro de sorte que #1 deviendra 01
        # # créez un nouveau str avec le nouveau nom de fichier
        #   utliser os.rename pour renommer le fichier


if __name__ == "__main__" :
    # Les videos dans le réperoire "Ex3 Videos" sont mal nommées.
    # Elles sont sous le fomat "{sujet} _ {cours} _ {numéro}.mp4"
    # Alors qu'on voudrait le format : "{numéro}-{sujet}-{cours}.mp4"
    # Donc   "Conditionals and Booleans _ Python _ #6.mp4" devra devenir "06-Conditionals and Booleans-Python.mp4"
    # Complèter la fonction renommer_fichiers en suivant le pseudo-code donnée
    # NOTE : Si vous faites une erreur lors de l'exécution, vous pouvez "discard" les changements dans github desktop.
    nom_répertoire = "Ex3 Videos"
    renommer_fichiers(nom_répertoire)
