import axios from 'axios'

export default {
  fetchMovies (method, params, data) {
    if (method === 'post') {
      return ajax('api/movies/', 'method', null, {data})
    } else {
      return ajax('api/movies/', 'get', {})
    }
  },
  getMovieByTitle (method, params, data) {
    return ajax(`api/movies/?title__icontains=${params}`, 'get', {})
  }
}

/**
 * @param url
 * @param method
 * @param params
 * @param data
 * @returns
 */
function ajax(url, method, options) {
  if (options !== undefined) {
    var {params = {}, data = {}} = options
  } else {
    params = data = {}
  }

  return new Promise((resolve, reject) => {
    axios({
      url,
      method,
      params,
      data
    }).then(res => {
      resolve(res)
    }, res => {
      reject(res)
    })
  })
}
