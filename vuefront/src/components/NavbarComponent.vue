<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <a class="navbar-brand">
          <img
            src="https://cdn.icon-icons.com/icons2/1948/PNG/512/free-30-instagram-stories-icons23_122570.png"
            height="50"
            alt=""
            loading="lazy"
          />
          <p>Tienda de mascotas :D</p>
        </a>
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" @click="$router.push({ name: 'Index' })"
              >Inicio</a
            >
          </li>
          <li class="nav-item">
            <a
              class="nav-link"
              @click="$router.push({ name: 'AgregarProducto' })"
              >Añadir producto</a
            >
          </li>
          <li class="nav-item">
            <a
              class="nav-link"
              @click="$router.push({ name: 'CrearCategoria' })"
              >Añadir categoria</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style>
</style>