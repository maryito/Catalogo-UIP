#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 
import os.path


def DbCarreras(linciatura): 
    contenido =[]
    con = None  
    try:
        #traer la dirrecion del archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "BD_carreras")
        con = sqlite3.connect(db_path)    
        cur = con.cursor()    
        
        # cur.execute('SELECT * FROM Carrera')
        consulta= ("SELECT * FROM carrera WHERE resolucion LIKE '{}'".format(linciatura))
        cur.execute(consulta)
        datos = cur.fetchone()
        if datos == None:
            print("-No disponible-")
        else:           
            print("-Disponible-")
            for i  in range(len(datos)):
                if i==0:
                    # print("  Resolución: ",datos[i])
                    contenido.append(datos[i])
                if i==1:
                    # print("Duración: ",datos[i])
                    contenido.append(datos[i])
                if i==2:
                    # print("Sede: ",datos[i])
                    contenido.append(datos[i])
                if i==3:
                    # print("Horario: ",datos[i])
                    contenido.append(datos[i])
                if i==4:
                    # print("Modalidad: ",datos[i])
                    contenido.append(datos[i])
                    # print(contenido)
                if i==5:
                    # print("Modalidad: ",datos[i])
                    contenido.append(datos[i])
                    # print(contenido    
                if i==6:
                    # print("Modalidad: ",datos[i])
                    contenido.append(datos[i])
                    # print(contenido    
                if i==7:
                    # print("Modalidad: ",datos[i])
                    contenido.append(datos[i])
                    # print(contenido    
    except Exception as e: 
        print("Error %s : "%(e.args[0]) )
    finally:
        if con:
            con.close()
    return contenido

# lic= 'CTF-14-2013 -  16-Abril-2013'
# print(DbCarreras(lic))
