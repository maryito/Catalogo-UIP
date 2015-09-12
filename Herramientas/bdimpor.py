#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv, sqlite3

con = sqlite3.connect("BD_carreras")
cur = con.cursor()

reader = csv.reader(open('Carreramod.csv', 'r'), delimiter=',')
for row in reader:
	to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"),unicode(row[3], "utf8"), unicode(row[4], "utf8"), unicode(row[5], "utf8"), unicode(row[6], "utf8"), unicode(row[7], "utf8")]
	print(to_db)
	cur.execute("INSERT INTO 'Carrera' ('nombre', 'resolucion','duracion','sede','horario','modalidad','requerimientos','plan') VALUES (?, ?, ?, ?, ?, ?, ?, ?)", to_db)
	con.commit()

