<template>
    <div class="my-4">
      <h2 class="mb-3">List of Cats</h2>
      <ul class="list-group">
        <li v-for="cat in cats" :key="cat.id" class="list-group-item">
          <div class="card-body d-flex justify-content-between align-items-center">
            <div>
              <img :src="cat.image_url" alt="Cat" class="cat-image">
              ID: <strong>{{ cat.id }}</strong>
              Name: <strong>{{ cat.name }}</strong>
              Age: <strong>{{ cat.age }}</strong>
              Breed: <strong>{{ cat.breed }}</strong>
              Status: <strong>{{ cat.is_adopted ? 'Adopted' : 'Available for Adoption' }}</strong>
            </div>
            <div>
              <UpdateCat @catRefresh="fetchCats" :catData="cat" class="mt-4" />
              <button @click="deleteCat(cat)" class="btn btn-danger m-2">Delete</button>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
<script>
import UpdateCat from './UpdateCat.vue'; 

export default {
  data() {
    return {
      cats: [], 
    };
  },
  created() {
    this.fetchCats(); 
  },
  components: {
    UpdateCat, 
  },
  methods: {
    fetchCats() { 
      fetch("http://localhost:8000/api/cats/") 
        .then(response => response.json())
        .then(data => {
          this.cats = data; 
        })
        .catch(error => {
          console.error("Error:", error);
        });
    },
    deleteCat(cat) { 
      console.log(cat)
      fetch(`http://localhost:8000/api/update_cat/${cat.id}/`, { 
        method: "DELETE"
      })
        .then(response => {
          this.$emit("catRefresh", cat.id); 
        })
        .catch(error => {
          console.error("Error:", error);
        });
    }
  }
};
</script>

<style>
.cat-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
}
</style>