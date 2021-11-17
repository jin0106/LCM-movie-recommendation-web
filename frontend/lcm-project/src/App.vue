<template>
  <div id="app">
    <div id="nav">
      <h1 v-if="isLogin">로그인 완료</h1>
      <h2 v-else>로그인 안됨</h2>

      <router-link :to="{ name : 'Signup' }">Signup</router-link>   |
      <router-link :to="{ name : 'Login' }">Login</router-link>   |
      <router-link :to="{ name : 'temp' }">temp</router-link>   


    </div>
    <router-view 
    @login="setLogin"
    />
  </div>
</template>
<script>

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
      setLogin: function () {
      this.isLogin = true
    },
  },
  created: function () {
    if (localStorage.getItem('JWT')) {
      this.isLogin = true
    } else {
      this.$router.push({ name: 'Login' }).catch(() => {})
    }
  }

}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
