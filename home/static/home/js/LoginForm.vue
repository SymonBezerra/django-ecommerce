<template>
    <div class="login-container">
        <div class="login-form">
            <h2>Ecommerce</h2>
            <div class="login-item">
                <p>Username</p>
                <input type="text" placeholder="Enter your username" v-model="username" @keydown.enter="submitLogin()">
                <p>Password</p>
                <input type="password" placeholder="Enter your password" v-model="password" @keydown.enter="submitLogin()">
            </div>
            <div class="login-submit" @click="submitLogin()">Login</div>
            <p style="color: red;">{{ errorMsg }}</p>
        </div>
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
            username: "",
            password: "",
            errorMsg: ""
        };
    },
    methods: {
        async submitLogin () {
            if (!this.username || !this.password) {
                this.errorMsg = "Please enter both username and password.";
                return;
            }
            const response = await fetch('/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            });
            const data = await response.json();
            if (!response.ok) {
                this.errorMsg = data.error || 'An error occurred during login.';
            } else {
                window.location.href = '/';
            }
        }
    }
};
</script>
