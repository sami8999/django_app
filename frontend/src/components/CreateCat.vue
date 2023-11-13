<template>
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createCatModal">
    Add Cat
  </button>

  <div class="modal fade" id="createCatModal" tabindex="-1" aria-labelledby="createCatModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="createCatModalLabel">Add New Cat</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addCat" class="my-4">
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
              <label for="notAdopted" class="p-1">Not Adopted</label>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-primary" @click="addCat">Add Cat</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
data() {
    return {
    catData: {
        name: "",
        age: null,
        breed: "",
        is_adopted: false,
    }
    };
},
methods: {
    addCat() {
    fetch("http://localhost:8000/api/cats/", {
        method: "POST",
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.catData)
    })
        .then(response => response.json())
        .then(data => {
        this.$emit('catRefresh');
        this.catData = { name: "", age: null, breed: "", is_adopted: true};
        })
        .catch(error => {
        console.error("Error:", error);
        });
    }
}
};
</script>
