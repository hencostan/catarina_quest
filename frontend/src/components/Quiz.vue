<template>
  <div class="quiz">
    <h1 class="subtitle" :class="{'category-selected': selectedCategory}">
      {{ selectedCategory ? selectedCategoryName : 'Escolha uma categoria:' }}
    </h1>

    <div v-if="!selectedCategory" class="category-list">
      <div v-for="category in categories" :key="category.id" class="category-button">
        <button @click="selectCategory(category)">
          {{ category.name }}
        </button>
      </div>
    </div>
    
    <div v-else-if="questions.length > 0 && currentQuestion.question" class="question-box">
      <p class="question-text">{{ currentQuestion.question }}</p>
      <div class="options">
        <button v-for="(option, index) in shuffledOptions" 
                :key="index" 
                @click="selectOption(option)"
                :class="{'correct': option.isCorrect && selectedAnswer !== null, 'incorrect': !option.isCorrect && selectedAnswer === option}">
          {{ option.text }}
        </button>
      </div>
      <p v-if="selectedAnswer !== null" class="feedback">
        {{ selectedAnswer.isCorrect ? 'Resposta correta!' : 'Resposta incorreta' }}
      </p>
      <button v-if="selectedAnswer !== null && currentQuestionIndex < questions.length - 1" 
        @click="nextQuestion" 
        class="next-button">
        Próxima
      </button>

    </div>
    
    <div v-else>
      <p>Aguarde o carregamento das perguntas, caso demore, tente selecionar outra categoria.</p>
    </div>
    
    <div v-if="quizCompleted" class="result-box">
      <p>Quiz concluído! Sua pontuação: {{ score }} / {{ questions.length }}</p>
      <button @click="resetQuiz" class="back-button">Voltar para o menu</button>
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
      selectedCategoryName: '',  
      shuffledOptions: [],     
      quizCompleted: false,
      selectedAnswer: null, 
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex] || {};
    },
  },
  props: {
    onReset: Function
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await fetch("http://localhost:8000/api/categories/");
        const data = await response.json();
        console.log("Categorias carregadas:", data);
        this.categories = data;
      } catch (error) {
        console.error("Erro ao carregar categorias", error);
      }
    },
    async selectCategory(category) {
      this.selectedCategory = category.id;
      this.selectedCategoryName = category.name;
      console.log("Categoria selecionada:", this.selectedCategory);
      try {
        const response = await fetch(`http://localhost:8000/api/questions/?category=${this.selectedCategory}`);
        const data = await response.json();
        console.log("Perguntas carregadas:", data);
        this.questions = Array.isArray(data) ? [...data] : [];
        if (this.questions.length > 0) {
          this.currentQuestionIndex = 0;
          this.score = 0;
          this.quizCompleted = false;
          this.selectedAnswer = null;
          this.shuffleOptions();
        } else {
          console.log("Não há perguntas para esta categoria.");
        }
      } catch (error) {
        console.error("Erro ao carregar perguntas", error);
      }
    },
    shuffleOptions() {
      if (!this.currentQuestion || !this.currentQuestion.options) return;
      // Cria um array de objetos a partir do array de opções
      const options = this.currentQuestion.options.map((opt, index) => ({
        text: opt,
        isCorrect: index === this.currentQuestion.correct_option
      }));
      // Embaralha as opções
      this.shuffledOptions = options.sort(() => Math.random() - 0.5);
    },
    selectOption(option) {
      if (this.selectedAnswer === null) {
        this.selectedAnswer = option;
          if (option.isCorrect) this.score++; // Se for a última pergunta, finalize o quiz imediatamente
          if (this.currentQuestionIndex === this.questions.length - 1) {
            this.quizCompleted = true;
          }
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
      console.log("Header clicado: resetCategory acionado");
      this.selectedCategory = null;
      this.selectedCategoryName = '';
      this.questions = [];
      this.currentQuestionIndex = 0;
      this.score = 0;
      this.quizCompleted = false;
      this.selectedAnswer = null;
      if (this.onReset) {
        this.onReset();
      }
    },
  },
  mounted() {
    console.log("Chamando fetchCategories");
    this.fetchCategories();
  },
};
</script>

<style scoped>
.quiz {
  font-family: Arial, sans-serif;
  text-align: center;
  background-size: cover;
  color: #ffffff;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 25px;
  background-color: #9BCF4B; 
}

.subtitle {
  font-size: 2.8rem;
  font-weight: bold;
  margin-bottom: 30px;
  color: white;
  text-shadow: 0 0 5px red;
}

.subtitle.category-selected {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 30px;
  color: white;
  text-shadow: 0 0 5px red;
}

.category-list, .options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
}

.category-button button, .back-button {
  padding: 13px 26px;
  border: 3px solid #d32f2f;
  background-color: #d32f2f;
  color: #ffffff;
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.next-button {
  padding: 12px 24px;
  border: 3px solid #d32f2f;
  background-color: #d32f2f;
  color: #ffffff;
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.correct-answer, .incorrect-answer {
  margin-bottom: 10px;
}

.category-button button:hover, .back-button:hover, .next-button:hover {
  background-color: #ffffff;
  color: #d32f2f;
}

.question-box, .result-box {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 30px;
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
  margin-top: 20px;
}

.result-box {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 30px;
  border-radius: 10px;
  margin-top: 30px;
}

.result-box p {
  font-size: 1.6rem; 
  margin-bottom: 20px;  
}
</style>