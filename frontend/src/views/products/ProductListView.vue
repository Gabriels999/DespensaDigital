<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Tasks </v-card-title>
        </v-card>
      </v-col>
      <PopupCreateProducts @createProduct="createProduct"/>
      <v-col v-for="item in items" :key="item.id" cols="12">
        <product 
        :product="item" 
        @delProduct="deleteProduct" 
        @upProduct="updateProduct"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import API from "@/api/products.api.js"
import Product from "@/components/Product.vue"
import PopupCreateProducts from "@/components/PopupCreateProducts.vue";

export default {
  name: "ProductsList",
  components: { Product, PopupCreateProducts },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      items: [],
    }
  },
  mounted() {
    this.getProducts()
  },
  methods: {
    getProducts() {
      this.loading = true
      API.getProducts().then((data) => {
        this.items = data.products
        this.loading = false
      })
    },
    createProduct(product) {
      this.loading = true
      console.log(product)
      API.createProduct(product).then((product) => {
        this.appStore.showSnackbar(`Nova tarefa adicionada #${product.id}`)
        this.getProducts()
        this.loading = false
      })
    },
    updateProduct(obj) {
      this.loading = true
      console.log(obj)
      debugger
      API.updateProduct(obj).then((obj) => {
        this.appStore.showSnackbar(`Novo produto adicionado! #${obj.id}`)
        this.getProducts()
        this.loading = false
      })
    },
    deleteProduct(id) {
      this.loading = true
      API.deleteProduct(id).then(() => {
        this.appStore.showSnackbar('Produto deletado.')
        this.getProducts()
        this.loading = false
      });
    }
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
