const data = require("../data");
const accounts = require("./accounts");

function getMaxId(items) {
  return Math.max(...items.map((item) => item.id));
}

module.exports = {
  list: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { id } = req.params;
    if (id != undefined) {
      const userStore = data.userStore.find((t) => t.ownerId == id);
      if (!userStore || userStore.ownerId != loggedUser.id) {
        res.status(404).end();
        return;
      }
      res.send(userStore);
      return;
    }
    const response = {
      userStoreList: data.userStore.filter((t) => t.ownerId == loggedUser.id),
    };
    res.send(response);
  },
  add: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { description } = req.body;
    const id = getMaxId(data.products) + 1;
    const newTask = {
      id,
      description,
      userId: loggedUser.id,
    };
    data.products.push(newTask);
    res.send(newTask);
  },
};
