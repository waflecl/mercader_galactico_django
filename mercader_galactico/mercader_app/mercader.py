#!/usr/bin/env python
#coding=utf-8

from mercader_galactico.mercader_app.numeros_romanos import NumerosRomanos
class Mercader:
    libro_palabras = {}
    libro_precios = {}

    respuesta_defecto = ""

    def __init__(self, respuesta_defecto):
        self.respuesta_defecto = respuesta_defecto
    
    def crear_libro_palabras(self, ref_palabras):
        error_msj = []        
        for item in ref_palabras:
            patrones = item.split(' ')
            if len(patrones) == 3 and patrones[1] == 'is':
                if patrones[0] not in self.libro_palabras:
                    self.libro_palabras.update({patrones[0]: patrones[2]})
                elif self.libro_palabras[patrones[0]] != patrones[2]:
                    print("Update Word " + patrones[0] + " from " + self.libro_palabras[patrones[0]] + " to " + patrones[2])
                    self.libro_palabras.update({patrones[0]:patrones[2]})
                else:
                    continue
            else:
                error_msj.append(item)                
        return error_msj

    def crear_libro_precios(self, libro_precios):
        error_msjs = []
        for item in libro_precios:
            patrones = item.split(' ')
            try:
                buen_patron_precio = int(patrones[-2])
            except ValueError:
                print("That's not an integer: ", patrones[-2])
                error_msjs.append(item)

            buen_nombre = patrones[-4]

            monto_arabico = self.traducir_refefencia_de_arabico(patrones[:-4])
            if monto_arabico:
                buen_precio = float(buen_patron_precio)/monto_arabico
                if buen_precio not in self.libro_precios:
                    self.libro_precios.update({buen_nombre: buen_precio})
                elif buen_nombre in self.libro_precios and self.libro_precios[buen_nombre] != buen_precio:
                    print("update price of " + buen_nombre + " from " + self.libro_precios[buen_nombre] + " to " + buen_precio)
                    self.libro_precios.update({buen_nombre: buen_precio})
                else:
                    continue
            else:
                print('Error while updaing prices dict with:', buen_nombre, monto_arabico)
                error_msjs.append(item)
        return error_msjs             

    def traducir_refefencia_de_arabico(self, lista_palabras_referencia):
        numeros_romanos = []
        for item in lista_palabras_referencia:
            if item in self.libro_palabras:
                numeros_romanos.append(self.libro_palabras[item])
            else:
                print('Error amount pattern', item)
                return None
        
        return NumerosRomanos.hacia_arabico(''.join(numeros_romanos))

    def aprender_conocimiento(self, ref_palabras, precio_msjs):
        error_msjs = []
        error_msjs.extend(self.crear_libro_palabras(ref_palabras))
        error_msjs.extend(self.crear_libro_precios(precio_msjs))
        return error_msjs

    def responder_preguntas(self, preguntas):
        respuestas = []

        for item in preguntas:
            if 'how much is' in item:
                num_respuesta = self.traducir_refefencia_de_arabico(item.split()[3:-1])
                respuestas.append(" ".join(item.split()[3:-1]) + ' is ' + str(num_respuesta))
            elif 'how many Credits' in item:
                buen_nombre = item.split()[-2]
                buen_monto = self.traducir_refefencia_de_arabico(item.split()[4:-2])
                if buen_monto is not None and buen_nombre in self.libro_precios:
                    buen_precio = int(buen_monto * self.libro_precios[buen_nombre])
                    respuestas.append(" ".join(item.split()[4:-1]) + ' is ' + str(buen_precio) + ' Credits')
                else:
                    respuestas.append(self.respuesta_defecto + ": "+  " ".join(item.split()[4:-1]))
            else:
                respuestas.append(self.respuesta_defecto)
        return respuestas