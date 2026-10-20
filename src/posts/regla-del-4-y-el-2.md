---
title: Outs y la regla del 4 y el 2, con números de verdad
date: 2026-10-12
tags: [probabilidad, póker]
resumen: Multiplicar los outs por 4 o por 2 es el atajo más usado en la mesa. Aquí comparo la regla con la probabilidad exacta y explico de dónde sale y cuándo empieza a fallar.
portada: /img/portada-poker.svg
portadaAlt: Mesa de póker con un as y un rey de corazones y un flop con dos corazones
---

En Texas Hold'em casi nunca tienes la mejor mano en el flop; lo normal es ir «proyectado» y necesitar una carta concreta. La pregunta es siempre la misma: **¿me compensa pagar para verla?** Para responderla en la mesa, sin calculadora, existe la regla del 4 y el 2. Quería comprobar hasta qué punto es fiable.

## Qué es un out

Un *out* es cada carta que queda en la baraja y que mejora tu mano hasta ganar. Ejemplo típico: llevas **A♥ K♥** y el flop es **9♥ 4♥ Q♠**. Tienes cuatro corazones; quedan 13 − 4 = **9 corazones** en la baraja, así que tienes 9 outs para el color.

Después del flop conoces 5 cartas (tus 2 y las 3 de la mesa), por lo que quedan **47 desconocidas**.

## La cuenta exacta

La forma más cómoda es calcular la probabilidad de **no** ligar en ninguna de las dos cartas que faltan y restarla de 1:

<p class="formula">P(ligar en turn o river) = 1 − C(47−n, 2) / C(47, 2)</p>

Con 9 outs: 1 − (38·37)/(47·46) = 1 − 1406/2162 ≈ **35,0 %**.

Si solo queda una carta por ver (del turn al river) es directo: n/46. Con 9 outs, 9/46 ≈ **19,6 %**.

## De dónde sale la regla

Desarrollando la expresión anterior:

<p class="formula">1 − (1 − n/47)(1 − n/46) = n/47 + n/46 − n²/2162</p>

Los dos primeros términos suman aproximadamente 2n/46,5 ≈ **4,3·n %**. El último resta, y crece con el cuadrado de n. Para pocos outs ambos efectos casi se cancelan y queda el famoso **4·n**. Con una sola carta, n/46 ≈ 2,2·n %, que se redondea a **2·n**.

## ¿Cuánto se equivoca?

<div class="tabla">

| Outs | Proyecto típico | Exacta (2 cartas) | 4·n | Exacta (1 carta) | 2·n |
|---:|:---|---:|---:|---:|---:|
| 4 | Escalera interna | 16,5 % | 16 % | 8,7 % | 8 % |
| 8 | Escalera abierta | 31,5 % | 32 % | 17,4 % | 16 % |
| 9 | Color | 35,0 % | 36 % | 19,6 % | 18 % |
| 12 | Color + pareja | 45,0 % | 48 % | 26,1 % | 24 % |
| 15 | Color + escalera | 54,1 % | 60 % | 32,6 % | 30 % |

</div>

<figure>
  <img src="/img/poker-grafica.svg" alt="Gráfica que compara la probabilidad exacta con la regla del 4 y su versión corregida entre 1 y 15 outs" width="1000" height="520" loading="lazy">
  <figcaption>Hasta 8 outs la regla del 4 es casi exacta; a partir de ahí sobreestima. La corrección 4·n − (n − 8) la pega a la curva real.</figcaption>
</figure>

Hasta 8 o 9 outs el error es de un punto como mucho. A partir de ahí el término n² pesa y la regla se pasa: con 15 outs dice 60 % cuando la realidad es 54 %. El ajuste que uso es **restar (n − 8) cuando tengo más de 8 outs**: con 15 outs, 60 − 7 = 53 %, a un punto del valor exacto.

## Cómo usarla para decidir

La probabilidad sola no dice nada; hay que compararla con lo que cuesta pagar. Si el bote es de 100 y el rival apuesta 50, pagas 50 para optar a un bote final de 200. Necesitas ganar al menos:

<p class="formula">50 / (100 + 50 + 50) = 25 %</p>

- **Si es la última apuesta antes del river** (te queda ver una carta): con el color tienes ≈ 19,6 %. No llega al 25 %, así que solo pagarías contando con cobrar más si ligas (*implied odds*).
- **Si es un all-in en el flop** (ves turn y river sin pagar más): tienes ≈ 35 %, por encima del 25 %. Pagar es rentable a largo plazo.

<p class="nota">Error que cometía al principio: usar la regla del 4 en el flop cuando el rival todavía puede apostar en el turn. Si vas a tener que pagar otra vez, lo correcto es usar la regla del 2 en cada calle.</p>
