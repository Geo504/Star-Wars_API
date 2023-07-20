export const singIn = (username ,email, password) => {
  return(
    fetch(`${process.env.REACT_APP_API_URL}/api/users/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user_name: username,
        email: email,
        password: password,
        // favorites_people: []
      })
    })
    .then(resp =>{
      if (resp.status<200 && resp.status>=300){
        alert("There has been an error creating user");
      }
      else return resp.json();
    })
    .catch(error => {
      console.log("Error:" + error);
    })
  )
}