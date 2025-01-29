<template>
  <div class="quiz">
    <!-- Subtítulo "Escolha uma categoria" com contorno degradê -->
    <h2 class="subtitle">Escolha uma categoria:</h2>

    <!-- Exibindo as categorias -->
    <div v-if="categories.length" class="category-list">
      <div v-for="category in categories" :key="category.id" class="category-button">
        <button 
          @click="selectCategory(category.id)"
          @mouseover="hoveredCategory = category" 
          @mouseout="hoveredCategory = null"
        >
          {{ category.name }}
        </button>
        <!-- Exibindo a descrição da categoria ao passar o mouse -->
        <div v-if="hoveredCategory && hoveredCategory.id === category.id" class="description-box">
          <p>{{ hoveredCategory.description }}</p>
        </div>
      </div>
    </div>
    <div v-else>
      <p class="loading-text">Carregando categorias...</p>
    </div>

    <!-- Exibindo a descrição da categoria -->
    <div v-if="hoveredCategory" class="description-box">
      <p>{{ hoveredCategory.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Quiz",
  data() {
    return {
      categories: [],
      questions: [],
      currentQuestionIndex: 0,
      score: 0,
      selectedCategory: null, // Armazena a categoria escolhida
      hoveredCategory: null   // Armazena a categoria que está sendo hover
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex] || {};
    },
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await fetch("http://localhost:8000/api/categories/");
        if (!response.ok) {
        throw new Error('Network response was not okay');
        }
        const data = await response.json();
        console.log("Categorias carregadas:", data);
        this.categories = Array.isArray(data) ? data.map(category => ({
        ...category,
        description: category.description || "Descrição não disponível" // Descrição padrão
        })) : [];
      } catch (error) {
          console.error("Erro ao carregar categorias:", error);
        }
    }
  },
    async selectCategory(categoryId) {
      console.log("Categoria selecionada:", categoryId);
      this.selectedCategory = categoryId;
      try {
        const response = await fetch(`http://localhost:8000/api/questions/?category=${categoryId}`);
        const data = await response.json();
        console.log("Perguntas carregadas:", data);
        this.questions = data;
        this.currentQuestionIndex = 0;
        this.score = 0;
      } catch (error) {
        console.error("Erro ao carregar perguntas:", error);
      }
    },
    selectOption(selectedIndex) {
      if (this.currentQuestion.correctOption === selectedIndex) {
        this.score++;
        alert("Resposta correta!");
      } else {
        alert("Resposta incorreta.");
      }

      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
      } else {
        alert(`Quiz concluído! Sua pontuação foi: ${this.score}`);
        this.resetQuiz();
      }
    },
    resetQuiz() {
      this.currentQuestionIndex = 0;
      this.score = 0;
      this.questions = [];
      this.selectedCategory = null;
    },
    mounted() {
    this.fetchCategories();
    },
};
</script>

<style scoped>
/* Estilo para o componente quiz */
.quiz {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 0;
  padding: 20px;
  background-color: transparent; /* Remover a cor de fundo */
  color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 100%;
  min-height: 100vh; /* Ajuste a altura */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

h2.subtitle {
  font-size: 1.8rem;
  opacity: 100; /* Aumentar a opacidade conforme necessário */
  margin-bottom: 20px;
  padding: 10px 15px;
  background: linear-gradient(90deg, #6bae4f, #d52b1e);
  -webkit-background-clip: text;
  color: transparent;
  font-weight: bold;
}

/* Estilo para a lista de categorias */
.category-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
}

/* Estilo para os botões de categoria */
.category-button button {
  margin: 10px;
  padding: 12px 24px;
  border: 3px solid #d32f2f;
  background-color: rgba(255, 255, 255, 0.2);
  color: #006847; /* Texto verde */
  font-size: 1rem;
  font-weight: bold; /* Deixa o texto mais grosso (negrito) */
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.category-button button:hover {
  background-color: #d32f2f;
  color: #ffffff;
}

/* Estilo para o box de perguntas */
.question-box {
  margin-top: 30px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
}

/* Estilo para o texto das perguntas */
.question-text {
  font-size: 1.4rem;
  margin-bottom: 20px;
}

/* Estilo para as opções de respostas */
.options button {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border-radius: 5px;
  border: 2px solid #d32f2f;
  background-color: #ffffff;
  color: #006847;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease, color 0.3s ease;
}

.options button:hover {
  background-color: #d32f2f;
  color: #ffffff;
}

/* Estilo para o container do botão "Voltar" */
.back-button-container {
  margin-top: 20px;
  text-align: center;
  position: absolute;
  bottom: 20px;
  width: 100%;
}

/* Estilo para o botão "Voltar" */
.back-button {
  margin: 10px;
  padding: 12px 24px;
  border: 3px solid #006847; /* Borda verde */
  background-color: #d32f2f; /* Fundo vermelho */
  color: #ffffff; /* Texto branco */
  font-size: 1rem;
  font-weight: bold; /* Deixa o texto mais grosso (negrito) */
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.back-button:hover {
  background-color: rgba(255, 255, 255, 0.2); /* Fundo transparente */
  color: #006847; /* Texto verde */
}

/* Estilo para o texto "Carregando perguntas" */
.loading-text {
  font-size: 1.2rem;
  color: #4a4a4a; /* Tom mais escuro */
}

.description-box {
  margin-top: 10px;
  padding: 10px 15px;
  background-color: rgba(255, 255, 255, 0.7);
  color: #333;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  max-width: 300px;
  text-align: center;
  position: absolute;
  bottom: 60px; /* Ajustar conforme necessário */
  z-index: 10; /* Para garantir que fique acima de outros elementos */
}

/* Animação para os pontos */
@keyframes loading-dots {
  0% {
    content: '';
  }
  25% {
    content: '.';
  }
  50% {
    content: '..';
  }
  75% {
    content: '...';
  }
}

.loading-dots::after {
  content: '...';
  animation: loading-dots 1.5s steps(3, end) infinite;
}
</style>