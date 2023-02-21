const utils = require('../utils')

module.exports = {
  users: utils.parseJson('./data/users.json'),
  products: utils.parseJson('./data/products.json'),
  userStore: utils.parseJson('./data/userStore.json'),
}
