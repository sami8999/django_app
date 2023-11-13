<template>
    <div id="app" class="container my-4">
      <h1 class="mb-4">Cat adoption centre</h1>
  
      <ListCat :key="state" @catRefresh="refreshCats" class="mt-4" />
      <CreateCat @catRefresh="refreshCats" class="mt-4" /> 
      <!-- event listener catRefresh and triggers refreshCats method - updating data property state causing a rerender -->

    </div>
  </template>
  
  <script>
  import ListCat from './components/ListCat.vue';
  import CreateCat from './components/CreateCat.vue';
  
  export default {
    components: {
      ListCat,
      CreateCat,
    },
    data() {
      return {
        state: 1
      };
    },
    methods: {
      refreshCats() {
        this.state += 1
      }
    }
  };
  </script>