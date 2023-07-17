import React from 'react';
import { useAppContext } from '../Context/AppContext';
import { useParams } from 'react-router-dom';

import { DiscriptionVehicle } from '../Components/DiscriptionVehicles/DiscriptionVehicle';

export const VehicleDetail = () => {
  const value = useAppContext();
  const params = useParams();

  return (
    <div className='container'>
      {
        value.store.vehicles.map(item=>{
          if (item.id===params.id) {
            return (
              <DiscriptionVehicle 
                key={item.id}
                vehicle={item}
              />
            )};
          return
        })
      }
    </div>
  )
}