---
title: Mi rastreador de precios de gasolineras en Java
date: 2026-10-05
tags: [java, datos abiertos, proyectos]
resumen: Una aplicación de escritorio que hice para saber qué gasolinera es la más barata usando los datos abiertos del Ministerio.
portada: /img/portada-gasolineras.svg
portadaAlt: Dibujo de un surtidor y un panel con precios de gasolina
---

Hace un tiempo me di cuenta de que entre gasolineras de la misma ciudad podía haber más de 10 céntimos de diferencia por litro. Llenando el depósito eso son varios euros cada vez, así que decidí hacerme un programa en Java que me dijera cuál es la más barata.

## De dónde saco los precios

El Ministerio publica los precios de todas las gasolineras de España en un servicio web gratuito que devuelve los datos en JSON. Para cada gasolinera viene el nombre, la dirección, el municipio, la provincia y el precio de cada combustible. No hace falta registrarse, así que es perfecto para un proyecto personal.

## Cómo funciona

El programa tiene cuatro partes:

1. Descarga los datos (o los lee de un fichero guardado para hacer pruebas).
2. Guarda la información de cada gasolinera.
3. Los filtra por provincia y combustible.
4. Los muestra en una ventana hecha con Swing, en una tabla que se puede ordenar por precio.

## Problemas que me encontré

- Los precios vienen con coma (1,589) y Java espera un punto, así que al principio me daba error al convertirlos. Lo arreglé cambiando la coma por un punto antes de convertir.
- Algunas gasolineras no venden todos los combustibles y el precio viene vacío.
- Mientras descargaba los datos la ventana se quedaba congelada. Lo solucioné haciendo la descarga en segundo plano.

Me gustaría añadirle un mapa y guardar los precios de cada día para ver cómo cambian.
