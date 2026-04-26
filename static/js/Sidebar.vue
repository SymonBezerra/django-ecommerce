<template>
    <a href="/">
        <h2>{{ appName }}</h2>
        <h3></h3>
    </a>

    <a href="/products/">Products</a>
    <a href="#">Sales</a>
    <a href="#">Users</a>
    <div style="flex: 1;"></div>
    <div class="ecommerce-logout" v-on:click="logout()">Logout</div>
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
            appName: 'Ecommerce'
        }
    },
    methods: {
        async logout() {
            const response = await fetch('/logout/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            if (response.ok) {
                window.location.href = '/login/';
            } else {
                console.error('Logout failed');
            }
        }
    }
}
</script>
