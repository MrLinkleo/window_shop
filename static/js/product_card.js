function openModal(productName, productId, productPrice) {
    document.getElementById('productName').value = productName;
    document.getElementById('productId').value = productId;
    document.getElementById('productPrice').value = productPrice;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submitCartForm() {
    const productId = document.getElementById('productId').value;
    const quantity = document.getElementById('productQuantity').value;

    fetch(`/add_to_cart/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            productId: productId,
            quantity: quantity
        })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Ошибка при добавлении в корзину');
    })
    .then(data => {
        alert(data.message);
        document.getElementById('cartForm').reset();
        const cartModal = bootstrap.Modal.getInstance(document.getElementById('cartModal'));
        cartModal.hide();
    })
    .catch(error => console.error('Ошибка:', error));
}