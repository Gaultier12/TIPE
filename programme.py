
import pylab as py

from random import randint

import numpy as np


def tableau(lignes, colonnes):
	return np.zeros(shape=(lignes, colonnes))


def rempli_al(lignes, colonnes):
	tableau = np.zeros(shape=(lignes, colonnes))
	for i in range(tableau.shape[0]):
		for j in range(tableau.shape[1]):
			if randint(0,1) == 0:
				tableau[i,j] = randint(0,30) #la hauteur maximale moyenne est de 30m
	return tableau

def rempli_avec_coherence(tableau, n): # n est le nombre de cases que l'on prend autour pour faire la moyenne
	for i in range(np.shape(tableau)[0] - n):
		for j in range(np.shape(tableau)[1] - n):

			cases_autour = tableau[i-n:i+n, j-n:j+n]
			
			somme = 0
			nombre_de_vrais_chiffres = 0 #on fait ça à cause des NaN
			for k in range(np.shape(cases_autour)[0]):
				for l in range(np.shape(cases_autour)[1]):
					if not np.isnan(cases_autour[k,l]):
						somme += cases_autour[k,l]
						nombre_de_vrais_chiffres += 1
			
			if nombre_de_vrais_chiffres == 0:
				nombre_de_vrais_chiffres = 1 #on met +1 pour éviter de diviser par 0 pour la première case
			moyenne = somme // (nombre_de_vrais_chiffres)
			
			# valeur = randint(moyenne - 3, moyenne)
			
			# if valeur < 0:
				# valeur = 0
			
			valeur = randint(moyenne -2, moyenne )

			tableau[i,j] = valeur
	
	tableau = tableau[n:-n, n:-n]
	
	return(tableau)


def creer_une_pre_dune(tableau, intensite): #crée un arc de cercle, qui appliqué a la fonction rempli_avec_coherence, créera une dune un peu plus réaliste que ce qui avait été eu précédemment
	#intensité est la hauteur du croissant formé
	lignes, colonnes = np.shape(tableau)
		
	#coordonnées du centre du cercle et rayon
	centrex = lignes // 2
	centrey = 3 * colonnes // 4
	rayon = colonnes // 4
	
	i=0
	for i in range(lignes):
		for j in range(colonnes):
			if j < (5 * colonnes / 8): #permet de tronquer le cercle et de faire le croissant
				distance_au_centre_du_cercle = np.sqrt((centrex - i)**2 + (centrey - j)**2)
				if distance_au_centre_du_cercle > rayon - 2 and distance_au_centre_du_cercle < rayon + 2:
					tableau[i,j] = intensite
	return tableau



A = rempli_avec_coherence(creer_une_pre_dune(tableau(100, 100), 100), 1)
# A = rempli_avec_coherence(tableau(100,100), 2)
print(A)

min = np.min(A)
max = np.max(A)

A = A - min
#A = A / (max - min)

py.figure()
py.imshow(A, interpolation = 'nearest')
py.axis('off')
py.title('Vue de dessus')
py.show()

