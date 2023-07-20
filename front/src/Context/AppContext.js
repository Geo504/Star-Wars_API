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
      getUserData(localToken, setUserData);
      setToken(localToken);
      return
    }
  },[token])

  useEffect(()=>{
    if (userData.favorites_people!==undefined && userData.favorites_people.length>0){
      userData.favorites_people.map(person_db=>{
        characters.map(item=>{
          if(item.id === person_db.id){
            item.favorite = true;
          }
        })
      })
    }
    if (userData.favorites_planets!==undefined && userData.favorites_planets.length>0){
      userData.favorites_planets.map(planet_db=>{
        planets.map(item=>{
          if(item.id === planet_db.id){
            item.favorite = true;
          }
        })
      })
    }
    if (userData.favorites_vehicles!==undefined && userData.favorites_vehicles.length>0){
      userData.favorites_vehicles.map(vehicle_db=>{
        vehicles.map(item=>{
          if(item.id === vehicle_db.id){
            item.favorite = true;
          }
        })
      })
    }

    const favoritesListCharacters = characters.filter((item) => item.favorite === true);
    const favoritesListPlanets = planets.filter((item) => item.favorite === true);
    const favoritesListVehicles = vehicles.filter((item) => item.favorite === true);

    const favoritesList = favoritesListCharacters.concat(favoritesListPlanets, favoritesListVehicles);
    setFavorites(favoritesList);
    return
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

  const deleteFavorite = (id, element) =>{
    if (element==='characters'){switchFavoritesCharacter(id)};
    if (element==='planets'){switchFavoritesPlanets(id)};
    if (element==='vehicles'){switchFavoritesVehicles(id)};
  }

  const handleFavorites = () =>{
    const favoritesListCharacters = characters.filter((item) => item.favorite === true);
    const favoritesListPlanets = planets.filter((item) => item.favorite === true);
    const favoritesListVehicles = vehicles.filter((item) => item.favorite === true);

    const favoritesList = favoritesListCharacters.concat(favoritesListPlanets, favoritesListVehicles);
    setFavorites(favoritesList);

    if (token && token!==undefined && token!==""){
      const favoritesListId = favoritesList.map(item => item.id);
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