const routerBase = process.env.DEPLOY_ENV === 'GH_PAGES' ? {
  router: {
    base: '/sprites-as-a-service/'
  }
} : {}

const favicon = process.env.DEPLOY_ENV === 'GH_PAGES' ? '/sprites-as-a-service/favicon.ico' : '/favicon.ico'

export default {
  ...routerBase,
  mode: 'spa',
  /*
  ** Environment variables
  */
  env: {
    baseurl: process.env.BASE_URL || 'http://localhost:8080/api/v1/sprite'
  },
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: favicon }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
      "pattern.css/dist/pattern.min.css",
      "nes.css/css/nes.min.css",
      "shorthandcss/dist/shorthand.min.css",
      "@fortawesome/fontawesome-free/css/all.min.css"
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
