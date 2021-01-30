#!/usr/bin/env python3
#coding=utf-8

import sys
import os

from mercader_galactico.mercader_app.mercader import Mercader
from mercader_galactico.mercader_app.leer_mensaje import leer_mensaje

RESPUESTA_POR_DEFECTO = "I have no idea what you are talking about"

def aprender_y_responder(message):
    info = leer_mensaje(message)
    error_msjs = info['error_msj']

    if len(info['ref_palabras']) > 0:
        mercader = Mercader(RESPUESTA_POR_DEFECTO)
        resultado = mercader.aprender_conocimiento(info['ref_palabras'], info['precio_msj'])
        
        if resultado:
            error_msjs.extend(resultado)
        resultado = mercader.responder_preguntas(info['preguntas'])
        if resultado:
            return resultado
        if error_msjs:
            return error_msjs
    else:
        return "no ref words found" 
