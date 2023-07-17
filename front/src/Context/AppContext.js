import { createContext, useContext, useEffect, useMemo, useState } from "react";

// import {useResourses} from "../Hooks/useResourses"
import {useResourse} from "../Hooks/useResourse"
import { getUserData } from '../Services/getUserData'


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
      return
    } 
  },[])

  useEffect(()=>{
    if (token && token!==undefined && token!==""){
      getUserData(token, setUserData);
      return
    } 
  },[token])



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