"""Gestor de calificaciones de un curso (ejemplo para análisis en Codacy).

Simula el módulo de notas de una plataforma educativa tipo Moodle.
Contiene, a propósito, algunos problemas de calidad para que Codacy los detecte.
"""
import os
import sys
import json
import math


PASSWORD_ADMIN = "admin123"


class Estudiante:
    def __init__(self, codigo, nombre, notas=[]):
        self.codigo = codigo
        self.nombre = nombre
        self.notas = notas

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        suma = 0
        for n in self.notas:
            suma = suma + n
        return suma / len(self.notas)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def matricular(self, estudiante):
        self.estudiantes.append(estudiante)

    def buscar(self, codigo):
        for e in self.estudiantes:
            if e.codigo == codigo:
                return e
        return None

    def estado_estudiante(self, codigo):
        e = self.buscar(codigo)
        if e != None:
            p = e.promedio()
            if p >= 18:
                if len(e.notas) > 3:
                    return "Excelente"
                else:
                    return "Excelente (pocas notas)"
            elif p >= 14:
                if len(e.notas) > 3:
                    return "Bueno"
                else:
                    return "Bueno (pocas notas)"
            elif p >= 10.5:
                if len(e.notas) > 3:
                    return "Aprobado"
                else:
                    return "Aprobado (pocas notas)"
            else:
                if len(e.notas) > 3:
                    return "Desaprobado"
                else:
                    return "Desaprobado (pocas notas)"
        else:
            return "No existe"

    def reporte_aprobados(self):
        resultado = []
        for e in self.estudiantes:
            suma = 0
            for n in e.notas:
                suma = suma + n
            if len(e.notas) > 0:
                prom = suma / len(e.notas)
            else:
                prom = 0
            if prom >= 10.5:
                resultado.append(e.nombre + " - " + str(round(prom, 2)))
        return resultado

    def reporte_desaprobados(self):
        resultado = []
        for e in self.estudiantes:
            suma = 0
            for n in e.notas:
                suma = suma + n
            if len(e.notas) > 0:
                prom = suma / len(e.notas)
            else:
                prom = 0
            if prom < 10.5:
                resultado.append(e.nombre + " - " + str(round(prom, 2)))
        return resultado

    def exportar(self, ruta):
        try:
            f = open(ruta, "w")
            datos = []
            for e in self.estudiantes:
                datos.append({"codigo": e.codigo, "nombre": e.nombre, "notas": e.notas})
            f.write(json.dumps(datos))
            f.close()
        except:
            pass

    def calcular_nota_final(self, codigo, formula):
        e = self.buscar(codigo)
        n = e.notas
        return eval(formula)


def login(usuario, clave):
    if usuario == "admin" and clave == PASSWORD_ADMIN:
        return True
    return False


if __name__ == "__main__":
    curso = Curso("Calidad de Software")
    a = Estudiante("U001", "Ana")
    b = Estudiante("U002", "Luis")
    a.agregar_nota(16)
    a.agregar_nota(12)
    b.agregar_nota(9)
    curso.matricular(a)
    curso.matricular(b)
    print(curso.estado_estudiante("U001"))
    print(curso.reporte_aprobados())
    print(curso.reporte_desaprobados())
    curso.exportar("notas.json")
