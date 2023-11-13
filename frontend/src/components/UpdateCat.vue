<template>
  <button type="button" class="btn btn-primary" :data-bs-target="'#updateCatModal' + catData.id" data-bs-toggle="modal">
    View Cat
  </button>

  <div class="modal fade" :id="'updateCatModal' + catData.id" tabindex="-1" aria-labelledby="updateCatLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="updateCatLabel">Edit Cat</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="text-center">
            <img :src="catData.image_url" alt="Random Cat" class="img-fluid rounded">
          </div>
          <form @submit.prevent="updateCat" class="my-4">
            <div class="form-group">
              <label for="name">Name:</label>
              <input type="text" id="name" v-model="catData.name" required class="form-control">
            </div>

            <div class="form-group">
              <label for="age">Age:</label>
              <input type="number" id="age" v-model="catData.age" required class="form-control">
            </div>

            <div class="form-group">
              <label for="breed">Breed:</label>
              <input type="text" id="breed" v-model="catData.breed" required class="form-control">
            </div>

            <label for="isAdopted">Adoption Status:</label>
            <div class="form-group">
              <input type="radio" id="adopted" v-model="catData.is_adopted" name="adoptionStatus" value=true>
              <label for="adopted" class="p-1">Adopted</label><br>
              <input type="radio" id="notAdopted" v-model="catData.is_adopted" name="adoptionStatus" value=false>
              <label for="notAdopted" class="p-1">Available for Adoption</label>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" @click="updateCat" class="btn btn-primary">Update Cat</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    catData: {
      type: Object,
      default: () => ({
        id: 0,
        name: "",
        age: null,
        breed: "",
        is_adopted: false,
      }),
      required: false,
    },
  },
  methods: {
    updateCat() {
      fetch(`http://localhost:8000/api/update_cat/${this.catData.id}/`, {
        method: "PUT",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.catData)
      })
        .then(response => response.json())
        .then(data => {
          this.$emit('catRefresh')
        })
        .catch(error => {
          console.error("Error:", error);
        });
    }
  }
};
</script>
