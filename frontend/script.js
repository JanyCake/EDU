async function askQuestion() {
    const question = document.getElementById('question').value;
    const responseDiv = document.getElementById('answer');
    responseDiv.textContent = 'Загрузка...';

    try {
        const res = await fetch('/api/question', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await res.json();
        if (data.answer) {
            responseDiv.textContent = data.answer;
        } else {
            responseDiv.textContent = 'Ошибка: ' + (data.error || 'Нет ответа.');
        }
    } catch (err) {
        responseDiv.textContent = 'Ошибка подключения к серверу.';
    }
}
