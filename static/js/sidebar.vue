<template>
    <template id="sidebar-template">
        <a href="/">
            <h2>{{ appName }}</h2>
            <h3></h3>
        </a>

        <a href="#">Products</a>
        <a href="#">Sales</a>
        <a href="#">Users</a>
        <div style="flex: 1;"></div>
        <div class="ecommerce-logout" v-on:click="logout()">Logout</div>
    </template>
</template>

<script>
createApp({
    data() {
        return {
            appName: 'Ecommerce'
        }
    },
    methods: {
        logout() {
            console.log('Logging out...')
        }
    }
}).mount('#sidebar')
</script>
