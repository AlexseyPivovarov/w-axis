axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

new Vue({
   el: '#cart',
   delimiters: ['${','}'],
   data: {
       carts: [],
       loading: false,
   },
   mounted: function() {
        this.getCartList();
   },
   methods: {
        getCartList: function() {
              this.loading = true;
              axios.get('/api/cartlist/').then((response) => {
                    this.carts = response.data;
                    this.loading = false;
                  })
                  .catch((err) => {
                   this.loading = false;
                   console.log(err);
                  })
        },
        delCart: function(id) {
            axios.delete('/api/del/' + id).then(this.getCartList)
            .catch((err) => {
            this.loading = false;
            console.log(err);
            })
        },
        edit: function(id) {
            window.location.href= 'Update/' + id;
        },
    },
})