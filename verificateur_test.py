import os
import unittest
import Ex2_dict as e2
# import Ex3_Renommer_plusieurs_fichiers as e3



# Données de test
DONNEES:list[dict] = [
    {"id": 0, "prenom": "Hélène", "nom": "Boucher", "solde": 8160},
    {"id": 1, "prenom": "Thérèse", "nom": "Tessier", "solde": 7038},
    {"id": 2, "prenom": "Benjamin", "nom": "Savard", "solde": 3163},
    {"id": 3, "prenom": "Jean", "nom": "Tremblay", "solde": 411},
    {"id": 41, "prenom": "Hugues", "nom": "Pelletier", "solde": 96},
]

class Test_ex2(unittest.TestCase):
    def test_obtenir_liste_noms(self):
        resultat = e2.obtenir_liste_noms(DONNEES)
        attendu = ["Hélène Boucher", "Thérèse Tessier", "Benjamin Savard", "Jean Tremblay", "Hugues Pelletier"]
        self.assertEqual(resultat, attendu)


    def test_obtenir_solde_moyen(self):
        resultat = e2.obtenir_solde_moyen(DONNEES)
        attendu = (8160 + 7038 + 3163 + 411 + 96) / 5
        self.assertEqual(resultat , attendu)


    def test_obtenir_stats(self):
        total_attendu = 8160 + 7038 + 3163 + 411 + 96
        moy_attendue = total_attendu / 5
        qt_attendue = 5

        total, moy, qt = e2.obtenir_stats(DONNEES)

        self.assertEqual( total , total_attendu)
        self.assertEqual( moy , moy_attendue)
        self.assertEqual( qt , qt_attendue)

# test_ex4_unittest.py

import os
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from io import StringIO
import Ex4_csv as e4



class TestEx4CSV(unittest.TestCase):
    def setUp(self):
        """Crée un fichier CSV temporaire pour les tests."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_path = Path(self.temp_dir.name)

        # Contenu CSV simulé
        self.csv_content = (
            "Poste;Compagnie;Ville;Expérience;Diplôme;Salaire\n"
            "Tech reseau;ABC;Montreal;2 ans;Dec;45000\n"
            "Admin sys;XYZ;Quebec;3 ans;Non déterminé;50000\n"
            "Support IT;DEF;Laval;1 an;AEC;38000\n"
        )

        # Création du fichier CSV
        self.csv_file = self.base_path / "emplois.csv"
        self.csv_file.write_text(self.csv_content, encoding="utf-8")

    def tearDown(self):
        """Nettoyage."""
        self.temp_dir.cleanup()

    def test_charger_csv(self):
        """Vérifie que le CSV est chargé correctement et sans les en-têtes."""
        lignes = e4.charger_csv(str(self.csv_file))

        self.assertEqual(len(lignes), 3)
        self.assertEqual(lignes[0][0], "Tech reseau")
        self.assertEqual(lignes[1][4], "Non déterminé")

    def test_filtrer_offres_par_diplome(self):
        """Vérifie que seules les offres Dec ou Non déterminé sont conservées."""
        lignes = e4.charger_csv(str(self.csv_file))
        filtrées = e4.filtrer_offres_par_diplome(lignes)

        self.assertEqual(len(filtrées), 2)
        self.assertEqual(filtrées[0][4], "Dec")
        self.assertEqual(filtrées[1][4], "Non déterminé")




if __name__ == "__main__" :
    os.system("cls") # vide console windows
    unittest.main(verbosity=2)