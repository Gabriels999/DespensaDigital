<template>
  <v-col cols="auto">
    <v-dialog transition="dialog-bottom-transition" max-width="600" v-model="dialog">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" v-bind="props"> Registrar Produto</v-btn>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card>
          <v-col cols="12">
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="name"
                :rules="[(v) => !!v || 'Insira um nome valido']"
                label="Name"
              ></v-text-field>
              <v-text-field
                v-model="price"
                label="Preco"
                :rules="[(v) => !!v || 'Insira um preco valido']"
              ></v-text-field>
              <v-select
                v-model="typePicker"
                :items="types"
                :rules="[(v) => !!v || 'Selecione um tipo']"
                label="Tipo"
                required
              ></v-select>
              <v-checkbox
                v-model="addToUserStore"
                label="Adicionar este item na sua despensa ?"
              ></v-checkbox>
              <div v-show="addToUserStore">
                  <v-text-field
                  v-model="target_quantity"
                  label="Quantidade para estoque"
                ></v-text-field>
                <v-text-field
                  v-model="real_quantity"
                  label="Quantidade atual"
                ></v-text-field>
              </div>
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
  name: "PopupRegisterProduct",
  emits: ['registerProduct'],
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
      addToUserStore: true
    };
  },
  methods: {
    async validate() {
      const { valid } = await this.$refs.form.validate()
      if (valid){
        this.registerProduct();
      }
    },
    registerProduct() {
      const newProduct = {
        name: this.name,
        price: this.price,
        type: this.typePicker,
      };
      if(this.addToUserStore){
        newProduct["target_quantity"] = this.target_quantity
        newProduct["real_quantity"] = this.real_quantity
      }
      this.$emit('registerProduct', newProduct)
    },
    closePopup(){
      this.product = null
      this.name = null
      this.price = null
      this.typePicker = null
      this.dialog = false
    }
  }
};
</script>
