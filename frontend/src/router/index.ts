import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import NotFound from "../components/NotFound.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: HomeView },
    { path: "/about", component: AboutView },
    { path: "/:pathMatch(.*)", component: NotFound },
  ],
  // routes: [
  //   //{ path: "/home", component: "Home", meta: { requiresAuth: true } },
  //   //,
  //   // {
  //   //   path: "/about",
  //   //   name: "about",
  //   //   // route level code-splitting
  //   //   // this generates a separate chunk (About.[hash].js) for this route
  //   //   // which is lazy-loaded when the route is visited.
  //   //   component: () => import("../views/AboutView.vue"),
  //   // },
  // ],
});

// router.beforeEach((to, from) => {});

export default router;
