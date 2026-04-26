<template>
    <h1>Create Product</h1>

    <div class="products-create-form">
        <div class="products-create-form-item">
            <h2>Name</h2>
            <input type="text" id="name" v-model="name">
        </div>

        <div class="products-create-form-item">
            <h2>Description</h2>
            <textarea id="description" v-model="description"></textarea>
        </div>

        <div class="products-create-form-item">
            <h2>Price</h2>
            <input v-money="moneyConfig" v-model="price">
        </div>

        <div class="products-create-form-item">
            <h2>Type</h2>
            <input type="text" v-model="type">
        </div>

        <div class="products-create-form-item">
            <h2>Expiration Date</h2>
            <input type="text" v-mask="'##/##/####'" v-model="expirationDate">
        </div>


        <div class="products-submit-btn" @click="submitProduct()">Submit</div>
    </div>
</template>

<script>
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie) {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    export default {
        data() {
            return {
            description: '',
            expirationDate: '',
            name: '',
            type: '',
            price: null,
            moneyConfig: {
                decimal: ',',
                thousands: '.',
                prefix: 'R$ ',
                precision: 2,
                masked: false
                }
            }
        },
        methods: {
            toISODate(dateStr) {
                const [day, month, year] = dateStr.split('/');
                return `${year}-${month}-${day}`;
            },
            async submitProduct() {
                const response = await fetch('/products/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({
                        name: this.name,
                        description: this.description,
                        type: this.type,
                        price: this.price,
                        expiration_date: this.toISODate(this.expirationDate)
                    })
                });

                if (response.ok) {
                    window.location.href = '/products/';
                } else {
                    const errorData = await response.json();
                    alert(`Error creating product: ${errorData.error}`);
                }
            }
        }
    }
</script>