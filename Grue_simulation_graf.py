import matplotlib.pyplot as plt
import numpy as np

from Simulation_proto import *


def graf_sim():
	"""
	Donne des graphique issue de la simulation du fichier Simulation_proto
	Pre: Il suffit de faire tourné tourné la fonction simulation du fichier 
		 Simulation_proto
	Post: Ressort 5 graphique, inslinaison, enegies, diagramme de phase 
		  graphiques de charges et gaphique des charge variable
	"""
	
##############################	
##Graphique des trajectoires##
##############################	

	plt.xlabel("t(s)")
	plt.ylabel('Angle (Deg)')
	plt.title("Grue simulation", size='xx-large')
	plt.figure(1)
	plt.subplot(1,1,1)
	
	plt.axhline(y = np.rad2deg(angle_soulev),ls='dotted', color='red')
	plt.axhline(y = np.rad2deg(angle_chav),ls='dotted', color='green')
	plt.legend(["Seuils de soulevement", "Seuils de submersion"], loc='lower right')
	plt.axhline(y = -np.rad2deg(angle_chav),ls='dotted', color='green')
	plt.axhline(y = -np.rad2deg(angle_soulev),ls='dotted', color='red')
	plt.axhline(y = 0, color='black', ls='dotted')
	
	plt.plot(tp, np.rad2deg(theta), color='#377cff')
	text = "Theta final = " + str(round(np.rad2deg(theta[-1]), 4)) + " Deg"
	props = dict(boxstyle='square', facecolor='#ffffff')
	plt.text(6.43, -np.rad2deg(angle_chav)+3, text, bbox=props, size='large')
	
	plt.show()
	
	
	
	plt.xlabel("t(s)")
	plt.ylabel('Angle (Deg)')
	plt.title("Grue simulation", size='xx-large')
	plt.figure(6)
	plt.subplot(1,1,1)
	
	plt.axhline(y = np.rad2deg(angle_soulev),ls='dotted', color='red')
	plt.legend(["Seuils de soulevement"], loc='lower right')
	plt.plot(tp, np.rad2deg(theta), color='#377cff')
	text = "Theta final = " + str(round(np.rad2deg(theta[-1]), 4)) + " Deg"
	props = dict(boxstyle='square', facecolor='#ffffff')
	plt.text(6.43, 0.3, text, bbox=props, size='large')
	
	plt.show()
	
##########################
##Graphique des Energies##
##########################

	plt.figure(2)
	plt.xlabel("t(s)")
	plt.ylabel("Energie (J)")
	plt.title("Graphiques : Energies")
	
	E_charge, = plt.plot(tp, E_A, color='red')
	E_poussé, = plt.plot(tp, E_C, color='#ffcc12')
	E_flotteur, = plt.plot(tp, E_G, color='#0059ff')
	E_ciné, = plt.plot(tp, E_K, color='green')
	E_totale, = plt.plot(tp, E_tot, color='purple')
	
	plt.legend([E_charge, E_poussé, E_flotteur, E_ciné, E_totale], ["E Charge", "E Poussé", "E Flotteur", "E Cinétique", "E Totale"])
	plt.show()
	
##################################
##Graphique : Diagramme de phase##
##################################

	plt.figure(3)
	plt.xlabel("Angle d'inclinaison (Deg)")
	plt.ylabel("Vitesse angulaire (Deg/s)")
	plt.title("Diagramme de phase", size='x-large')
	
	plt.plot(np.rad2deg(theta), np.rad2deg(v))
	
	plt.show()
	
#########################	
##Graphique des charges##
#########################

	plt.figure(4)
	plt.grid(True)
	plt.xlabel("Temps (s)")
	plt.ylabel("Inclinaison (Deg)")
	plt.title("Graphique des charges")
	
	plt.axhline(y = np.rad2deg(angle_soulev),ls='dotted', color='red')
	plt.axhline(y = np.rad2deg(angle_chav),ls='dotted', color='green')
	
	plt.plot(tp, np.rad2deg(theta_m2))
	plt.plot(tp, np.rad2deg(theta_m4))
	plt.plot(tp, np.rad2deg(theta_m6))
	plt.plot(tp, np.rad2deg(theta_m8))
	plt.plot(tp, np.rad2deg(theta_m10))
	
	plt.legend(["Seuils de soulevement", "Seuils de submersion", "m = 50g", "m = 100g", "m = 150g", "m = 200g", "m = 300g"], loc='upper left')
	
	plt.axhline(y = -np.rad2deg(angle_chav),ls='dotted', color='green')
	plt.axhline(y = -np.rad2deg(angle_soulev),ls='dotted', color='red')
	plt.axhline(y = 0, color='black', ls='dotted')
	
	plt.show() 
	
	
	
	plt.figure(7)
	plt.grid(True)
	plt.xlabel("Temps (s)")
	plt.ylabel("Inclinaison (Deg)")
	plt.title("Graphique des charges")
	
	plt.axhline(y = np.rad2deg(angle_soulev),ls='dotted', color='red')
	
	plt.plot(tp, np.rad2deg(theta_m2))
	plt.plot(tp, np.rad2deg(theta_m4))
	plt.plot(tp, np.rad2deg(theta_m6))
	plt.plot(tp, np.rad2deg(theta_m8))
	plt.plot(tp, np.rad2deg(theta_m10))
	
	plt.legend(["Seuils de soulevement", "m = 50g", "m = 100g", "m = 150g", "m = 200g", "m = 300g"], loc='upper left')
	
	plt.show()
	
#############################	
##Graphique charge variable##
#############################

	plt.figure(5)

#Graphique couple par rapport au temps

	plt.subplot(3,1,1)
	plt.title("Graphique charge variable", size='x-large')
	plt.ylabel("Couple appliqué (N.m)", size='small')
	plt.plot(tp, couple)
	
#Graphique angles par rapport au temps

	plt.subplot(3,1,2)
	plt.ylabel("Angle (Deg)", size='small')
	
	#plt.axhline(y = (np.rad2deg(angle_chav)),ls='dotted', color='red')
	#plt.axhline(y = -(np.rad2deg(angle_chav)),ls='dotted', color='red')
	plt.axhline(y = 0, color='black', ls='dotted')
	plt.plot(tp, np.rad2deg(theta2))

#Graphique vitesse angulaire par rapport au temps 
			
	plt.subplot(3,1,3)
	plt.xlabel("t(s)")
	plt.ylabel("Vitesse angulaire (Deg/s)", size='small')
	plt.plot(tp, np.rad2deg(v2))
		
	plt.show()

simulation()
graf_sim()                     
