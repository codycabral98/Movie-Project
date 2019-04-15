import Vue from 'vue'
import Vuex from 'vuex'
import api from "./api";


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchedMovies: [],
    likedMovies: []
  },
  mutations: {
    SET_SEARCHED_MOVIES: (state, movies) => state.searchedMovies = movies,
    ADD_LIKED_MOVIE: (state, movie) => state.likedMovies.push(movie)
  },
  actions: {
    getSearchedMovie: ({ commit }, title) => {
      api.getMovieByTitle('get', title, null).then(res => {
        commit('SET_SEARCHED_MOVIES', res.data)
      }).catch((e) => {
        this.console.log(e)
      })
    },
    addLikedMovie: ({commit}, movie) => {
      commit('ADD_LIKED_MOVIE', movie)
    }
  },
})
