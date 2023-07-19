import { createContext, useContext, useEffect, useMemo, useState } from "react";

import {useResourse} from "../Hooks/useResourse"
import { getUserData } from '../Services/getUserData'
import { updateFavorites } from '../Services/updateFavorites'


const AppContext = createContext();

export const AppProvider = ({children}) => {
  const [characters, setCharacter]=useResourse('people');
  const [planets, setPlanets]=useResourse('planets');
  const [vehicles, setVehicles]=useResourse('vehicles');

  const [favorites, setFavorites] = useState([]);
  const [token, setToken] = useState('');
  const [userData, setUserData] = useState({});

  

  useEffect(()=>{ 
    const localToken = sessionStorage.getItem("token");
    if (localToken && localToken!==undefined && localToken!==""){
      setToken(localToken);
      getUserData(localToken, setUserData);
      return
    }
  },[token])

  useEffect(()=>{
    if (userData.favorites!==undefined && userData.favorites.length>0){
      userData.favorites.map(person_db=>{
        characters.map(item=>{
          if(item.id === person_db.id){
            return item.favorite = true;
          }
        })
      })

      const favoritesListCharacters = characters.filter((item) => item.favorite === true);
      const favoritesListPlanets = planets.filter((item) => item.favorite === true);
      const favoritesListVehicles = vehicles.filter((item) => item.favorite === true);
  
      const favoritesList = favoritesListCharacters.concat(favoritesListPlanets, favoritesListVehicles);
      setFavorites(favoritesList);
      return
    }
  },[userData])



  const switchFavoritesCharacter = (id) =>{
    const updateCharacters = characters.map(item=>{
      if(item.id === id){
        item.favorite = !item.favorite;
      }
      return item;
    });
    setCharacter(updateCharacters);
    handleFavorites();
  }

  const switchFavoritesPlanets = (id) =>{
    const updatePlanets = planets.map(item=>{
      if(item.id === id){
        item.favorite = !item.favorite;
      }
      return item;
    });
    setPlanets(updatePlanets);
    handleFavorites();
  }

  const switchFavoritesVehicles = (id) =>{
    const updateVehicles = vehicles.map(item=>{
      if(item.id === id){
        item.favorite = !item.favorite;
      }
      return item;
    });
    setVehicles(updateVehicles);
    handleFavorites();
  }

  const deleteFavorite = (id) =>{
    switchFavoritesCharacter(id);
    switchFavoritesPlanets(id);
    switchFavoritesVehicles(id);
  }

  const handleFavorites = () =>{
    const favoritesListCharacters = characters.filter((item) => item.favorite === true);
    const favoritesListPlanets = planets.filter((item) => item.favorite === true);
    const favoritesListVehicles = vehicles.filter((item) => item.favorite === true);

    const favoritesList = favoritesListCharacters.concat(favoritesListPlanets, favoritesListVehicles);
    setFavorites(favoritesList);

    if (token && token!==undefined && token!==""){
      const favoritesListId = favoritesListCharacters.map(person => person.id);
      updateFavorites(token, favoritesListId, setToken);
    }
  }



  const store = useMemo(()=>{
    return  {characters, planets, vehicles, favorites, token, userData}
  },[characters, planets, vehicles, favorites, token, userData]);

  const actions = {
    switchFavoritesCharacter,
    switchFavoritesPlanets,
    switchFavoritesVehicles,
    deleteFavorite,
    setToken,
    setUserData
  }

  return(
    <AppContext.Provider value={{ store, actions }}>
      {children}
    </AppContext.Provider>
  );
}

export const useAppContext = () => useContext(AppContext);