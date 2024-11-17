// function handleRegister(event) {
//     event.preventDefault();  // Останавливаем стандартное поведение кнопки

//     var username = document.getElementById('registerUsername').value;
//     var email = document.getElementById('registerEmail').value;
//     var password1 = document.getElementById('registerPassword1').value;
//     var password2 = document.getElementById('registerPassword2').value;

//     if (username === "" || email === "" || password1 === "" || password2 === "") {
//         alert("Пожалуйста, заполните все поля.");
//         return;
//     }

//     if (password1 !== password2) {
//         alert("Пароли не совпадают.");
//         return;
//     }

//     // Отправка данных через AJAX
//     $.ajax({
//         type: 'POST',
//         url: '{% url "users:register" %}',  // URL для обработки регистрации на сервере
//         data: {
//             'username': username,
//             'email': email,
//             'password1': password1,
//             'password2': password2,
//             'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),  // csrf токен
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 // Закрыть модальное окно регистрации
//                 $('#registerModal').modal('hide');
//                 alert('Регистрация прошла успешно!');
//                 // Здесь можешь делать дополнительные действия, например, перенаправление на страницу профиля.
//             } else {
//                 alert('Произошла ошибка при регистрации: ' + response.message);
//             }
//         },
//         error: function(xhr, status, error) {
//             alert("Произошла ошибка при отправке данных.");
//         }
//     });
// }

// function handleLogin(event) {
//     event.preventDefault();  // Останавливаем стандартное поведение кнопки

//     var username = document.getElementById('loginUsername').value;
//     var password = document.getElementById('loginPassword').value;

//     if (username === "" || password === "") {
//         alert("Пожалуйста, заполните все поля.");
//         return;
//     }

//     // Отправка данных через AJAX
//     $.ajax({
//         type: 'POST',
//         url: '{% url "users:login" %}',  // URL для обработки логина на сервере
//         data: {
//             'username': username,
//             'password': password,
//             'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),  // csrf токен
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 // Закрыть модальное окно входа
//                 $('#loginModal').modal('hide');
//                 alert('Вы успешно вошли!');
//                 // Можно сделать редирект на главную страницу или страницу профиля
//             } else {
//                 alert('Неверные данные для входа!');
//             }
//         },
//         error: function(xhr, status, error) {
//             alert("Произошла ошибка при отправке данных.");
//         }
//     });
// }

