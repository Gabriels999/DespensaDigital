<template>
  <v-col cols="auto">
    <v-dialog transition="dialog-bottom-transition" max-width="600">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" v-bind="props">Editar</v-btn>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card>
          <v-col cols="12">
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="name"
                :rules="[(v) => !!v || 'Insira um nome valido']"
                label="Name"
                required
                disabled
              ></v-text-field>
              <v-text-field
                v-model="price"
                label="Preco"
                :rules="[(v) => !!v || 'Insira um preco valido']"
                required
                disabled
              ></v-text-field>
              <v-text-field
                v-model="target_quantity"
                :rules="[(v) => !!v || 'Insira uma quantidade valida']"
                label="Quantidade para estoque"
                required
              ></v-text-field>
              <v-text-field
                v-model="real_quantity"
                :rules="[(v) => !!v || 'Insira uma quantidade valida']"
                label="Quantidade atual"
                required
              ></v-text-field>
              <v-select
                v-model="typePicker"
                :items="types"
                :rules="[(v) => !!v || 'Selecione um tipo']"
                label="Tipo"
                required
                disabled
              ></v-select>
              <v-btn
                color="success"
                class="mr-4"
                @click="editProduct"
              >
              Editar
              </v-btn>
              <v-card-actions class="justify-end">
                <v-btn class="error" text @click="isActive.value = false"
                  >Fechar</v-btn
                >
              </v-card-actions>
            </v-form>
          </v-col>
        </v-card>
      </template>
    </v-dialog>
  </v-col>
</template>

<script>
//TODO: Tem um jeito de fazer fechar diretamente como na linha 65 sem perder a oportunidade de usar a funcao na linha 59?

export default {
  name: "PopupEditProduct",
  emits: ['updateProduct'],
  props: {
    product: {
      type: Object,
      default: () => {},
      required: true
    },
  },

  data() {
    return {
      valid: true,
      name: this.product.name,
      price: this.product.price,
      target_quantity: this.product.target_quantity,
      real_quantity: this.product.real_quantity,
      typePicker: this.product.type,
      types: [
        "Congelados",
        "Refrigerados",
        "Secos",
        "Hortifruti",
        "Frutas",
        "Limpeza",
        "Higiene",
      ],
    };
  },
  methods: {
    editProduct() {
      const updatedProduct = {
        id: this.product.id,
        name: this.name,
        type: this.typePicker,
        price: this.price,
        target_quantity: this.target_quantity,
        real_quantity: this.real_quantity,
      };
      this.$emit('updateProduct', updatedProduct)
    },
  },
};
</script>
