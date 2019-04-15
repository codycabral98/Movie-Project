<template>
  <div>
    <b-card no-body v-for="movie in movieInfo" :key="movie.imdbID" class="overflow-hidden rounded-0" bg-variant="light" text-variant="dark" border-variant="dark">
      <b-row no-gutters>
        <b-col md="auto">
          <!--<mdb-icon fab icon="500px"/>-->
          <b-card-img height="410px" class="rounded-0" fluid
                      :src="movie.Poster"></b-card-img>
        </b-col>
        <b-col>
          <b-card-body>
            <b-card-title><i class="fas fa-film"/>
              {{ movie.Title }} {{ movie.Year }}
            </b-card-title>
            <b-card-sub-title>
              {{ movie.Rated }} |
              {{ movie.Genre }} |
              <i class="far fa-clock"/> {{ movie.Runtime }}
            </b-card-sub-title>
            <hr>
            <b-card-text>
              <b-container>
                <b-row>
                  <b-col cols="4"><strong>About</strong></b-col>
                  <b-col>{{ movie.Plot }}</b-col>
                </b-row>
                <br>
                <b-row>
                  <b-col cols="4"><strong>Director</strong></b-col>
                  <b-col>{{ movie.Director }}</b-col>
                </b-row>
                <br>
                <b-row>
                  <b-col cols="4"><strong>Actors</strong></b-col>
                  <b-col>{{ movie.Actors }}</b-col>
                </b-row>
                <br><br><br><br>
                <b-row>
                  <b-col>
                    <b-button bottom variant="success" @click="appendLikedMovie(movie)">Like Movie</b-button>
                  </b-col>
                  <b-col></b-col>
                </b-row>
              </b-container>
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    name: "MovieDetail",
    data() {
      return {
        movieInfo: []
      }
    },
    computed: {
      ...mapState([
        'searchedMovies'
      ])
    },
    methods: {
      ...mapActions([
        'addLikedMovie'
      ]),
      appendLikedMovie(movie) {
        console.log(movie)
        this.addLikedMovie(movie)
      }
    },
    mounted: function () {
      //56adb70a
      //f680c13
      this.searchedMovies.forEach((obj) => {
        fetch(`http://omdbapi.com/?apikey=f680c13&i=${obj.imdb_id}`, {
          method: 'get'
        })
          .then((response) => {
            return response.json()
          })
          .then((jsonData) => {
            this.movieInfo.push(jsonData)
          })
      })
    },
  }
</script>

<style scoped>

</style>
