const baseURL = "http://djangorest.eliaseriksson.eu"

export const getToken = async (username, password) => {
    let response = await fetch(
        `${baseURL}/token/`, {
            cors: "no-cors",
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"username": username, "password": password})
        }
    );
    let data = await response.json();
    return data["token"];
}

export const requestEndpoint = async (endpoint, token, method, data) => {
    let response = await fetch(
        `${baseURL}${endpoint}`, {
            cors: "no-cors",
            method: method,
            headers: {
                "Authorization": `Token ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    if (response.status === 200) {
        return await response.json();
    }
    return response;
}

export const demo = async (token) => {
    /* POST request */
    let response = await requestEndpoint("/courses/", token, "POST", {
        "code": "IG021G",
        "name": "Projektledning",
        "progression": "A",
        "plan": "update this"
    });
    console.log("POST:", response);

    /* GET request */
    response = await requestEndpoint("/courses/IG021G/", token, "GET");
    console.log("GET:", response);

    /* PUT request */
    response["plan"] = "updated";
    response = await requestEndpoint("/courses/IG021G/", token, "PUT", response);
    console.log("PUT:", response);

    /* DELETE request */
    response = await requestEndpoint("/courses/IG021G/", token, "DELETE", {
        "code": "IG021G"
    });
    console.log("DELETE:", response);
}



