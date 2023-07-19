import React from 'react'

import style from './DiscriptionVehicle.module.css'

export const DiscriptionVehicle = ({vehicle}) => {
  const {model, max_speed, crew, cargo_capacity, cost_in_credits, length, image, description} = vehicle;

  return (
    <>

    <div className={`${style.card} card my-4`}>
      <div className="row g-0">

        <div className="col-md-8">
          <img src={image} className={`${style.img} img-fluid rounded-start`} />
        </div>

        <div className={`${style.cardBody} col-md-4`}>
          <div className="card-body">
            <h5 className="card-title text-center">{model}</h5>
            <p className="card-text">
              {description}
            </p>
          </div>
        </div>

      </div>
    </div>

    <div className={`${style.cardGroup} card-group`}>
      <div className={`${style.cardData} card`}>
        <p className='card-text'>Speed:</p>
        <p className='card-text'>{max_speed} km/h</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Crew:</p>
        <p className='card-text'>{crew}</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Cargo capacity:</p>
        <p className='card-text'>{cargo_capacity} tons</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Lenght:</p>
        <p className='card-text'>{length}</p>
      </div>

      <div className={`${style.cardData} card`}>
        <p className='card-text'>Cost:</p>
        <p className='card-text'>{cost_in_credits} credits</p>
      </div>
    </div>

    </>
    
  )
}