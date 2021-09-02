import {getToken, demo} from "./functions.js";

let token;
let usernameFieldElement = document.getElementById("username-field");
let passwordFieldElement = document.getElementById("password-field");
let formElement = document.getElementById("form");

formElement.addEventListener("submit", async (event) => {
    event.preventDefault();
    token = await getToken(usernameFieldElement.value, passwordFieldElement.value);
    await demo(token)
});