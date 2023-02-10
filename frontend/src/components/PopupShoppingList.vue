<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" scrollable>
            <template v-slot:activator="{ props }">
                <v-btn color="primary" v-bind="props" @click="generateShoppingList">
                    Gerar Lista de Compras
                </v-btn>
            </template>
            <v-card>
                <v-card-title>Shopping List</v-card-title>
                <v-divider></v-divider>
                <div v-for="item in shoppingList" :key="item.id">
                    <v-card-text>
                        <p>{{ item.name }}</p>
                        <p>Precisa comprar: {{ item.target_quantity - item.real_quantity }}</p>
                        <p>Ultimo preco: {{ item.price }}</p>
                        <p>Tipo: {{ item.type }}</p>
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
    props: {
        shoppingList: {
            type: Object,
        },
    },
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