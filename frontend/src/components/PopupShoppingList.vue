<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" scrollable>
            <template v-slot:activator="{ props }">
                <v-btn color="primary" v-bind="props" class="py-0" @click="generateShoppingList">
                    Gerar Lista de Compras
                </v-btn>
            </template>
            <v-card>
                <v-card-title>Shopping List</v-card-title>
                <v-divider></v-divider>
                <v-card-text v-if="shoppingList.length == 0">
                        <p>Sua lista está vazia!</p>
                    </v-card-text>
                <div v-for="item in shoppingList" :key="item.id">
                    <v-card-text>
                        <p>{{ item.product.name }}</p>
                        <p>Precisa comprar: {{ item.product.target_quantity - item.product.real_quantity }}</p>
                        <!-- <p>Ultimo preco: R$ {{ item.product.price }}</p> -->
                        <!-- <p>Total esperado: R$ {{ item.product.expected_total }}</p> -->
                        <p>Tipo: {{ item.product.type }}</p>
                    </v-card-text>
                </div>
                <v-card-actions>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script>

import API from "@/api/products.api.js"

export default {
    name:"PopupShoppingList",
    data() {
        return {
            dialogm1: '',
            dialog: false,
            shoppingList: [],
        }
    },
    methods:{
        generateShoppingList() {
            API.getShoppingList().then((data) => {
                this.shoppingList = data.products
            })
        },
    }
}
</script>