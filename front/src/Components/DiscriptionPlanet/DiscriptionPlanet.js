import React from 'react'

import style from './DiscriptionPlanet.module.css'

export const DiscriptionPlanet = ({planet}) => {
  const {name, population, diameter, terrain, climate, surface_water, image, description} = planet;

  return (
    <>
    <div className={`${style.card} card my-4`}>
      <div className="row g-0">

        <div className="col-md-8">
          <img src={image} className={`${style.img} img-fluid rounded-start`} />
        </div>

        <div className={`${style.cardBody} col-md-4`}>
          <div className="card-body">
            <h5 className="card-title text-center">{name}</h5>
            <p className="card-text">
              {description}
            </p>
          </div>
        </div>

      </div>
    </div>

    <div className={`${style.cardGroup} card-group`}>
      <div className={`${style.cardData} card`}>
        <p className='card-text'>Population:</p>
        <p className='card-text'>{population}</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Diameter:</p>
        <p className='card-text'>{diameter} km.</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Terrain:</p>
        <p className='card-text'>{terrain}</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Climate:</p>
        <p className='card-text'>{climate}</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Surface water:</p>
        <p className='card-text'>{surface_water}%</p>
      </div>
    </div>

    </>
    
  )
}