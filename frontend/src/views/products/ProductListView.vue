<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline">
            Products
          </v-card-title>
        </v-card>
      </v-col>
      <PopupShoppingList/>
      <PopupAddProducts @addProduct="addProduct" :productList=allProductsList />
      <v-btn>Adicionar produto na despensa</v-btn>
    </v-row>
    <v-row>
      <v-card class="d-flex mx-4" v-for="item in productsList" :key="item.id">
        <product
        :product="item.product"
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
import PopupAddProducts from "@/components/PopupAddProducts.vue";
import PopupShoppingList from "@/components/PopupShoppingList.vue";

export default {
  name: "ProductsList",
  components: {
    Product, PopupAddProducts, PopupShoppingList },
  setup() {
    const appStore = useAppStore()
    const userStore = useAccountsStore()
    return { appStore, userStore }
  },
  data() {
    return {
      loading: false,
      productsList: [],
      allProductsList: [],
      user: this.userStore.loggedUser,
    }
  },
  mounted() {
    this.getUserProducts()
    this.getAllProducts()
  },
  methods: {
    getAllProducts(){
      this.loading = true
      API.getAllProducts().then((data)=> {
        this.allProductsList = data.products
        this.loading = false
      })
    },
    getUserProducts() {
      this.loading = true
      API.getUserProducts().then((data) => {
        this.productsList = data.products
        this.loading = false
      })
    },
    addProduct(product) {
      this.loading = true
      debugger
      API.addProduct(product).then((product) => {
        this.appStore.showSnackbar(`Novo produto adicionado! #${product.id}`)
        this.getUserProducts()
        this.loading = false
      })
    },
    updateProduct(product) {
      this.loading = true
      API.updateProduct(product).then((product) => {
        this.appStore.showSnackbar(`O produto ${product.name} foi editado!`)
        this.getUserProducts()
        this.loading = false
      })
    },
    deleteProduct(id) {
      this.loading = true
      API.deleteProduct(id).then(() => {
        this.appStore.showSnackbar('Produto deletado.')
        this.getUserProducts()
        this.loading = false
      });
    },
    useProduct(item){
      if (item.real_quantity > 0){
        API.useProduct(item.id).then(()=>{
          this.appStore.showSnackbar('Produto consumido!')
          this.getUserProducts()
        })
      }
      else{
        this.appStore.showSnackbar('Esse produto já está zerado!')
      }
    },
    shopProduct(id){
        API.shopProduct(id).then(()=>{
          this.appStore.showSnackbar('Produto abastecido!')
          this.getUserProducts()
        })
      }
    }
}
</script>

<style scoped>
</style>
