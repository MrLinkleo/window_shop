document.addEventListener('DOMContentLoaded', function () {
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');
    const logoutBtn = document.getElementById('logoutBtn');
    const loginSubmit = document.getElementById('loginSubmit');
    const registerSubmit = document.getElementById('registerSubmit');
    const cartBtn = document.getElementById('cartBtn');

    // Функция для обработки входа
    if (loginSubmit) {
        loginSubmit.addEventListener('click', async function () {
            const username = document.getElementById('loginUsername').value;
            const password = document.getElementById('loginPassword').value;
            const url = loginBtn.dataset.url; // URL для отправки запроса

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                window.location.href = '/users/profile/';
            } else {
                alert('Ошибка входа');
            }
        });
    }

    // Функция для регистрации
    if (registerSubmit) {
        registerSubmit.addEventListener('click', async function () {
            const username = document.getElementById('registerUsername').value;
            const email = document.getElementById('registerEmail').value;
            const password = document.getElementById('registerPassword1').value;
            const confirmPassword = document.getElementById('registerPassword2').value;

            // Проверка на совпадение паролей
            if (password !== confirmPassword) {
                alert('Пароли не совпадают');
                return;
            }

            const data = {
                username: username,
                email: email,
                password1: password,
                password2: confirmPassword
            };

            try {
                const response = await fetch('/users/register/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    },
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    // Получаем данные из ответа сервера
                    const result = await response.json();

                    // Перенаправляем пользователя в личный кабинет после успешной регистрации
                    window.location.href = '/users/profile/';  // Путь, куда нужно перенаправить
                } else {
                    const errorData = await response.json();
                    alert(`Ошибка регистрации: ${errorData.message || 'Неизвестная ошибка'}`);
                }
            } catch (error) {
                alert('Ошибка соединения с сервером: ' + error.message);
            }
        });
    }

    // Функция для выхода
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async function () {
            const url = logoutBtn.dataset.url;
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });

            if (response.ok) {
                window.location.href = '/users/home/';
            } else {
                alert('Ошибка выхода');
            }
        });
    }
    if (cartBtn) {
        cartBtn.addEventListener('click', function(event) {
            const url = event.target.getAttribute('data-url');
            window.location.href = url; // Перенаправление на корзину
        });
    }
});