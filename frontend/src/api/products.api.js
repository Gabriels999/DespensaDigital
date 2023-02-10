import api from "./config.js";
import apiHelpers from "./helpers.js";

export default {
  getProducts: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/products/list_products")
        .then((response) => {
          return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
  addNeTask: (description) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/add_todo", apiHelpers.dataToForm({ description }))
        .then((response) => {
          return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
  updateProduct: (product) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/update_product/", apiHelpers.dataToForm(product))
        .then((response) => {
          return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
  deleteProduct: (id) => {
    return new Promise((resolve, reject) => {
      api // Isso aqui nao faz sentido, pedir ajuda
      .post('/api/products/delete_product/', apiHelpers.dataToForm({id}))
      .then((response) => {
        return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
};
