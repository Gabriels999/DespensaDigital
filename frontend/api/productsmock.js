function later(result) {
  return new Promise(function (resolve) {
    setTimeout(() => {
      resolve(result);
    }, 500);
  });
}

let products = [
  {
    id: 1,
    name: "Ketchup",
    type: "Secos",
    price: 99.9,
    target_quantity: 1,
    real_quantity: 0,
  },
  {
    id: 2,
    name: "Maionese",
    type: "Secos",
    price: 19.9,
    target_quantity: 1,
    real_quantity: 0,
  },
];

export default {
  getProducts: () => {
    return later(products);
  },
  addProduct: (product) => {
    products.push(product);
    console.log(`${product} criado`);
    return later(products);
  },
  updateProduct: (product) => {
    console.log(`${product} atualizado`);
    return later(products);
  },
  deleteProduct: (product) => {
    console.log(`${product} apagado`);
    return later(products);
  },
};
