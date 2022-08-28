const contentContainer = document.getElementById('content-container');
const loginForm = document.getElementById('login-form');

const baseEndpoint = "http://localhost:8000/api";
if (loginForm) {
    loginForm.addEventListener('submit', handleLogin);
}

function handleLogin(event) {
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/` // JWT token
    let loginFormData = new FormData(loginForm); // grab the form data
    let loginObjectData = Object.fromEntries(loginFormData);
    let bodystr = JSON.stringify(loginObjectData);
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodystr // JSON string
    }
    fetch(loginEndpoint, options) // similar to requests.POST
    .then(res => res.json())
    .then((data) => handleAuthData(data, getProductList))
    .catch(err => console.log(err));
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback) {
        callback();
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body) {
    return {
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`,
        },
        body: body ? body : null
    }
}

function isTokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code == 'token_not_valid') {
        // run a refresh token fetch
        alert('please login again');
        // return false;
    }
    return true;
}

function validateJWTToken() {
    // fetch
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(res => res.json())
    .then(data => {
        // refresh token
        // isTokenNotValid(data);
    })
}

function getProductList() {
    const endpoint = `${baseEndpoint}/event_providers/`
    const options = getFetchOptions();
    fetch(endpoint, options)
    .then(res => {
        // console.log(res);
        return res.json();
    })
    .then(data => {
        const validData = isTokenNotValid(data);
        if (validData) {
            writeToContainer(data);
        }
    })
}

// validateJWTToken();
getProductList();
