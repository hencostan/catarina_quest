<template>
  <div id="app">
    <!-- Cabeçalho -->
    <header class="app-header">
      <h1>Catarina Quest</h1>
      <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
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
import Quiz from "@/components/Quiz.vue";

export default {
  name: "App",
  components: {
    Quiz,
  },
};
</script>

<style scoped>
/* Atualizando o estilo da página para ocupar toda a altura e largura */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
  background: linear-gradient(135deg, #ff0000, #b22222); /* Adicionar o fundo vermelho */
  color: #333333;
  position: relative;
}

.app-main {
  flex: 1; /* Faz a área principal expandir para ocupar o espaço disponível */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #ffffff, #e6e6e6);
  padding: 20px;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
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
  z-index: 0;
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

/* Responsividade */
@media (max-width: 768px) {
  .app-main {
    padding: 10px;
  }
}

@media (max-width: 480px) {
  .app-header {
    font-size: 1.8rem;
  }

  .app-footer {
    font-size: 0.8rem;
  }
}
</style>