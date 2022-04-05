<template>
  <navbar-component />
  <div class="cuerpo">
    <div class="album py-5 bg-darkblue">
      <div class="container">
        <div class="row">
          <div v-for="categs in APIDatos" :key="categs.id" class="col-md-4">
            <div class="card mb-4 box-shadow">
              <img
                class="card-img-top"
                src="https://via.placeholder.com/150x100"
                alt="Card image cap"
              />
              <div class="card-body">
                <h4>
                  <a class="text-secondary" @click="$router.push({name: 'Productos', params: {id: categs.id}})"> {{categs.nombre}}</a>
                </h4>
                <p class="card-text">{{categs.descripcion}}</p>
                <div class="d-flex justify-content-between align-items-center">
                  <small class="text-muted">:D</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarComponent from "./NavbarComponent.vue";
import getApi from '@/axios-api'

export default {
  components: { NavbarComponent },
  name: "IndexComponent",

    data() {
        return {
            APIDatos: [],
            nombre: '',
            descripcion: '',
            categoria: '',
        };
    },

    created() {
        getApi.get("index/categorias")
        .then((Response) => {
            console.log("Api recibe dato");
            this.APIDatos = Response.data;
        })
        .catch((err) => {
            console.log(err)
        })
    },

};
</script>

<style>

.cuerpo {
    margin-top: 90px;
}

</style>