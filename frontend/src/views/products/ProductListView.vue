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
    </v-row>
    <v-row>
      <v-card class="d-flex mx-4" v-for="item in productsList" :key="item.id">
        <product
        :product="item" 
        @delProduct="deleteProduct" 
        @upProduct="updateProduct"
        @useProduct="useProduct"
        @shopProduct="shopProduct"
        />
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"
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
    const userStore = useAccountsStore()
    return { appStore, userStore }
  },
  data() {
    return {
      loading: false,
      productsList: [],
      user: this.userStore.loggedUser
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
      API.createProduct(product, this.user.id).then((product) => {
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
      if (item.real_quantity > 0){
        API.useProduct(item.id).then(()=>{
          this.appStore.showSnackbar('Produto consumido!')
          this.getProducts()
        })
      }
      else{
        this.appStore.showSnackbar('Esse produto já está zerado!')
      }
    },
    shopProduct(id){
        API.shopProduct(id).then(()=>{
          this.appStore.showSnackbar('Produto abastecido!')
          this.getProducts()
        })
      }
    }
}
</script>

<style scoped>
</style>
