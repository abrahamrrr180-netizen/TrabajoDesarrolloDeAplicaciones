---
title: Cómo monté un rastreador de precios de gasolineras en Java
date: 2026-10-05
tags: [java, datos abiertos, proyectos]
resumen: El Ministerio publica el precio de cada gasolinera de España varias veces al día. Con Java y Swing lo convertí en una aplicación de escritorio para saber dónde repostar.
portada: /img/portada-gasolineras.svg
portadaAlt: Ilustración de un surtidor junto a un panel con precios de gasolina y gasóleo
---

Entre dos gasolineras de la misma ciudad puede haber diez o quince céntimos de diferencia por litro. En un depósito de 50 litros son unos 6 € cada vez que repostas, así que quise tener una herramienta que me dijera de un vistazo cuál es la más barata cerca de casa. De ahí salió este proyecto: una aplicación de escritorio en **Java** que descarga los precios oficiales, los filtra y los ordena.

## De dónde salen los datos

El Ministerio para la Transición Ecológica mantiene el **Geoportal de Gasolineras**, y detrás hay un servicio REST público que devuelve en JSON todas las estaciones de servicio terrestres con sus precios. No hace falta registrarse ni pedir una clave. Cada estación viene con campos como `Rótulo`, `Dirección`, `Municipio`, `Provincia`, `Horario`, `Latitud`, `Longitud (WGS84)` y un precio por cada combustible (`Precio Gasolina 95 E5`, `Precio Gasoleo A`…).

> Son datos abiertos: cualquiera puede reutilizarlos, y eso es lo que hace posible un proyecto así sin pagar a nadie.

## Cómo está organizado

Separé la aplicación en capas para que cada parte hiciera una sola cosa y pudiera cambiarla sin romper el resto:

<figure class="ancha">
  <img src="/img/gasolineras-arquitectura.svg" alt="Diagrama de capas: API del Ministerio, lector, parser, modelo y vista Swing" width="1200" height="300" loading="lazy">
  <figcaption>Flujo de datos de la aplicación, de la API a la tabla que ve el usuario.</figcaption>
</figure>

1. **Lector**: descarga el JSON (o lo lee de un fichero guardado, que me vino muy bien para probar sin depender de la red).
2. **Parser**: convierte cada estación en un objeto `Estacion` con tipos de verdad (`double` para los precios, no `String`).
3. **Modelo**: una `List<Estacion>` envuelta en un `AbstractTableModel`, con los filtros por provincia, combustible y municipio.
4. **Vista**: una ventana Swing con una `JTable` y un `TableRowSorter` para ordenar por cualquier columna con un clic.

## Los detalles que dieron guerra

**La coma decimal.** Los precios llegan como texto con formato español: `"1,589"`. `Double.parseDouble` espera un punto, así que el primer intento reventó con `NumberFormatException`. Lo resolví normalizando antes de convertir:

```java
static double precio(String valor) {
    if (valor == null || valor.isBlank()) return Double.NaN; // no vende ese combustible
    return Double.parseDouble(valor.trim().replace(',', '.'));
}
```

**Campos vacíos.** No todas las estaciones venden todos los combustibles; cuando no hay precio el campo llega vacío. Usar `NaN` y mandar esas filas al final al ordenar fue más limpio que inventar un cero, que las habría puesto las primeras.

**La interfaz congelada.** La descarga tarda unos segundos y, si se hace en el hilo de eventos de Swing, la ventana se queda bloqueada. Moví la descarga y el parseo a un `SwingWorker` y solo actualizo la tabla en `done()`, que ya se ejecuta en el hilo correcto.

**Las tildes.** Leer la respuesta sin indicar la codificación convertía «Logroño» en algo ilegible. Leer siempre con `StandardCharsets.UTF_8` lo arregló.

<figure>
  <img src="/img/gasolineras-ventana.svg" alt="Ventana con filtros de provincia y combustible y una tabla de estaciones ordenada por precio" width="1200" height="560" loading="lazy">
  <figcaption>Esquema de la ventana principal: filtros arriba y tabla ordenable debajo (datos de ejemplo).</figcaption>
</figure>

## Qué haría ahora

- **Guardar un histórico** en SQLite para ver cómo evoluciona el precio de cada estación y detectar qué día de la semana sale más barato.
- **Ordenar por distancia** usando la latitud y longitud que ya vienen en los datos (fórmula de Haversine).
- **Separar la lógica de Swing** del todo para poder reutilizarla en una versión web.

Lo más útil del proyecto no fue la aplicación en sí, sino ver lo mucho que se puede construir con datos abiertos y un par de clases bien separadas.
