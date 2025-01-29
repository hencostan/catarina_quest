import { createRouter, createWebHistory } from 'vue-router';
import Quiz from '../components/Quiz.vue';

const routes = [
  {
    path: '/quiz/:categoryId',
    name: 'Quiz',
    component: Quiz,
    props: true  // Permite passar o ID da categoria para o componente
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;