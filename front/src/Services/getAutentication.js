export const login = (email, password, updateTokenFuntion, updateIdFunction) => {
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
      if (resp.status===401){
        alert("Your password is wrong!");
      }
      else if (resp.status===404){
        alert("This email don't exist on data base.");
      } 
      else if (resp.status!==200){
        alert("There has been an error");
      }
      else return resp.json();
    })

    .then(body => {
      sessionStorage.setItem("token", body.access_token);
      sessionStorage.setItem("userId", body.user_id);
      updateTokenFuntion(body.access_token);
      updateIdFunction(body.user_id);
      return true;
    })
    
    .catch(error => {
      console.log("Error:" + error);
    })
  )
}