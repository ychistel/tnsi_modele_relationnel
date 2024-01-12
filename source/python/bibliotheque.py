from csv import DictWriter

biblio = [\
         {'titre' : '1984',\
           'nom_auteur' : 'Orwell', \
           'prénom_auteur' : 'George', \
           'naissance_auteur' : 1903, \
           'langue' : 'anglais',\
           'année_publication' : 1949,\
           'genre' : ['totalitarisme', 'science-fiction', 'anticipation', 'dystopie']
          },\
         {'titre' : 'Dune',\
           'nom_auteur' : 'Herbert', \
           'prénom_auteur' : 'Frank', \
           'naissance_auteur' : 1920, \
           'langue' : 'anglais',\
           'année_publication' : 1965,\
           'genre' : ['science-fiction', 'anticipation']
          },\
         {'titre' : 'Fondation',\
           'nom_auteur' : 'Asimov', \
           'prénom_auteur' : 'Isaac', \
           'naissance_auteur' : 1920, \
           'langue' : 'anglais',\
           'année_publication' : 1951,\
           'genre' : ['science-fiction', 'économie']
          },\
         {'titre' : 'Le meilleur des mondes',\
           'nom_auteur' : 'Huxley', \
           'prénom_auteur' : 'Aldous', \
           'naissance_auteur' : 1894, \
           'langue' : 'anglais',\
           'année_publication' : 1931,\
           'genre' : ['totalitarisme', 'science-fiction', 'dystopie']
          },\
         {'titre' : 'Farenheit 451',\
           'nom_auteur' : 'Bradbury', \
           'prénom_auteur' : 'Ray', \
           'naissance_auteur' : 1920, \
           'langue' : 'anglais',\
           'année_publication' : 1953,\
           'genre' : ['science-fiction', 'dystopie']
          },\
         {'titre' : 'Ubik',\
           'nom_auteur' : 'K Dick', \
           'prénom_auteur' : 'Philip', \
           'naissance_auteur' : 1928, \
           'langue' : 'anglais',\
           'année_publication' : 1969,\
           'genre' : ['science-fiction', 'anticipation']
          },\
         {'titre' : 'Chroniques martiennes',\
           'nom_auteur' : 'Bradbury', \
           'prénom_auteur' : 'Ray', \
           'naissance_auteur' : 1920, \
           'langue' : 'anglais',\
           'année_publication' : 1950,\
           'genre' : ['science-fiction', 'anticipation']
          },\
         {'titre' : 'La nuit des temps',\
           'nom_auteur' : 'Barjavel', \
           'prénom_auteur' : 'René', \
           'naissance_auteur' : 1911, \
           'langue' : 'français',\
           'année_publication' : 1968,\
           'genre' : ['science-fiction', 'tragédie']
          },\
         {'titre' : 'Blade runner',\
           'nom_auteur' : 'K Dick', \
           'prénom_auteur' : 'Philip', \
           'naissance_auteur' : 1928, \
           'langue' : 'anglais',\
           'année_publication' : 1968,\
           'genre' : ['intelligence artificielle', 'science-fiction']
          },\
         {'titre' : 'Les robots',\
           'nom_auteur' : 'Asimov', \
           'prénom_auteur' : 'Isaac', \
           'naissance_auteur' : 1920, \
           'langue' : 'anglais',\
           'année_publication' : 1950,\
           'genre' : ['science-fiction', 'intelligence artificielle']
          },\
         {'titre' : 'La planète des singes',\
           'nom_auteur' : 'Boulle', \
           'prénom_auteur' : 'Pierre', \
           'naissance_auteur' : 1912, \
           'langue' : 'français',\
           'année_publication' : 1963,\
           'genre' : ['science-fiction', 'dystopie']
          },\
         {'titre' : 'Ravage',\
           'nom_auteur' : 'Barjavel', \
           'prénom_auteur' : 'René', \
           'naissance_auteur' : 1911, \
           'langue' : 'français',\
           'année_publication' : 1943,\
           'genre' : ['dystopie', 'uchronie']
          },\
         {'titre' : 'Le monde des A',\
           'nom_auteur' : 'Van Vogt', \
           'prénom_auteur' : 'Alfred Elton', \
           'naissance_auteur' : 1912, \
           'langue' : 'anglais',\
           'année_publication' : 1945,\
           'genre' : ['science-fiction', 'intelligence artificielle']
          },\
         {'titre' : 'La fin de l\'éternité',\
           'nom_auteur' : 'Asimov', \
           'prénom_auteur' : 'Isaac', \
           'naissance_auteur' : 1920, \
           'langue' : 'anglais',\
           'année_publication' : 1955,\
           'genre' : ['science-fiction', 'voyage dans le temps']
          },\
         {'titre' : 'De la terre à la lune',\
           'nom_auteur' : 'Verne', \
           'prénom_auteur' : 'Jules', \
           'naissance_auteur' : 1828, \
           'langue' : 'français',\
           'année_publication' : 1865,\
           'genre' : ['science-fiction', 'aventure']
          },\
         {'titre' : 'La machine à explorer le temps',\
           'nom_auteur' : 'Wells', \
           'prénom_auteur' : 'Herbert George', \
           'naissance_auteur' : 1866, \
           'langue' : 'anglais',\
           'année_publication' : 1895,\
           'genre' : ['science-fiction', 'voyage dans le temps']
          }
        ]

def export_csv(table):
    attributs = table[0].keys()
    with open("../csv/table.csv",mode='w',encoding='utf8',newline='') as f:
        data = DictWriter(f,attributs,delimiter=';')
        #data.writeheader()
        data.writerows(table)
            