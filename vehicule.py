from datetime import date

class Vehicule:
    def __init__(self,marque,modele,annee,prix_Location):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self._prix_Location = prix_Location


    @property
    def marque(self):
        return  self.__marque

    @marque.setter
    def marque(self,nouvelleMarque):
        self.__marque = nouvelleMarque

    @property
    def modele(self):
        return  self.__modele

    @modele.setter
    def modele(self,nouveauModele):
        self.__modele = nouveauModele

    @property
    def annee(self):
        return  self.__annee

    @annee.setter
    def annee(self,nouveauAnnee):
        if isinstance(nouveauAnnee , date ):
            self.__annee = nouveauAnnee
        else :
            raise ValueError("L'année invalide .")

    @property
    def prix_Location(self):
        return self._prix_Location

    @prix_Location.setter
    def  prix_Location(self,nouvellePrixLocation):
        if nouvellePrixLocation > 0 :
            self._prix_Location = nouvellePrixLocation

    def Afficher_details(self):
        print(f"marque : {self.__marque}\n"
              f"modele : {self.__modele}\n"
              f"annee : {self.__annee }\n"
              f"Le prix de location : {self._prix_Location}")

    def Calculer_prix_location(self,duree):
        prix = self._prix_Location * duree
        if duree >= 7 :
            return self.reduction(prix)
        else:
            return prix

    def reduction(self , prix):
        return prix - (prix * 10 / 100)
class Voiture(Vehicule):

    def __init__(self,marque,modele,annee,prix_Location,nombrePortes):
        super().__init__(marque,modele,annee,prix_Location)
        self.__nombrePortes = nombrePortes

    @property
    def nombrePortes(self):
        return self.__nombrePorte

    @nombrePortes.setter
    def nombrePortes(self,nouvelleNombre):
        if nouvelleNombre > 0 :
            self.__nombrePorte = nouvelleNombre

        else :
            raise ValueError(" le nombre de porte doit etre positive .")

    def Afficher_details(self):
        print(f"{self.Afficher_details()}\n"
              f"Le nombre de portes : {self.__nombrePorte}")

class Moto(Vehicule):
    def __init__(self,marque,modele,annee,prix_Location,cylindree):
        super().__init__(marque, modele, annee, prix_Location)
        self.__cylindree = cylindree

    @property
    def cylindree(self):
        return self.__cylindree

    @cylindree.setter
    def cylinder(self,diametre):
        if diametre > 0 :
            self.__cylindree = diametre
        else :
            raise ValueError("le diamétre doit etre positive.")

    def Afficher_details(self):
        print(f"{self.Afficher_details()}\n"
              f"Cylinder : {self.__cylindree}")


class Camion(Vehicule):
    def __init__(self,marque,modele,annee,prix_Location,capacite_Chargement):
        super().__init__(marque, modele, annee, prix_Location)
        self.__capacite_Chargement = capacite_Chargement

    @property
    def capacite_Chargement(self):
        return self.__capacite_Chargement

    @capacite_Chargement.setter
    def capacite_Chargement(self,nouvelleCapacite):
        if nouvelleCapacite > 0 :
            self.__capacite_Chargement = nouvelleCapacite

        else :
            raise ValueError(f"La capacité doit etre positive.")

    def Afficher_details(self):
        print(f"{self.Afficher_details()}\n"
              f"Capacité de chargement : {self.__capacite_Chargement}")

class Location :

    __auto = 0
    def __init__(self,numero_location , nom_client , vehicule , date_debut , date_fin , montant_Totale ):
        Location.__auto += 1
        self.__numero_location = Location.__auto
        self.__nom_client =  nom_client
        self.__vehicule =  vehicule
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__montant_Totale =  montant_Totale

    @property
    def numero_location(self):
        return  self.__numero_location

    @property
    def nom_client(self):
        return self.__nom_client

    @nom_client.setter
    def nom_client(self,nouvelleNomClient):
        self.__nom_client  = nouvelleNomClient

    @property
    def vehicule(self):
        return  self.__vehicule

    @vehicule.setter
    def vehicule(self,nouvelleVehicule):
        self.__vehicule = nouvelleVehicule

    @property
    def date_debut(self):
        return  self.__date_debut

    @date_debut.setter
    def date_debut(self,nouvelleDateDebut):
        if isinstance(nouvelleDateDebut,date):
            self.__date_debut  = nouvelleDateDebut

        else :
            raise ValueError("la date de debut de location invalide.")

    @property
    def date_debut(self):
        return self.__date_fin

    @date_debut.setter
    def date_debut(self, nouvelleDateFin):
        if isinstance(nouvelleDateFin, date):
            self.__date_debut = nouvelleDateFin

        else:
            raise ValueError("la date de fin de location invalide.")


    @property
    def montant_Totale(self):
        return    self.__montant_Totale

    @montant_Totale.setter
    def montant_Totale(self,montant):
















