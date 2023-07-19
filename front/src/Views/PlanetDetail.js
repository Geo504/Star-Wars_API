import React from 'react';
import { useAppContext } from '../Context/AppContext';
import { useParams } from 'react-router-dom';

import { DiscriptionPlanet } from '../Components/DiscriptionPlanet/DiscriptionPlanet'

export const PlanetDetail = () => {
  const value = useAppContext();
  const params = useParams();

  return (
    <div className='container'>
      {
        value.store.planets.map(item=>{
          if (item.id===params.id) {
            return (
              <DiscriptionPlanet 
                key={item.id}
                planet={item}
              />
            )
          };
        })
      }
    </div>
  )
}