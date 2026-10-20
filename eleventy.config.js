import { HtmlBasePlugin } from "@11ty/eleventy";

const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
  "agosto", "septiembre", "octubre", "noviembre", "diciembre"];

export default function (eleventyConfig) {
  eleventyConfig.addPlugin(HtmlBasePlugin);
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/img");
  eleventyConfig.addPassthroughCopy({ "src/.nojekyll": ".nojekyll" });

  // Fechas en castellano: "20 de octubre de 2026"
  eleventyConfig.addFilter("fecha", (d) =>
    `${d.getUTCDate()} de ${MESES[d.getUTCMonth()]} de ${d.getUTCFullYear()}`);
  eleventyConfig.addFilter("fechaISO", (d) => d.toISOString().slice(0, 10));
  eleventyConfig.addFilter("anio", (d) => d.getUTCFullYear());

  // Minutos de lectura aproximados (200 palabras/min)
  eleventyConfig.addFilter("lectura", (html) => {
    const palabras = String(html).replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(palabras / 200));
  });

  // Colección de entradas, de más reciente a más antigua
  eleventyConfig.addCollection("entradas", (api) =>
    api.getFilteredByGlob("src/posts/*.md").sort((a, b) => b.date - a.date));

  // Lista de etiquetas únicas (sin la etiqueta interna "post")
  eleventyConfig.addCollection("etiquetas", (api) => {
    const set = new Set();
    api.getFilteredByGlob("src/posts/*.md").forEach((p) =>
      (p.data.tags || []).filter((t) => t !== "post").forEach((t) => set.add(t)));
    return [...set].sort();
  });

  eleventyConfig.addFilter("slugTag", (t) =>
    t.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/\s+/g, "-"));

  return {
    dir: { input: "src", output: "docs", includes: "_includes", data: "_data" },
    pathPrefix: process.env.PATH_PREFIX || "/",
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
}
