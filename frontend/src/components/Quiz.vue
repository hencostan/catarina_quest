<template>
    <div class="quiz">
      <h1>{{ Catarina Quest }}</h1>
      <div v-if="questions.length">
        <p>{{ currentQuestion.question }}</p>
        <div v-for="(option, index) in currentQuestion.options" :key="index">
          <button @click="selectOption(index)">{{ option }}</button>
        </div>
      </div>
      <div v-else>
        <p>Carregando perguntas...</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Quiz',
    data() {
      return {
        title: 'Quiz Time!',
        questions: [],
        currentQuestionIndex: 0,
        score: 0,
      };
    },
    computed: {
      currentQuestion() {
        return this.questions[this.currentQuestionIndex] || {};
      },
    },
    methods: {
      async fetchQuestions() {
        try {
          const response = await fetch('http://localhost:8000/api/questions/');
          const data = await response.json();
          this.questions = data;
        } catch (error) {
          console.error('Erro ao carregar perguntas:', error);
        }
      },
      selectOption(selectedIndex) {
        if (this.currentQuestion.correctOption === selectedIndex) {
          this.score++;
          alert('Resposta correta!');
        } else {
          alert('Resposta incorreta.');
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
      },
    },
    mounted() {
      this.fetchQuestions();
    },
  };
  </script>
  
  <style scoped>
  .quiz {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 20px auto;
    max-width: 600px;
  }
  
  button {
    margin: 5px;
    padding: 10px 20px;
    border: none;
    background-color: #3498db;
    color: white;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  button:hover {
    background-color: #2980b9;
  }
  </style>  