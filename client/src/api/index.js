import axios from 'axios'

export function authenticate(userDate) {
  return axios.post('/api/login', userDate)
}
