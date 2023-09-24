<template>
  <v-container>
    <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Login</h1> </v-sheet>
        <v-form>
          <v-text-field
            v-model="username"
            label="Username"
            prepend-inner-icon="mdi-email-fast-outline"
            variant="outlined"
            required></v-text-field>

          <v-text-field
            v-model="password"
            type="password"
            label="Password"
            prepend-inner-icon="mdi-key-outline"
            variant="outlined"
            required></v-text-field>
          <v-text-field
            v-model="confPassword"
            type="password"
            label="Confirm password"
            prepend-inner-icon="mdi-key-outline"
            variant="outlined"
            required></v-text-field>

          <v-btn
            class="my-2"
            block
            size="large"
            rounded="pill"
            color="primary"
            variant="outlined"
            append-icon="mdi-chevron-right"
            :disabled="password !== confPassword"
            @click="signup">
            Save
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AccountsApi from "@/api/accounts.api.js"
import { useAppStore } from "@/stores/appStore"

export default {
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data: () => {
    return {
      loading: false,
      valid: false,
      username: "",
      password: "",
      confPassword: "",
      error: false,
    }
  },
  methods: {
    signup() {
      this.loading = true
      AccountsApi.signup(this.username, this.password)
        .then((response) => {
          if (!response) {
            this.appStore.showSnackbar("Houve um problema. Por favor, tente novamente.", "danger")
            return
          }
          this.showLogin()
        })
        .finally(() => {
          this.loading = false
        })
    },
    showLogin() {
      this.$router.push({ name: "accounts-login" })
    },
  },
}
</script>
