let questions;
let currentQuestionIndex;
let score = 0;
let timer;
let timeLeft = 60;

document.getElementById('start-button').addEventListener('click', startGame);
document.getElementById('restart-button').addEventListener('click', restartGame);
document.getElementById('show-answers-button').addEventListener('click', showAnswers);

function startGame() {
    document.getElementById('menu').style.display = 'none';
    document.getElementById('quiz').style.display = 'block';
    score = 0;
    currentQuestionIndex = 0;
    timeLeft = 60;
    startTimer();
    fetchQuestions();
}

function fetchQuestions() {
    fetch('/questions')
        .then(response => response.json())
        .then(data => {
            questions = data;
            setNextQuestion();
        });
}

function startTimer() {
    timer = setInterval(() => {
        timeLeft--;
        document.getElementById('time').innerText = timeLeft;
        if (timeLeft <= 0) {
            clearInterval(timer);
            showScore();
        }
    }, 1000);
}

function setNextQuestion() {
    resetState();
    showQuestion(questions[currentQuestionIndex]);
}

function showQuestion(question) {
    document.getElementById('question').innerText = question[0];
    const answerButtons = document.getElementById('answer-buttons');
    question[1].forEach((answer, index) => {
        const button = document.createElement('button');
        button.innerText = answer;
        button.classList.add('btn');
        button.addEventListener('click', () => selectAnswer(index, question[2]));
        answerButtons.appendChild(button);
    });
}

function resetState() {
    const answerButtons = document.getElementById('answer-buttons');
    while (answerButtons.firstChild) {
        answerButtons.removeChild(answerButtons.firstChild);
    }
}

function selectAnswer(selectedIndex, correctIndex) {
    if (selectedIndex === correctIndex) {
        score++;
    }
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        setNextQuestion();
    } else {
        showScore();
    }
}

function showScore() {
    clearInterval(timer);
    document.getElementById('question-container').style.display = 'none';
    document.getElementById('score-container').style.display = 'block';
    document.getElementById('score').innerText = score + '/' + questions.length;
}

function restartGame() {
    document.getElementById('score-container').style.display = 'none';
    startGame();
}

function showAnswers() {
    const answersContainer = document.getElementById('answers-container');
    answersContainer.style.display = 'block';
    answersContainer.innerHTML = '';

    questions.forEach((question, index) => {
        const div = document.createElement('div');
        div.innerHTML = `<strong>${index + 1}. ${question[0]}</strong> <br> (Correct Answer: ${question[1][question[2]]})`;
        answersContainer.appendChild(div);
    });
}
