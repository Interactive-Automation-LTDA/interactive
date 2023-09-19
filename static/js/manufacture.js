function listManufacturers(url) {
    url = 'http://127.0.0.1:8000/api/v1/cpq/manufacturer/'
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



function insertManufacture(){
  const formEl = document.querySelector(".user-data")
  formEl.addEventListener('submit', event =>{
    event.preventDefault()

    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData)

    fetch('http://127.0.0.1:8000/api/v1/cpq/manufacturer/', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
})
}

