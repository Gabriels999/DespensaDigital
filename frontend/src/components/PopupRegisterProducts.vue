<template>
  <v-col cols="auto">
    <v-dialog transition="dialog-bottom-transition" max-width="600">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" v-bind="props"> <v-icon icon="mdi-plus"></v-icon></v-btn>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card>
          <v-col cols="12">
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="name"
                :rules="[(v) => !!v || 'Insira um nome valido']"
                label="Name"
                disabled
              ></v-text-field>
              <v-text-field
                v-model="price"
                label="Preco"
                :rules="[(v) => !!v || 'Insira um preco valido']"
                disabled
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
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="validate"
              >
                Criar
              </v-btn>
              <v-card-actions class="justify-end">
                <v-btn class="error" text @click="closePopup"
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

export default {
  name: "PopupCreateProduct",
  emits: ['addProduct'],
  props: {
    productList: {
      type: Array
    }
  },
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
      product: null,
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
        product: this.product,
        target_quantity: this.target_quantity,
        real_quantity: this.real_quantity,
      };
      this.$emit('addProduct', newProduct)
    },
    closePopup(){
      this.product = null
      this.name = null
      this.price = null // dar um jeito de permitir virgula nesse valor
      this.typePicker = null
      debugger
      isActive.value = false
    }
  },
  watch:{
    product(){
      this.productList.forEach(item =>{
        if(item.name == this.product){
          this.name = item.name
          this.price = item.price // dar um jeito de permitir virgula nesse valor
          this.typePicker = item.type
        }
      })
    }
  }
};
</script>
