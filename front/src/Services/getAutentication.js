export const login = (email, password, updateFuntion) => {
  return(
    fetch(`${process.env.REACT_APP_API_URL}/api/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    })
    .then(resp =>{
      if (resp.status!==200){
        alert("There has been an error");
        return false;
      } 
      return resp.json();
    })
    .then(body => {
      // console.log(body);
      sessionStorage.setItem("token", body.access_token);
      updateFuntion(body.access_token);
      return true;
    })
    .catch(error => {
      console.log("Error:" + error);
    })
  )
}