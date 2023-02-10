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
                {{ shoppingList }}
                <v-card-text style="height: 300px;">
                </v-card-text>
                <v-divider></v-divider>
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
            default: null,
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