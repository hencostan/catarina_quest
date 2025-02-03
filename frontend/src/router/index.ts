import { createRouter, createWebHistory } from 'vue-router';
import Quiz from '../components/Quiz.vue';

const routes = [
  {
    path: '/quiz/:categoryId',
    name: 'Quiz',
    component: Quiz,
    props: true  
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;