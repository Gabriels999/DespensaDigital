<template>
  <v-col cols="auto">
    <v-dialog transition="dialog-bottom-transition" max-width="600" v-model="dialog">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" v-bind="props" class="py-0"> <v-icon icon="mdi-plus" class="py-0"></v-icon></v-btn>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card>
          <v-col cols="12">
            <v-autocomplete
                  v-model="product"
                  :items="productList"
                  item-title="name"
                  color="white"
                  hide-no-data
                  item-text="Produto"
                  label="Produto"
                  placeholder="Insira um produto"
                ></v-autocomplete>
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
  name: "PopupAddProduct",
  emits: ['addProduct', 'update:isActive'],
  props: {
    productList: {
      type: Array
    }
  },
  data() {
    return {
      dialog: false,
      valid: true,
      name: '',
      productId: null,
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
        id: this.productId,
        name: this.name,
        target_quantity: this.target_quantity,
        real_quantity: this.real_quantity,
      };
      this.$emit('addProduct', newProduct)
      this.dialog = false
    },
    closePopup(){
      this.product = null
      this.name = null
      this.price = null
      this.typePicker = null
      this.target_quantity = null,
      this.real_quantity = null,
      this.dialog = false
    }
  },
  watch:{
    product(){
      this.productList.forEach(item =>{
        if(item.name == this.product){
          this.productId = item.id
          this.name = item.name
          this.price = item.price
          this.typePicker = item.type
        }
      })
    }
  }
};
</script>
