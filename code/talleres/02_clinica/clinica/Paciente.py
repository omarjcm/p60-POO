#!/usr/bin/python
#-*- coding: utf-8 -*-

from select import select


class Paciente:
    def __init__(self, nombre, apellido, sexo, anio_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__anio_nacimiento = anio_nacimiento

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

