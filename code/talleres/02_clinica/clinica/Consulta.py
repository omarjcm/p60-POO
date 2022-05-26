#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime

class Consulta:
    def __init__(self, fecha_consulta, paciente, especialidad):
        self.__fecha_consulta = datetime.strptime(fecha_consulta, '%d-%m-%Y')
        self.__valor_descuento = 0.0
        self.__valor_total = 0.0
        self.ref_paciente = paciente
        self.ref_especialidad = especialidad

    @property
    def fecha_consulta(self):
        return self.__fecha_consulta

    @fecha_consulta.setter
    def fecha_consulta(self, valor):
        self.__fecha_consulta = datetime.strptime(valor, '%d-%m-%Y')

    def __str__(self):
        return str(self.__fecha_consulta.day) + '/' + str(self.__fecha_consulta.month) + '/' + str(self.__fecha_consulta.year) + ' ' + str(self.ref_paciente) + ' - ' + str(self.ref_especialidad)
