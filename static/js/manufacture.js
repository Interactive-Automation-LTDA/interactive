function listManufacturers(url) {
    url = 'http://127.0.0.1:8000/api/v1/cpq/manufactuter/'
    fetch(url)
    .then(response => {
      return response.json()
    })
    .then(responseData => {
      responseData.forEach(manufactures => {
        const listManufactures = `<li>${manufactures.name}</li> <li>${manufactures.cnpj}</li>`
        document.querySelector('ul').insertAdjacentHTML('beforeend', listManufactures)
      })
    })
  }