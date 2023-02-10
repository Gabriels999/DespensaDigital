// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import ProductListView from "@/views/products/ProductListView.vue"

export default [
  {
    path: "/products",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "products-list",
        component: ProductListView,
      },
    ],
  },
]
