<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Products </v-card-title>
        </v-card>
      </v-col>
      <PopupShoppingList/>
      <PopupCreateProducts @createProduct="createProduct"/>
      <v-col v-for="item in productsList" :key="item.id" cols="12">
        <product 
        :product="item" 
        @delProduct="deleteProduct" 
        @upProduct="updateProduct"
        @useProduct="useProduct"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import API from "@/api/products.api.js"
import Product from "@/components/Product.vue"
import PopupCreateProducts from "@/components/PopupCreateProducts.vue";
import PopupShoppingList from "@/components/PopupShoppingList.vue";

export default {
  name: "ProductsList",
  components: {
    Product, PopupCreateProducts, PopupShoppingList },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      productsList: [],
    }
  },
  mounted() {
    this.getProducts()
  },
  methods: {
    getProducts() {
      this.loading = true
      API.getProducts().then((data) => {
        this.productsList = data.products
        this.loading = false
      })
    },
    createProduct(product) {
      this.loading = true
      API.createProduct(product).then((product) => {
        this.appStore.showSnackbar(`Novo produto adicionado! #${product.id}`)
        this.getProducts()
        this.loading = false
      })
    },
    updateProduct(product) {
      this.loading = true
      API.updateProduct(product).then((product) => {
        this.appStore.showSnackbar(`O produto ${product.name} foi editado!`)
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
    },
    useProduct(item){
      //TODO se for 0, levantar um erro
      if (item.real_quantity > 0){
        API.useProduct(item).then(()=>{
          this.appStore.showSnackbar('Produto consumido!')
          this.getProducts()
        })
      }
      else{
        this.appStore.showSnackbar('Esse produto já está zerado!')
      }
    }
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
