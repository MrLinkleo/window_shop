function updateQuantity(cartItemId) {
    const quantity = document.getElementById('quantity-' + cartItemId).value;
    console.log('Обновление количества для товара с ID:', cartItemId, 'Количество:', quantity);

    fetch("{% url 'shop_app:update_cart_item' %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: new URLSearchParams({
            'cart_item_id': cartItemId,
            'quantity': quantity
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Обновляем сумму в корзине
            document.getElementById('total-price').innerText = data.total_price + ' руб.';
        } else {
            alert("Ошибка при обновлении количества товара");
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}

// Функция для удаления товара из корзины
function deleteItem(cartItemId) {
    if (confirm('Вы уверены, что хотите удалить этот товар из корзины?')) {
        fetch("{% url 'shop_app:delete_cart_item' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: new URLSearchParams({
                'cart_item_id': cartItemId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Удаляем строку товара из таблицы
                document.getElementById('cart-item-' + cartItemId).remove();
                // Обновляем общую сумму корзины
                document.getElementById('total-price').innerText = data.total_price + ' руб.';
            } else {
                alert("Ошибка при удалении товара");
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert("Произошла ошибка при запросе.");
        });
    }
}