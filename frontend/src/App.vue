<template>
  <div id="app">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
          integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">

    <b-navbar toggleable="lg" type="dark" variant="dark">

      <b-navbar-nav>
        <b-link to="/results" class="mr-sm-2" router-tag="b-nav-item">
          BMS
        </b-link>
      </b-navbar-nav>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <!--<b-form @submit.prevent="setSearchedMovies">-->
          <b-input-group class="mr-sm-2" size="sm">
            <b-form-input v-model="searchBar" placeholder="Movie Title"></b-form-input>
            <b-input-group-append>
              <!--to="/moviedetail" type="submit" @click="setSearchedMovies-->
              <b-button variant="light" to="/moviedetail"><i class="fas fa-search"/></b-button>
            </b-input-group-append>
          </b-input-group>
          <!--</b-form>-->
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <b-link to="/about" class="mr-sm-2" router-tag="b-nav-item">
              About
            </b-link>
          </b-navbar-nav>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template slot="button-content"><i class="fas fa-user"/></template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div id="likedMovieBar">
      <b-container fluid class="p-4 bg-dark" v-if="likedMovies.length">
        <b-row>
          <b-col v-for="movie in likedMovies" :key="movie.imdbID">
            <b-img center thumbnail fluid :src="movie.Poster" :alt="movie.Title" height="202px" width="137px"></b-img>
          </b-col>
        </b-row>
      </b-container>
    </div>

    <router-view/>

    <ul>
      <li v-for="movie in searchedMovies"> {{ movie.title }}</li>
    </ul>
    <hr>
    <ul>
      <li v-for="movieID in likedMovies"> {{ movieID }}</li>
    </ul>
  </div>
</template>

<script>
  import _ from 'lodash'
  import {mapActions, mapState} from 'vuex'

  export default {
    name: 'app',
    data() {
      return {
        searchBar: ''
      }
    },
    computed: {
      ...mapState([
        'searchedMovies',
        'likedMovies'
      ])
    },
    methods: {
      ...mapActions([
        'getSearchedMovie'
      ]),
      setSearchedMovies() {
        const title = this.searchBar
        this.getSearchedMovie(title)
      }
    },
    watch: {
      searchBar: _.debounce(function (newVal) {
        this.setSearchedMovies(newVal)
      }, 500)
    },
    // created: function () {
    //     this.debouncedSetSearchedMovies = _.debounce(this.setSearchedMovies, 500)
    // }
    //this.$store.dispatch('getSelectedMovie')
  }
</script>

<!--<style lang="scss">-->
<!--#app {-->
<!--font-family: 'Avenir', Helvetica, Arial, sans-serif;-->
<!-- -webkit-font-smoothing: antialiased;-->
<!-- -moz-osx-font-smoothing: grayscale;-->
<!--text-align: center;-->
<!--color: #2c3e50;-->
<!--margin-top: 60px;-->
<!--}-->

<!--h1, h2 {-->
<!--font-weight: normal;-->
<!--}-->

<!--ul {-->
<!--list-style-type: none;-->
<!--padding: 0;-->
<!--}-->

<!--li {-->
<!--display: inline-block;-->
<!--margin: 0 10px;-->
<!--}-->

<!--a {-->
<!--color: #42b983;-->
<!--}-->
<!--</style>-->
