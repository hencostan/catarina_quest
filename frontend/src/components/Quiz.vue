<template>
  <div class="quiz">
    <!-- Subtítulo "Escolha uma categoria" ou o nome da categoria -->
    <h2 class="subtitle" :class="{'category-selected': selectedCategory}">
      {{ selectedCategory ? selectedCategoryName : 'Escolha uma categoria' }}
    </h2>

    <!-- Exibindo as categorias -->
    <div v-if="!selectedCategory" class="category-list">
      <div v-for="category in categories" :key="category.id" class="category-button">
        <button @click="selectCategory(category)">
          {{ category.name }}
        </button>
      </div>
    </div>
    
    <!-- Exibindo perguntas e respostas -->
    <div v-else-if="questions.length > 0" class="question-box">
      <p class="question-text">{{ currentQuestion.text }}</p>
      <div class="options">
        <button v-for="(option, index) in shuffledOptions" 
                :key="index" 
                @click="selectOption(option)"
                :class="{'correct': option.isCorrect && selectedAnswer !== null, 'incorrect': !option.isCorrect && selectedAnswer === option}">
          {{ option.text }}
        </button>
      </div>
      <p v-if="selectedAnswer !== null" class="feedback">
        {{ selectedAnswer.isCorrect ? 'Resposta correta!' : 'Resposta incorreta.' }}
      </p>
      <button v-if="selectedAnswer !== null" @click="nextQuestion" class="next-button">Próxima</button>
    </div>
    
    <!-- Mensagem ao finalizar o quiz -->
    <div v-if="quizCompleted" class="result-box">
      <p>Quiz concluído! Sua pontuação: {{ score }} / {{ questions.length }}</p>
      <button @click="resetQuiz" class="back-button">Voltar para categorias</button>
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
      selectedCategoryName: '',  // Para armazenar o nome da categoria selecionada
      shuffledOptions: [], // Para armazenar as respostas embaralhadas
      quizCompleted: false,
      selectedAnswer: null, // Para armazenar a resposta escolhida
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
    async selectCategory(category) {
      this.selectedCategory = category.id;
      this.selectedCategoryName = category.name;  // Atualiza o nome da categoria
      try {
        const response = await fetch(`http://localhost:8000/api/questions/?category=${category.id}`);
        const data = await response.json();
        this.questions = data;
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.quizCompleted = false;
        this.selectedAnswer = null;
        this.shuffleOptions();
      } catch (error) {
        console.error("Erro ao carregar perguntas:", error);
      }
    },
    shuffleOptions() {
      if (!this.currentQuestion) return;

      const options = [
        { text: this.currentQuestion.correct_answer, isCorrect: true },
        { text: this.currentQuestion.wrong_answer_1, isCorrect: false },
        { text: this.currentQuestion.wrong_answer_2, isCorrect: false },
        { text: this.currentQuestion.wrong_answer_3, isCorrect: false }
      ];
      
      this.shuffledOptions = options.sort(() => Math.random() - 0.5);
    },
    selectOption(option) {
      if (this.selectedAnswer === null) {
        this.selectedAnswer = option;
        if (option.isCorrect) this.score++;
      }
    },
    nextQuestion() {
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
        this.selectedAnswer = null;
        this.shuffleOptions();
      } else {
        this.quizCompleted = true;
      }
    },
    resetQuiz() {
      this.selectedCategory = null;
      this.selectedCategoryName = '';
      this.questions = [];
      this.currentQuestionIndex = 0;
      this.score = 0;
      this.quizCompleted = false;
      this.selectedAnswer = null;
    },
  },
  mounted() {
    this.fetchCategories();
  },
};
</script>

<style scoped>
.quiz {
  font-family: Arial, sans-serif;
  text-align: center;
  background: url('/img/bandeira.png') no-repeat center center fixed;
  background-size: cover;
  color: #ffffff;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background-color: #A1D99B; /* Fundo verde claro, similar ao da bandeira de SC */
}

.subtitle {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: white;
  text-shadow: 0 0 5px red; /* Contorno vermelho nas letras */
}

.subtitle.category-selected {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: white;
  text-shadow: 0 0 5px red; /* Contorno vermelho nas letras */
}

.category-list, .options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
}

.category-button button, .back-button, .next-button {
  padding: 12px 24px;
  border: 3px solid #d32f2f;
  background-color: #d32f2f;
  color: #ffffff;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.category-button button:hover, .back-button:hover, .next-button:hover {
  background-color: #ffffff;
  color: #d32f2f;
}

.question-box, .result-box {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 20px;
  border-radius: 10px;
}

.question-text {
  font-size: 1.4rem;
  margin-bottom: 20px;
}

.options button {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border-radius: 5px;
  border: 2px solid #d32f2f;
  background-color: #ffffff;
  color: #006847;
  font-size: 1rem;
  cursor: pointer;
}

.options button.correct {
  background-color: #4CAF50;
  color: #ffffff;
}

.options button.incorrect {
  background-color: #d32f2f;
  color: #ffffff;
}

.feedback {
  font-size: 1.2rem;
  font-weight: bold;
  margin-top: 10px;
}
</style>