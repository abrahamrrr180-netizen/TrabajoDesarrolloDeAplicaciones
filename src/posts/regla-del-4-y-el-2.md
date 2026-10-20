---
title: La regla del 4 y el 2 en el póker
date: 2026-10-12
tags: [probabilidad, póker]
resumen: Un truco muy sencillo para calcular en la mesa la probabilidad de ligar tu jugada, y lo he comparado con el cálculo exacto.
portada: /img/portada-poker.svg
portadaAlt: Dibujo de una mesa de póker con cartas y fichas
---

Me gusta jugar al póker con amigos y siempre me ha interesado la parte de probabilidad. Una de las cosas más útiles que he aprendido es la regla del 4 y el 2.

## Qué son los outs

Los *outs* son las cartas que quedan en la baraja y que te hacen ganar la mano. Por ejemplo, si tienes A♥ K♥ y en la mesa salen 9♥ 4♥ Q♠, te falta un corazón para hacer color. Quedan 9 corazones, así que tienes **9 outs**.

## La regla

- En el flop (quedan dos cartas por salir): outs × 4.
- En el turn (queda una carta): outs × 2.

Con el ejemplo del color: 9 × 4 = 36 % en el flop y 9 × 2 = 18 % en el turn.

## ¿Funciona de verdad?

Quería comprobarlo, así que calculé la probabilidad exacta. Después del flop quedan 47 cartas que no conoces, y la probabilidad de no ligar en ninguna de las dos es (47 − n)/47 · (46 − n)/46. Restándolo a 1 sale la probabilidad de ligar. Para 9 outs da un **35 %**, muy cerca del 36 % de la regla.

| Outs | Regla del 4 | Exacto |
|---|---|---|
| 4 | 16 % | 16,5 % |
| 8 | 32 % | 31,5 % |
| 9 | 36 % | 35 % |
| 15 | 60 % | 54 % |

![Gráfica comparando la regla del 4 con la probabilidad exacta](/img/poker-grafica.svg)

Hasta unos 9 outs la regla es casi perfecta, pero con muchos outs se pasa. Leí que se corrige restando (outs − 8) cuando tienes más de 8, y con 15 outs da 53 %, que ya se acerca bastante.
