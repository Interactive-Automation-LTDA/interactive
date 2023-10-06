// grab insert action to shopping cart
const updateBtns = document.getElementsByClassName('update-cart')

for (let index = 0; index < updateBtns.length; index++) {
    updateBtns[index].addEventListener('click', function () {
        const productID = this.dataset.product
        const action = this.dataset.action
        console.log('product:', productID, 'action:', action)
        console.log('User:', user)

        if (user === 'AnonymousUser') {
            console.log('Not Logged in')
        }else{
            updateUserOrder(productID, action)
        }
    })
}

function updateUserOrder(productID,action){
    const url = '/cpq/material_update/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('Data:', data)
    })
}