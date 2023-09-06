<template>
  <v-card class="mx-auto" max-width="400">
    <v-card-title>{{ product.name }}</v-card-title>
    <v-card-subtitle class="d-flex justify-space-between">
      #{{ product.id }}
      <v-chip label class="">
        {{ product.type }}
      </v-chip>
    </v-card-subtitle>
    <v-card-text>
      <div>
        Preco: {{ product.price }}
      </div>
      <div>Ideal: {{ product.target_quantity }}</div>
      <div>Em estoque: {{ product.real_quantity }}</div>
    </v-card-text>
    <v-card-actions>
      <PopupEditProducts :product="product" @updateProduct="updateProduct" />
      <v-btn class="ma-1" color="light-blue-lighten-2" plain @click="useProduct(product)">
        Usei
      </v-btn>
      <v-btn class="ma-1" color="success" @click="shopProduct(product)" plain>
        Abasteci
      </v-btn>
      <v-btn :loading="loading" class="d-flex flex-row-reverse" icon="mdi-close-circle" color="error"
        @click="deleteProduct(product)">
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

import PopupEditProducts from "@/components/PopupEditProducts.vue";

export default {
  name: "ProductModel",
  emits: ['delProduct', 'upProduct', 'useProduct', 'shopProduct'],
  components: { PopupEditProducts },
  props: {
    product: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      loading: false,
    };
  }, 
  methods: {
    deleteProduct(item) {
      this.$emit("delProduct", {id: item.id, name: item.name})
    },
    updateProduct(item){
      this.$emit('upProduct', item)
    },
    useProduct(item){
      this.$emit('useProduct', item)
    },
    shopProduct(item){
      this.$emit('shopProduct', item.id)
    }
  },
}
</script>
