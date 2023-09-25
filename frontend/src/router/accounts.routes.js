// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import LoginView from "@/views/accounts/LoginView.vue"
import SignupView from "@/views/accounts/SignupView.vue"
import LogoutView from "@/views/accounts/LogoutView.vue"

export default [
  {
    path: "/accounts",
    component: EmptyLayout,
    children: [
      {
        path: "login",
        name: "accounts-login",
        component: LoginView,
      },
      {
        path: "signup",
        name: "accounts-signup",
        component: SignupView,
      },
      {
        path: "logout",
        name: "accounts-logout",
        component: LogoutView,
      },
    ],
  },
]
