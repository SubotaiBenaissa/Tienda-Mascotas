import { createRouter, createWebHashHistory } from 'vue-router'
import IndexComponent from '@/components/IndexComponent'
import ProductoComponent from '@/components/ProductoComponent'
import FormComponent from '@/components/FormComponent'
import FormCategoria from '@/components/FormCategoria'

const routes = [

  {
    path: '/',
    name: 'Index',
    component: IndexComponent
  },
  {
    path: '/productos',
    name: 'Productos',
    component: ProductoComponent
  },
  {
    path: '/crearproducto',
    name: 'AgregarProducto',
    component: FormComponent
  },
  {
    path: '/crearcategoria',
    name: 'CrearCategoria',
    component: FormCategoria
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
