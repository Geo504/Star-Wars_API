import React from 'react'
import { useAppContext } from '../../Context/AppContext'

import { ElementCard } from '../ElementCard/ElementCard'

import style from './HomeLists.module.css'

export const HomeLists = () => {
  const value = useAppContext();

  return (
    <>
    <div className='mb-3'>
      <h2 className={`${style.pricipalTitle} pricipal-Title`}>Character List</h2>
      <div className='grid gap-3'>
        {value.store.characters.map(item =>
          <ElementCard
            elementType={'characters'}
            uid={item.uid}
            key={item.id}
            id={item.id}
            favorite={item.favorite}
            title={item.name}
            img={item.image}
            favoriteFuntion={value.actions.switchFavoritesCharacter}
          >
            <p><b>Gender:</b> {item.gender}</p>
            <p><b>Height:</b> {item.height} cm.</p>
            <p><b>Mass:</b> {item.mass} kg.</p>
          </ElementCard>
        )}
      </div>
    </div>

    <div className='mb-3'>
      <h2 className={`${style.pricipalTitle} pricipal-Title`}>Planet List</h2>
      <div className='grid gap-3'>
        {value.store.planets.map(item =>
          <ElementCard
            elementType={'planets'}
            key={item.id}
            id={item.id}
            uid={item.uid}
            favorite={item.favorite}
            title={item.name}
            img={item.image}
            favoriteFuntion={value.actions.switchFavoritesPlanets}
          >
            <p><b>Population:</b> {item.population}</p>
            <p><b>Diameter:</b> {item.diameter} km.</p>
            <p><b>Terrain:</b> {item.terrain}</p>
          </ElementCard>
        )}
      </div>
    </div>

    <div className='mb-3'>
      <h2 className={`${style.pricipalTitle} pricipal-Title`}>Vehicle List</h2>
      <div className='grid gap-3'>
        {value.store.vehicles.map(item =>
          <ElementCard
            elementType={'vehicles'}
            key={item.id}
            id={item.id}
            uid={item.uid}
            favorite={item.favorite}
            title={item.model}
            img={item.image}
            favoriteFuntion={value.actions.switchFavoritesVehicles}
          >
            <p><b>Speed:</b> {item.max_speed}km/h</p>
            <p><b>Passengers:</b> {item.crew} </p>
            <p><b>Cargo capacity:</b> {item.cargo_capacity} tons</p>
          </ElementCard>
        )}
      </div>
    </div>
    </>

  )
}
