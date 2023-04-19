# SQLITE : CRÉATION DE LA TABLE

import sqlite3

# connexion = "albums2.db"
# executer / curseur
# commit
# fermer

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

# curseur.execute("""CREATE TABLE artiste (
#     artiste_id INTEGER NOT NULL PRIMARY KEY,
#     nom VARCHAR);""")
curseur.execute(
    # """  INSERT INTO artiste (nom) VALUES ("Michael Jackson");"""
    """INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "Thriller", 1983);"""
)

connexion.commit()
connexion.close()
