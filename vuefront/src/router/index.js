import { createRouter, createWebHashHistory } from 'vue-router'
import IndexComponent from '@/components/IndexComponent'
import ProductoComponent from '@/components/ProductoComponent'
import FormComponent from '@/components/FormComponent'

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
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
