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
  createProduct: (product) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/add_product", apiHelpers.dataToForm(product))
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
        .post(`/api/products/edit_product/${product.id}`, apiHelpers.dataToForm(product))
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
      api
      .post(`/api/products/delete_product/${id}`, apiHelpers.dataToForm({id}))
      .then((response) => {
        return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
  useProduct: (id) => {
    return new Promise((resolve, reject) => {
      api
      .post(`/api/products/use_product/${id}`, apiHelpers.dataToForm({id}))
      .then((response) => {
        return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
};
