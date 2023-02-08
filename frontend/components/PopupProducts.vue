<template>
  <v-col cols="auto">
    <v-dialog transition="dialog-bottom-transition" max-width="600">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" v-bind="attrs" v-on="on">{{ title }}</v-btn>
      </template>
      <template v-slot:default="dialog">
        <v-card>
          <v-col cols="12">
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="name"
                :rules="[(v) => !!v || 'Insira um nome valido']"
                label="Name"
                required
              ></v-text-field>

              <v-text-field
                v-model="price"
                label="Preco"
                :rules="[(v) => !!v || 'Insira um preco valido']"
                required
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
              ></v-select>

              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="validate"
              >
                {{ product ? "Editar" : "Criar" }}
              </v-btn>
              <v-card-actions class="justify-end">
                <v-btn class="error" text @click="dialog.value = false"
                  >Cancelar</v-btn
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

import API from "~/api/productsmock";

export default {
  name: "TasksList",
  props: {
    title: {
      type: String,
      required: true,
    },
    product: {
      default: () => {},
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
    validate() {
      debugger;
      if (this.$refs.form.validate()) {
        this.product ? this.editProduct() : this.addProduct();
      }
    },
    addProduct() {
      const newProduct = {
        name: this.name,
        type: this.typePicker,
        price: this.price,
        target_quantity: this.target_quantity,
        real_quantity: this.real_quantity,
      };
      API.addProduct(newProduct).then(() => {
        //TODO: fazer fechar sozinho depois disso
      });
    },
    editProduct() {
      this.$refs.form.validate();
      const updatedProduct = {
        id: this.product.id,
        name: this.name,
        type: this.typePicker,
        price: this.price,
        target_quantity: this.target_quantity,
        real_quantity: this.real_quantity,
      };
      API.updateProduct(updatedProduct).then(() => {
        //TODO: fazer fechar sozinho depois disso
      });
    },
  },
};
</script>
