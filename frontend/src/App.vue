<template>
  <div>
    <!-- Cabeçalho que volta para a escolha de categorias -->
    <header class="site-header" @click.prevent="resetQuiz">
      <img src="@/assets/header-sc.png" alt="Cabeçalho" class="header-image" />
    </header>


    <!-- Área principal -->
    <main class="app-main">
      <Quiz />
    </main>

    <!-- Rodapé -->
    <footer class="app-footer">
      <p>Desenvolvido por Ana Laura, Henrique, Fábio e Sara</p>
    </footer>
  </div>
</template>

<script>
import Quiz from './components/Quiz.vue';

export default {
  components: {
    Quiz
  },
  methods: {
    resetCategory() {
      this.$emit("resetCategory"); // Dispara um evento global
    }
  }
};
</script>

<style scoped>
/* Atualizando o estilo da página para ocupar toda a altura e largura */
#app {
  flex-grow: 1; /* Faz a área principal expandir para ocupar o espaço disponível */
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0rem;
  overflow: hidden;
  background: linear-gradient(150deg, #d52b1e, #d52b1e); /* Adicionar o fundo vermelho */
  color: #d52b1e;
  position: relative;
  --vueuse-safe-area-top: 0px;
  --vueuse-safe-area-right: 0px;
  --vueuse-safe-area-bottom: 0px;
  --vueuse-safe-area-left: 0px;
}

:root {
  --vueuse-safe-area-top: 0px;
  --vueuse-safe-area-right: 0px;
  --vueuse-safe-area-bottom: 0px;
  --vueuse-safe-area-left: 0px;
}

.app-main {
  flex-grow: 1; /* Faz a área principal expandir para ocupar o espaço disponível */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #9BCF4B, #9BCF4B);
  padding: 5px;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
}

.component-name {
  --vueuse-safe-area-top: 0px;
  --vueuse-safe-area-right: 0px;
  --vueuse-safe-area-bottom: 0px;
  --vueuse-safe-area-left: 0px;
}

.app-main::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('@/assets/bandeira-sc.svg') no-repeat center center;
  background-size: cover;
  opacity: 0.2;
  z-index: -1; /* Coloca a imagem de fundo atrás do conteúdo */
}

.app-header {
  background: linear-gradient(90deg, #6bae4f, #d52b1e);
  color: white;
  padding: 20px;
  text-align: center;
  font-size: 2.5rem;
  font-weight: bold;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 0 0 20px 20px;
  z-index: 2;
}

.app-footer {
  background-color: #f7f7f7;
  color: #555;
  text-align: center;
  padding: 15px;
  z-index: 2;
}

.subtitle {
  font-family: 'Lobster', cursive;
  font-size: 2rem;
  color: #4a4a4a; /* Ajustando a cor para combinar com o novo estilo */
  text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

.site-header {
  width: 100%;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  cursor: pointer; /* Deixa claro que o cabeçalho é clicável */
}

.header-image {
  width: 100%;
  max-height: 1500px; /* Ajuste conforme necessário */
  object-fit: contain; /* Mantém a proporção da imagem */
}

</style>