#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime

class Consulta:
    def __init__(self, fecha_consulta, paciente, especialidad):
        self.__fecha_consulta = datetime.strptime(fecha_consulta, '%d-%m-%Y')
        self.ref_paciente = paciente
        self.ref_especialidad = especialidad

    @property
    def fecha_consulta(self):
        return self.__fecha_consulta

    @fecha_consulta.setter
    def fecha_consulta(self, valor):
        self.__fecha_consulta = datetime.strptime(valor, '%d-%m-%Y')

