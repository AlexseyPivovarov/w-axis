axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

new Vue({
   el: '#product',
   delimiters: ['${','}'],
   data: {
       products: [],
       loading: false,
       flag: [],
   },
   mounted: function() {
        this.getProducts();
   },
   methods: {
        getProducts: function() {
              this.loading = true;
              axios.get('/api/products/').then((response) => {
                    this.products = response.data;
                    this.loading = false;
                  })
                  .catch((err) => {
                   this.loading = false;
                   console.log(err);
                  })
        },
    },
})