<template>
  <navbar-component />
  <div class="cuerpo">
    <div class="formulario">
      <div class="container">
        <div class="card">
          <div class="card-body">
            <form
              enctype="multipart/form-data"
              v-on:submit.prevent="agregarProducto(producto)"
            >
              <div class="form-group py-2">
                <input
                  class="form-control"
                  type="text"
                  placeholder="Nombre del producto"
                  v-model="producto.nombre"
                  required
                />
              </div>
              <div class="form-group py-2">
                <textarea
                  class="form-control"
                  type="text"
                  rows="5"
                  placeholder="Descripción de producto"
                  v-model="producto.descripcion"
                  required
                />
              </div>
              <div class="form-group py-2">
                <div class="form-group">
                  <label for="name">Categoria</label>
                  <select v-model="producto.categoria" class="form-group">
                    <option :value="item.id" v-for="item of producto.categoria" :key="item.id">
                      {{ item.nombre }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="form-group py-2">
                <button class="btn btn-success btn-block" type="submit">
                  Añadir producto
                </button>
              </div>
            </form>
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
  name: "FormComponent",

  components: {
    NavbarComponent,
  },

  data() {
    return {
      producto: {
        nombre: "",
        descripcion: "",
        categoria: [],
      },
    };
  },

  created() {
      getApi
      .get("index/categorias")
      .then((Response) => {
        console.log("Api prods recibe datos");
        this.nombre = Response.data;
        this.producto.categoria = Response.data
      })
      .catch((err) => {
        console.log(err);
      });
      
  },

  methods: {
    agregarProducto() {
      getApi
        .post("index/agregar", this.producto)
        .then((Response) => {
          console.log(Response);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>