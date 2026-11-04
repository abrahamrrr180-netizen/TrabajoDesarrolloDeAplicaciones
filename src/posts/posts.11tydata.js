export default {
  layout: "post.njk",
  permalink: "/entradas/{{ page.fileSlug }}/",
  eleventyComputed: {
    anio: (data) => data.page.date.getUTCFullYear(),
  },
};
