#Maxime Delacroix

import math 
import numpy as np

def centre_grav(list_des_grav):
	"""
	Pre: Demande une liste de tuples avec la masse et un tuple de la position
		 ([ (masse_1, (x_1, y_1)), (masse_2, (x_2, y_2)) ])
		 
	Post: Sort un tuple (x, y) du centre de gravité
		
	"""
	sum_masses = 0
	sum_x = 0
	sum_y = 0
	
	for i in range(0, len(list_des_grav)):
		masse, coord = list_des_grav[i]
		x, y = coord
		sum_masses += masse 			#Additione toutes les masses
		sum_x += masse*x				#Multiplie la masse par sa composante en x
		sum_y += masse*y				#Multiplie la masse par sa composante en y
		
	centre_grav_x = sum_x / sum_masses	#Calcul le centre de gravité en x
	centre_grav_y = sum_y / sum_masses	#Calcul le centre de gravité en y
	
	centre_grav = (centre_grav_x, centre_grav_y) 
	return centre_grav
	
#Angles
tp = np.arange(0,10,0.001)		#Creer une liste de 0 a 10 avec des step de 0.001
a = np.empty_like(tp)			#Creer une liste de vide meme longueur que tp
v = np.empty_like(tp)			#Creer une liste de vide meme longueur que tp
theta = np.empty_like(tp)		#Creer une liste de vide meme longueur que tp

#Energies
E_G = np.empty_like(tp)			#Creer une liste de vide meme longueur que tp
E_C = np.empty_like(tp)			#Creer une liste de vide meme longueur que tp
E_K = np.empty_like(tp)			#Creer une liste de vide meme longueur que tp
E_A = np.empty_like(tp)			#Creer une liste de vide meme longueur que tp
E_tot = np.empty_like(tp)		#Creer une liste de vide meme longueur que tp

#Information Grue:
#Masse des differentes composante de la grue:
	
m1 = 1.2									#Masse du flotteurs					
m2 = 1.1									#Masse du bras de la grue 
m3 = 0.200									#Masse de la charge (silo d'eolienne)

M = m1 + m2 + m3 							#Masse total

#Dimension:
l = 0.60									#Largeur du flotteur
h = 0.09									#Hauteur du flotteur
d = 0.7										#Distance max de la charge
							
hc = (M) / ( 1000 * (l**2) )				#Calcul la hauteur de flottaison
angle_chav = math.atan( (h-hc) / (l/2) )	#Calcul l'angle de chavirement
angle_soulev = math.atan((hc) / (l/2))		#Calcul de l'angle de soulevement 

grav = [ (m1+m2,(0.06, 0.112-hc)), (m3, (d, 0.40-hc)) ]

#Constante:

xG_0, yG_0 = centre_grav(grav)				#Centre de gravité initial
yP_0 = (-hc/2)								#Composante y du centre de poussé initial

g = 9.81									#Gravité
I = 0.16									#Inertie de la barge
C_am = 2									#Coefficient d'amortissement


Fg = g * M									#Poids de la grue
Fp = Fg										#Poussé d'archimede




#Simulation de l'oscillation de la barge

def simulation_oci():
	"""
	Simulation d'une ocsillation lorsque qu'une charge est porte à une distance d
	
	Pre: Demande d'initialisé des listes vide et de temps, avoir une liste grav des positions et des
		 masses des différentes composante.
		  
	Post: Sort trois listes remplie des valeur en fonction du temps, une liste angle, une liste 
		  vitesse angulaire et une liste accélération angulaire.
		  
	"""
	
	v[0] = 0								#Valeur initial de la vitesse angulaire
	theta[0] = 0							#Valeur intial de l'angle d'inclinaison
	
	for i in range(len(tp)-1):
		dt = 0.001							#Interval de temps entre chaque calcul
		
		#Calcul de la position x du centre de poussé
		xP = (np.tan(theta[i]) * (l**2)) / (12 * hc)		
		
		#Calcul de la position y du centre de poussé	
		yP = (-hc/2) + (((math.tan(theta[i])**2 ) * (l**2) / (24 * hc) ) ) / (math.cos(theta[i]))	
		
		x, y = centre_grav(grav)			#Calcul des centre de gravité
		
		#Calcul de la composante x du centre de gravité en fonction de l'angle d'inclinaison
		x_angle = x*(math.cos(-theta[i])) - y * (math.sin(-theta[i]))
		
		#Calcul de la composante y du centre de gravité en fonction de l'angle d'inclinaison	
		y_angle = y * math.cos(theta[i])
		
		Ca = m3 * g * d									#Calcul du couple de la charge
		Mom_F = -(Fp * xP) + (Fg * x_angle)				#Calcul du moment de force 
		
		E_G[i] = M * g * (y_angle - yG_0)				#Calcul de l'enegie du flotteur 
		E_C[i] = -M * g * (abs(yP) - abs(yP_0)) 		#Calcul de l'enegie de poussé
		E_K[i] = (I * (v[i]**2)) / 2					#Calcul de l'enegie cinetique
		E_A[i] = theta[i] * -Ca							#Calcul de l'enegie de la charge
		E_tot[i] = E_A[i] + E_C[i] + E_G[i] + E_K[i]	#Calcul de l'enegie total
		
		
		a[i] = (-v[i] * C_am + Mom_F)/I					#Calcul de l'accelération angulaire
		v[i+1] = v[i] + a[i] * dt						#Calcul de la vitesse angulaire (i + 1) 
		theta[i+1] = theta[i] + v[i] * dt				#Calcul de l'angle d'inclinaison (i + 1)


#Simulation du déplacement d'un objet

depl1 = np.arange(0,d, 2*d/len(tp))				#Creer une liste de de 0 a d deux fois plus petite que tp
v2 = np.empty_like(tp)							#Creer une liste de vide meme longueur que tp
a2 = np.empty_like(tp)							#Creer une liste de vide meme longueur que tp
theta2 = np.empty_like(tp)						#Creer une liste de vide meme longueur que tp
couple = np.empty_like(tp)						#Creer une liste de vide meme longueur que tp


def simulation_deplac():
	
	"""
	Simulation de l'oscilation lorsque qu'une charge est deplacé de 0 a d, en 5 sec
	
	Pre: Demande d'initialisé des listes vide et de temps, avoir une liste grav des positions et des
		 masses des différentes composante.
		
	Post: Sort trois listes remplie des valeur en fonction du temps, une liste angle, une liste 
		  vitesse angulaire et une liste accélération angulaire.
	
	"""
	
	theta2[0] = 0				#Valeur initial de l'angle
	v2[0] = 0					#Valeur initial de la vitesse angulaire
	
	for i in range(len(tp)-1):
		
		dt = 0.001				#Interval de temps entre chaque calcul
		
		#Position du centre de poussé 
		xP2 = (np.tan(theta2[i]) * (l**2)) / (12 * hc)
		
		#print(tp[i])
		
		if tp[i] >= 5:
			
			#Une fois que la charge est au a sa distance final (au bout de 5 seconde)
			#Il calcul les composantes du centre de gravité lorsque la masse est a une distance d
			
			x, y = centre_grav(grav)
			x_angle = x*(math.cos(-theta2[i])) - y * (math.sin(-theta2[i]))
			
			couple[i] = m3 * d * g				#Calcul le couple pour le graphique de couple	
			
		else:
			
			#Liste des différente masses avec la charge en fonction du variable de deplacement
			
			grav2 = [(m1+m2,(0.06, 0.112-hc)), (m3, (depl1[i], 0.40-hc))]
			
			x, y = centre_grav(grav2)
			x_angle = x*(math.cos(-theta2[i])) - y * (math.sin(-theta2[i]))
			
			couple[i] = depl1[i] * g * m3 		#Calcul de couple
			
			
		Mom_F = -(Fp * xP2) + (Fg * x_angle)	#Calcul du moment de force
		
		a2[i] = (-v2[i] * C_am + Mom_F)/I		#Calcul de l'acceleration angulaire
		v2[i+1] = v2[i] + a2[i] * dt			#Calcul de la vitesse angulaire 
		theta2[i+1] = theta2[i] + v2[i] * dt	#Calcul de l'angle d'inclianaison
		
		
#Simulation en fonction de la masse

depl = np.arange(0,d, (d/len(tp)))				#Creer une liste de 0 a d de la meme longueur que tp
v3 = np.empty_like(tp)							#Creer une liste de vide meme longueur que tp
a3 = np.empty_like(tp)							#Creer une liste de vide meme longueur que tp		
theta3 = np.empty_like(tp)						#Creer une liste de vide meme longueur que tp

#Angles des différentes masses
#Listes pour stocker les valeurs de theta

theta_m2 = np.empty_like(tp)					#Creer une liste de vide meme longueur que tp
theta_m4 = np.empty_like(tp)					#Creer une liste de vide meme longueur que tp
theta_m6 = np.empty_like(tp)					#Creer une liste de vide meme longueur que tp	
theta_m8 = np.empty_like(tp)					#Creer une liste de vide meme longueur que tp
theta_m10 = np.empty_like(tp)					#Creer une liste de vide meme longueur que tp
v3_m2 = np.empty_like(tp)						#Creer une liste de vide meme longueur que tp

def simulation_deplac_masse(masse):
	
	"""
	Simulation de l'oscilation lorsque qu'une charge est deplacé de 0 a d, en fonction 
	d'une masse de charge donné
	
	Pre: Demande d'initialisé des listes vide et de temps, avoir une liste grav des positions et des
		 masses des différentes composante, et la masse de la charge a deplacé.
		
	Post: Sort trois listes remplie des valeur en fonction du temps, une liste angle, une liste 
		  vitesse angulaire et une liste accélération angulaire, tout ca en fonction de la masse 
		  de la charge donnée.
	
	"""

	theta3[0] = 0					#Valeur initial de l'angle		
	v3[0] = 0						#Valeur initial de la vitesse angulaire
	
	for i in range(len(tp)-1):
		dt = 0.001					#Interval de temps entre chaque calcul	
		
		Fg = g * ((M-m3) + masse)	#Calcul du poids total 
		Fp = Fg						#On pose la poussé d'archimede
		
		xP2 = (np.tan(theta3[i]) * (l**2)) / (12 * hc)		#Calcul de la possition du centre de poussé
		
		#Position des différentes masses des composantes de la grue
		grav2 = [(m1+m2,(0.06, 0.112-hc)), (masse, (depl[i], 0.40-hc))]
		
		#Position du centre de gravité en fonction de l'angle
		x, y = centre_grav(grav2)
		x_angle = x*(math.cos(-theta[i])) - y * (math.sin(-theta[i]))
		
		Mom_F = -(Fp * xP2) + (Fg * x_angle)	#Calcul du moment de force
		
		a3[i] = (-v3[i] * C_am + Mom_F)/I		#Calcul de l'accélération angulaire
		v3[i+1] = v3[i] + a3[i] * dt			#Calcul de la vitesse angulaire 
		theta3[i+1] = theta3[i] + v3[i] * dt	#Calcul de l'angle d'inclinaison
		
		
		
def simulation():
	simulation_oci()
	simulation_deplac()
	
simulation()	
#Création des listes d'angles en fonction des masses

simulation_deplac_masse(0.05)		#Simulation du deplacement d'une masse de 50 grammes
theta_m2 = theta3.copy()			#Copie de l'angle dans une liste a part

simulation_deplac_masse(0.1)		#Simulation du deplacement d'une masse de 100 grammes
theta_m4 = theta3.copy()			#Copie de l'angle dans une liste a part

simulation_deplac_masse(0.15)		#Simulation du deplacement d'une masse de 150 grammes
theta_m6 = theta3.copy()			#Copie de l'angle dans une liste a part

simulation_deplac_masse(0.2)		#Simulation du deplacement d'une masse de 200 grammes	
theta_m8 = theta3.copy()			#Copie de l'angle dans une liste a part

simulation_deplac_masse(0.3)		#Simulation du deplacement d'une masse de 300 grammes
theta_m10 = theta3.copy()			#Copie de l'angle dans une liste a part

