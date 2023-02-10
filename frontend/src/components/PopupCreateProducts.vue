<template>
  <v-col cols="auto">
    <v-dialog transition="dialog-bottom-transition" max-width="600">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" v-bind="props">Cadastrar Produto</v-btn>
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
                Criar
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
  name: "PopupCreateProduct",
  emits: ['createProduct'],

  data() {
    return {
      valid: true,
      name: '',
      price: null,
      target_quantity: null,
      real_quantity: null,
      typePicker: null,
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
    async validate() {
      const { valid } = await this.$refs.form.validate()
      if (valid){
        this.addProduct();
      }
    },
    addProduct() {
      const newProduct = {
        name: this.name,
        price: this.price, // dar um jeito de permitir , nesse valor
        type: this.typePicker,
        target_quantity: this.target_quantity,
        real_quantity: this.real_quantity,
      };
      this.$emit('createProduct', newProduct)
    },
  },
};
</script>
