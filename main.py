#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from _CarrerasDB_local  import *
import urllib2

class Ventanas(ScreenManager):
    nom =""    
    def datos(self,ventana, Resolucion):
        # Limpiar campos 
        self.nom = Resolucion
        self.nombreVentana=ventana
        print(ventana," ====> ",Resolucion)

    def limpiar(self):
        self.titulo=""
        self.resolucion=""
        self.duracion=""
        self.sede=""
        self.horario=""
        self.modalidad=""
        self.plan="0.jpeg"
        self.requerimiento="0.jpeg"
        print("Limpiando Variables") 

    def carrera(self):
        self.busqueda = ""+self.nom
       
        # Realizando Consulta y Asignando el resultado de la Consulta
        valor=DbCarreras(self.busqueda )

        #Asignacion de los Datos Traidos  a la Ventana
        if self.busqueda  in valor:
            print(self.busqueda )
            for i in range (len(valor)):
                if i==0:
                  # print("\t Carrera: ",valor[i])
                    self.titulo= "No Disponible"
                    if valor[i] != "":
                        self.titulo= valor[i]
                if i==1:
                    # print("\t Resolución: ",valor[i])
                    self.resolucion= "No Disponible"
                    if valor[i] != "":
                        self.resolucion= valor[i]
                if i==2:
                    # print("Duración: ",valor[i])
                    self.duracion= "No Disponible"
                    if valor[i] != "":
                        self.duracion= valor[i]
                if i==3:
                  # print("Horario: ",valor[i])
                    self.horario= "No Disponible"
                    if valor[i] != "":
                        self.horario= valor[i]
                if i==4:
                     # print("Sede: ",valor[i])
                    self.sede= "No Disponible"
                    if valor[i] != "":
                        self.sede= valor[i]
                if i==5:
                    # print("Modalidad: ",valor[i])
                    self.modalidad= "No Disponible"
                    if valor[i] != "":
                        self.modalidad= valor[i]
                if i==6:
                    # print("imagen requerimiento: ",valor[i])
                    self.requerimiento= "0.jpeg"
                    if valor[i] != "":
                        self.requerimiento= valor[i]
                if i==7:
                    # print("imagen plan: ",valor[i])
                    self.plan= "0.jpeg"
                    if valor[i] != "":
                       self.plan= valor[i]                     
                        
        else:
            print("no esta DISPONIBLE")
    
class AplicacionApp(App):
	def build(self):
       
		return Ventanas()


if __name__ == '__main__':
	AplicacionApp().run()