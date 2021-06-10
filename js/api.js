const axios = require('axios');

const callApi = async () => {
    const data = await axios.put('http://127.0.0.1:5000/drugs', {"name": "ansoline"});
    console.log(data.data);
}

callApi();
