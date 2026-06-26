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

document.querySelectorAll('.add-cart-btn').forEach(button => {
    button.addEventListener('click', function() {
        const productId = this.dataset.id;
        
        fetch('/cart/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ 'product_id': productId })
        })
        .then(response => response.json())
        .then(data => {
            alert('Product added asynchronously! Total items in cart: ' + data.total_items);
        })
        .catch(err => console.error("Error updating cart:", err));
    });
});

const searchBar = document.getElementById('search-bar');
const gridContainer = document.getElementById('product-grid-container');

if (searchBar) {
    searchBar.addEventListener('input', function(e) {
        const query = e.target.value;

        // Fetch the filtered HTML from Django asynchronously
        fetch(`/?q=${encodeURIComponent(query)}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Tells Django this is an AJAX request
            }
        })
        .then(response => response.json())
        .then(data => {
            // Swap out the old product list layout with the new filtered one
            gridContainer.innerHTML = data.html;
            
            // Re-attach "Add to Cart" click events to the newly generated buttons
            rebindAddToCartButtons();
        })
        .catch(err => console.error("Error during live search execution:", err));
    });
}

// Helper function to make sure newly searched buttons still work when clicked
function rebindAddToCartButtons() {
    document.querySelectorAll('.add-cart-btn').forEach(button => {
        // Remove old listeners to avoid multiple alerts
        button.replaceWith(button.cloneNode(true));
    });
    
    // Bind the click event again
    document.querySelectorAll('.add-cart-btn').forEach(button => {
        button.addEventListener('click', function() {
            fetch('/cart/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ 'product_id': this.dataset.id })
            })
            .then(res => res.json())
            .then(data => alert('Product added asynchronously! Total items in cart: ' + data.total_items));
        });
    });
}

// Cart view dynamic adjustment actions
document.querySelectorAll('.qty-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const productId = this.dataset.id;
        const action = this.dataset.action;
        
        fetch('/cart/update/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ 'product_id': productId, 'action': action })
        })
        .then(res => res.json())
        .then(data => {
            if (data.item_removed) {
                document.getElementById(`cart-row-${productId}`).remove();
            } else {
                document.getElementById(`qty-val-${productId}`).innerText = data.item_qty;
                document.getElementById(`total-val-${productId}`).innerText = data.item_total.toFixed(2);
            }
            
            document.getElementById('cart-grand-total').innerText = data.grand_total.toFixed(2);
            
            if (data.cart_empty) {
                const box = document.getElementById('cart-main-box');
                box.innerHTML = '<p>Your cart is empty.</p><hr><h3>Grand Total: $0.00</h3>';
            }
        });
    });
});
