<template>
  <div class="cuerpo">
    <navbar-component />
    <div class="album py-5 bg-darkblue">
      <div class="container">
        <div class="row">
          <div v-for="prods in APIData" :key="prods.id" class="col-md-4">
            <div class="card mb-4 box-shadow">
              <img
                class="card-img-top"
                src="https://previews.123rf.com/images/alfadanz/alfadanz1803/alfadanz180300075/97044689-conjunto-de-iconos-de-tienda-de-mascotas-con-accesorios-para-gatos-boho-ilustración-vectorial.jpg"
                width="100"
                height="200"
                alt="Card image cap"
              />
              <div class="card-body">
                <h4>
                  <a class="text-secondary"> {{ prods.nombre }}</a>
                </h4>
                <p class="card-text">{{ prods.descripcion }}</p>
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
import getApi from "@/axios-api";

export default {
  name: "ProductoComponent",

  components: {
    NavbarComponent,
  },

  data() {
    return {
      APIData: [],
      idProducto: this.$route.params.id,
      nombre: "",
      descripcion: "",
    };
  },

  created() {
    getApi
      .get("index/filtrar/" + this.idProducto)
      .then((Response) => {
        console.log("Api prods recibe datos");
        this.APIData = Response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },

  methods: {
    borrarProducto() {},
  },
};
</script>

<style>
</style>