<template>
  <div class="quiz">
    <!-- Subtítulo "Escolha uma categoria" -->
    <h2 class="subtitle">Escolha uma categoria:</h2>

    <!-- Exibindo as categorias -->
    <div v-if="!selectedCategory" class="category-list">
      <div v-for="category in categories" :key="category.id" class="category-button">
        <button @click="selectCategory(category.id)">
          {{ category.name }}
        </button>
      </div>
    </div>
    
    <div v-else-if="questions.length" class="question-box">
      <p class="question-text">{{ currentQuestion.text }}</p>
      <div class="options">
        <button v-for="(option, index) in shuffledOptions" 
                :key="index" 
                @click="selectOption(option)">
          {{ option }}
        </button>
      </div>
    </div>
    
    <div v-else-if="selectedCategory">
      <p>Carregando perguntas...</p>
    </div>

    <!-- Botão para reiniciar -->
    <div v-if="quizCompleted">
      <p>Quiz concluído! Sua pontuação: {{ score }} / {{ questions.length }}</p>
      <button @click="resetQuiz">Voltar para categorias</button>
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
      selectedCategory: null,
      shuffledOptions: [], // Para armazenar as respostas embaralhadas
      quizCompleted: false,
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
        const data = await response.json();
        this.categories = data;
      } catch (error) {
        console.error("Erro ao carregar categorias:", error);
      }
    },
    async selectCategory(categoryId) {
      this.selectedCategory = categoryId;
      try {
        const response = await fetch(`http://localhost:8000/api/questions/?category=${categoryId}`);
        const data = await response.json();
        this.questions = data;
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.quizCompleted = false;
        this.shuffleOptions();
      } catch (error) {
        console.error("Erro ao carregar perguntas:", error);
      }
    },
    shuffleOptions() {
      if (!this.currentQuestion) return;

      const options = [
        this.currentQuestion.correct_answer,
        this.currentQuestion.wrong_answer_1,
        this.currentQuestion.wrong_answer_2,
        this.currentQuestion.wrong_answer_3
      ];

      this.shuffledOptions = options.sort(() => Math.random() - 0.5);
    },
    selectOption(selectedOption) {
      if (selectedOption === this.currentQuestion.correct_answer) {
        this.score++;
        alert("Resposta correta!");
      } else {
        alert("Resposta incorreta.");
      }

      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
        this.shuffleOptions();
      } else {
        alert(`Quiz concluído! Sua pontuação foi: ${this.score}`);
        this.quizCompleted = true;
      }
    },
    resetQuiz() {
      this.selectedCategory = null;
      this.questions = [];
      this.currentQuestionIndex = 0;
      this.score = 0;
      this.quizCompleted = false;
    },
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

</style>