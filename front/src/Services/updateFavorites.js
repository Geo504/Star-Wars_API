export const updateFavorites = (token, favorites_id, updateTokenFuntion) => {
  return(
    fetch(`${process.env.REACT_APP_API_URL}/api/users/`, {
      method: 'PUT',
      headers: {
        'Authorization': 'Bearer '+ token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        favorites: favorites_id
      })
    })
    .then(resp =>{
      if (resp.status!==200){
        alert("There has been an error updating user Data");
      }
      else return resp.json();
    })
    .then(body => {
      sessionStorage.setItem("token", body.refresh_token);
      updateTokenFuntion(body.refresh_token);
      return true
    })
    .catch(error => {
      console.log("Error:" + error);
    })
  )
}