#!/usr/bin/env python
#coding=utf-8

import os

class NumerosRomanos:
    MONEDA = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self):
        pass        
    
    @staticmethod
    def validar_simbolos_romanos(romano):
        simbolos_admitidos = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        if not romano or not all(c in simbolos_admitidos for c in romano):
            return False
        else:
            return True

    @staticmethod
    def validar_reglas_romano_repetir(romano):
        nunca_pueden_ser_repetidos = ('D', 'L', 'V')
        pueden_ser_repetidos = ('I', 'X', 'C', 'M')

        CANT_VECES_I = 3
        CANT_VECES_X = 4 
        CANT_VECES_C = 4 
        CANT_VECES_M = 4

        for value in nunca_pueden_ser_repetidos:
            if romano.count(value) > 1:
                return False
        if romano.count('I') > CANT_VECES_I:
            return False
        if romano.count('X') > CANT_VECES_X \
            or (romano.count('X') == 4 and 'XXXIX' not in romano):
            return False
        if romano.count('C') > CANT_VECES_C \
            or (romano.count('C') == 4 and 'CCCXC' not in romano):
            return False
        if romano.count('M') > CANT_VECES_M \
            or (romano.count('M') == 4 and 'MMMCM' not in romano):
            return False   

        return True    

    @staticmethod
    def validar_romanos_sustraer_reglas(romano):
        pueden_ser_sustraidos_desde = { 'C': {'D', 'M'}, 'I': {'V', 'X'}, 'X': {'L', 'C'} }
        nunca_pueden_ser_sustraidos = ('V', 'L', 'D')

        ultima_sustraccion_romano = 0
        ultima_valor_arabico = 9999
        actual_valor_arabico = 0
        i = 0
        while i < len(romano):
            if (i < len(romano) - 1) and NumerosRomanos.MONEDA[romano[i]] < NumerosRomanos.MONEDA[romano[i+1]]:
                if romano[i] in nunca_pueden_ser_sustraidos:
                    return False
                if romano[i+1] not in pueden_ser_sustraidos_desde[romano[i]]:
                    return False

                actual_valor_arabico = NumerosRomanos.MONEDA[romano[i+1]] - NumerosRomanos.MONEDA[romano[i]]
                if actual_valor_arabico > ultima_valor_arabico:
                    return False
                if ultima_sustraccion_romano != 0 and actual_valor_arabico + ultima_valor_arabico >= ultima_sustraccion_romano:
                    return False
                else:
                    ultima_sustraccion_romano = NumerosRomanos.MONEDA[romano[i+1]]
                    ultima_valor_arabico = actual_valor_arabico
                    i = i + 2
            else:
                actual_valor_arabico = NumerosRomanos.MONEDA[romano[i]]
                if actual_valor_arabico > ultima_valor_arabico:
                    return False
                if ultima_sustraccion_romano != 0 and actual_valor_arabico + ultima_valor_arabico >= ultima_sustraccion_romano:
                    return False
                else:
                    ultima_valor_arabico = actual_valor_arabico
                    ultima_sustraccion_romano = 0
                    i = i + 1            
        return True    

    @staticmethod
    def validar_romanos(romano):
        return NumerosRomanos.validar_simbolos_romanos(romano) \
           and NumerosRomanos.validar_reglas_romano_repetir(romano) \
           and NumerosRomanos.validar_romanos_sustraer_reglas(romano)

    @staticmethod
    def hacia_arabico(simbolos):
        if not NumerosRomanos.validar_romanos(simbolos):
            return None
        numeros = [ NumerosRomanos.MONEDA[s] for s in simbolos ]

        for i in range(len(numeros) -1):
            if numeros[i] < numeros[i+1]:
                numeros[i] = -numeros[i]

        return sum(numeros)    