import api from "./config.js";
import apiHelpers from "./helpers.js";

export default {
  getAllProducts: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/products/list_all_products")
        .then((response) => {
          return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
  getUserProducts: () => {
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
  addProduct: (product) => {
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
  createProduct: (product) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/register_product", apiHelpers.dataToForm(product))
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
  shopProduct: (id) => {
    return new Promise((resolve, reject) => {
      api
      .post(`/api/products/shop_product/${id}`, apiHelpers.dataToForm({id}))
      .then((response) => {
        return resolve(response.data);
      })
        .catch((error) => {
          return reject(error);
        });
    });
  },
  getShoppingList: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/products/shopping_list")
        .then((response) => {
          return resolve(response.data);
        })
        .catch((error) => {
          return reject(error);
        });
    });
  },
};
