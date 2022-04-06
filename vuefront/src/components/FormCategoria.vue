<template>
  <navbar-component />
  <div class="cuerpo">
    <div class="formulario">
      <div class="container">
        <div class="card">
          <div class="card-body">
            <form enctype="multipart/form-data" @submit="agregarCategoria(categoria)">
              <div class="form-group py-2">
                <input
                  class="form-control"
                  type="text"
                  placeholder="Nombre de categoría"
                  v-model="categoria.nombre"
                  required
                />
              </div>
              <div class="form-group py-2">
                <textarea
                  class="form-control"
                  type="text"
                  rows="5"
                  placeholder="Descripción de categoría"
                  v-model="categoria.descripcion"
                  required
                />
              </div>
              <div class="form-group py-2">
                <button class="btn btn-success btn-block" type="submit">
                  Añadir categoría
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
import getApi from '@/axios-api'

export default {
  name: "FormCategoria",

  components: {
    NavbarComponent,
  },

  data() {
    return {
      categoria: {
        nombre: '',
        descripcion: '',
      }
    }
  },

  methods: {
    agregarCategoria() {
      getApi.post("index/agregarcategoria", this.categoria)
      .then((Response) => {
        console.log(Response);
      })
      .catch((err) => {
        console.log(err)
      });
    }
  }

};
</script>

<style>
</style>