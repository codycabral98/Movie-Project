<template>
    <div class="home">
      <img src="../assets/logo.png"/>
      <HelloWorld msg="My Message"/>
    </div>
</template>

<script>
    import HelloWorld from "../components/HelloWorld";
    export default {
        name: "Home",
      components: {HelloWorld}
    }
</script>
