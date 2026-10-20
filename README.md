# Bitácora — blog estático con Eleventy

Actividad 1 de **Desarrollo de Aplicaciones en Red** (Grado en Ingeniería Informática, UNIR).
Autor: Abraham Rajo Rodríguez.

**Web publicada:** https://abrahamrrr180-netizen.github.io/TrabajoDesarrolloDeAplicaciones/

## Qué es

Un blog con tres entradas (texto + imágenes), hecho con HTML y CSS propios y generado con
[Eleventy](https://www.11ty.dev/). No usa JavaScript en el navegador.

- Inicio con la lista de entradas (imagen, fecha y resumen).
- Página de cada entrada con sus etiquetas y enlaces a la entrada anterior/siguiente.
- Archivo, índice de etiquetas y una página por etiqueta.
- Página «Sobre mí» y página 404 propia.
- Diseño sencillo y adaptable a móvil.

## Estructura

```
src/                  Código fuente
├─ _data/site.json    Datos globales (título, autor, lema)
├─ _includes/         Plantillas Nunjucks: base, entrada y tarjeta
├─ css/style.css      Hoja de estilos única
├─ img/               Ilustraciones SVG
├─ posts/             Entradas en Markdown (+ datos comunes)
└─ *.njk / *.md       Inicio, archivo, etiquetas, sobre mí y 404
docs/                 Web generada (es la que sirve GitHub Pages)
herramientas/         Script de Python que genera las ilustraciones SVG
eleventy.config.js    Configuración: colecciones, filtros y rutas
```

## Compilar en local

```bash
npm install
npm run serve                     # http://localhost:8080
PATH_PREFIX=/TrabajoDesarrolloDeAplicaciones/ npm run build   # genera docs/ para GitHub Pages
```

## Publicación

GitHub Pages sirve la carpeta `docs/` de la rama `main`
(*Settings → Pages → Deploy from a branch → main /docs*).
