import {createRouter,createWebHashHistory} from "vue-router";
import {appRoutes} from "@/router/routes";

const router = createRouter({
  history: createWebHashHistory('./'),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    ...appRoutes,
  ],
  scrollBehavior() {
    return {
      top: 0
    }
  }
})

export default router
