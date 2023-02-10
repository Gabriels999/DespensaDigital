<template>
  <v-card>
    <v-card-text>
      <div>#{{ product.id }}</div>
    <p class="ma-0 pa-0 text-h5 text--primary">
      {{ product.name }}
    </p>
    <p class="ma-0 pa-0 text-h5 text--primary">
      {{ product.type }}
    </p>
    <p class="ma-0 pa-0 text-h5 text--primary">
      {{ product.price }}
    </p>
    <p class="ma-0 pa-0 text-h5 text--primary">
      {{ product.target_quantity }}
    </p>
    <p class="ma-0 pa-0 text-h5 text--primary">
      {{ product.real_quantity }}
    </p>
    </v-card-text>
    <v-col cols="6">
      <PopupEditProducts 
      :product="product" 
      @updateProduct="updateProduct"
      />
      <v-btn :loading="loading" class="ma-1" color="error" plain @click="deleteProduct(product)">
        Delete
      </v-btn>
      <v-btn class="ma-1" color="light-blue-lighten-2" plain @click="useProduct(product)">
        Use Product
      </v-btn>
    </v-col>
  </v-card>
</template>

<script>

import PopupEditProducts from "@/components/PopupEditProducts.vue";

export default {
  name: "ProductModel",
  emits: ['delProduct', 'upProduct', 'useProduct'],
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
      this.$emit("delProduct", item.id)
    },
    updateProduct(item){
      this.$emit('upProduct', item)
    },
    useProduct(item){
      this.$emit('useProduct', item)
    }
  },
}
</script>
