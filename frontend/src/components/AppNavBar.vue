<template>
  <v-app-bar>
    <template #append>
      <v-btn icon="mdi-heart" :to="{ name: 'base-home' }"><v-app-bar-title>{{ title }}</v-app-bar-title></v-btn>
      <v-btn></v-btn>
      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click.stop="themeClick"></v-btn>

      <v-btn icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item :to="{ name: 'accounts-logout' }"> Sair </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "Despensa Digital",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
  },
}
</script>
