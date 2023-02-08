<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-card>
        <v-card-title class="headline"> Produtos </v-card-title>
      </v-card>
    </v-col>

    <PopupProducts title="Cadastrar Produtos" :product="false" />

    <v-col v-for="item in items" :key="item.id" cols="12">
      <v-card>
        <v-card-text>
          <div>#{{ item.id }}</div>
          <p class="ma-0 pa-0 text-h5 text--primary">
            {{ item.name }}
          </p>
          <p class="ma-0 pa-0 text-h5 text--primary">
            {{ item.type }}
          </p>
          <p class="ma-0 pa-0 text-h5 text--primary">
            {{ item.price }}
          </p>
          <p class="ma-0 pa-0 text-h5 text--primary">
            {{ item.target_quantity }}
          </p>
          <p class="ma-0 pa-0 text-h5 text--primary">
            {{ item.real_quantity }}
          </p>
        </v-card-text>
        <v-col cols="6">
          <PopupProducts title="Editar Produto" :product="item" />
          <v-btn
            :loading="loading"
            class="ma-1"
            color="error"
            plain
            @click="deleteProduct(item)"
          >
            Delete
          </v-btn>
        </v-col>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import PopupProducts from "@/components/PopupProducts.vue";
import TasksApi from "@/api/tasks.api";
import API from "~/api/productsmock";

export default {
  name: "TasksList",
  components: { PopupProducts },

  data() {
    return {
      valid: true,
      name: "",
      price: 0,
      target_quantity: 0,
      real_quantity: 0,
      quantityRule: [(v) => !!v || "Insira uma quantidade valida"],

      typePicker: null,
      types: ["Congelados & Refrigerados", "Secos", "Limpeza", "Higiene"],
      loading: false,
      items: [],
    };
  },
  mounted() {
    this.listProducts();
  },
  methods: {
    listProducts() {
      this.loading = true;
      API.getProducts().then((data) => {
        this.items = data;
        this.loading = false;
      });
    },
    deleteProduct(product) {
      API.deleteProduct(product).then((data) => {
        this.listProducts();
      });
    },
  },
};
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
