export default (await import('vue')).defineComponent({
    name: "Quiz",
    data() {
        return {
            categories: [],
            title: "Quiz Time!",
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
        async fetchCategories() {
            try {
                const response = await fetch("http://localhost:8000/api/categories/");
                const data = await response.json();
                this.categories = data;
            }
            catch (error) {
                console.error("Erro ao carregar categorias:", error);
            }
        },
        selectCategory(categoryId) {
            console.log('Categoria selecionada:', categoryId);
        },
        async fetchQuestions() {
            try {
                const response = await fetch("http://localhost:8000/api/questions/");
                const data = await response.json();
                this.questions = data;
            }
            catch (error) {
                console.error("Erro ao carregar perguntas:", error);
            }
        },
        selectOption(selectedIndex) {
            if (this.currentQuestion.correctOption === selectedIndex) {
                this.score++;
                alert("Resposta correta!");
            }
            else {
                alert("Resposta incorreta.");
            }
            if (this.currentQuestionIndex < this.questions.length - 1) {
                this.currentQuestionIndex++;
            }
            else {
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
        this.fetchCategories();
        this.fetchQuestions();
    },
});
;
function __VLS_template() {
    const __VLS_ctx = {};
    let __VLS_components;
    let __VLS_directives;
    ['category-button',];
    __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
        ...{ class: ("quiz") },
    });
    __VLS_elementAsFunction(__VLS_intrinsicElements.h2, __VLS_intrinsicElements.h2)({
        ...{ class: ("subtitle") },
    });
    if (__VLS_ctx.categories.length) {
        __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
        for (const [category] of __VLS_getVForSourceType((__VLS_ctx.categories))) {
            __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
                key: ((category.id)),
                ...{ class: ("category-button") },
            });
            __VLS_elementAsFunction(__VLS_intrinsicElements.button, __VLS_intrinsicElements.button)({
                ...{ onClick: (...[$event]) => {
                        if (!((__VLS_ctx.categories.length)))
                            return;
                        __VLS_ctx.selectCategory(category.id);
                    } },
            });
            (category.name);
        }
    }
    else {
        __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
        __VLS_elementAsFunction(__VLS_intrinsicElements.p, __VLS_intrinsicElements.p)({});
    }
    if (__VLS_ctx.questions.length) {
        __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
        __VLS_elementAsFunction(__VLS_intrinsicElements.p, __VLS_intrinsicElements.p)({});
        (__VLS_ctx.currentQuestion.question);
        for (const [option, index] of __VLS_getVForSourceType((__VLS_ctx.currentQuestion.options))) {
            __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
                key: ((index)),
            });
            __VLS_elementAsFunction(__VLS_intrinsicElements.button, __VLS_intrinsicElements.button)({
                ...{ onClick: (...[$event]) => {
                        if (!((__VLS_ctx.questions.length)))
                            return;
                        __VLS_ctx.selectOption(index);
                    } },
            });
            (option);
        }
    }
    else {
        __VLS_elementAsFunction(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
        __VLS_elementAsFunction(__VLS_intrinsicElements.p, __VLS_intrinsicElements.p)({});
    }
    ['quiz', 'subtitle', 'category-button',];
    var __VLS_slots;
    var $slots;
    let __VLS_inheritedAttrs;
    var $attrs;
    const __VLS_refs = {};
    var $refs;
    var $el;
    return {
        attrs: {},
        slots: __VLS_slots,
        refs: $refs,
        rootEl: $el,
    };
}
;
let __VLS_self;
