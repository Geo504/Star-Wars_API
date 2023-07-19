import React from 'react'
import { Link } from 'react-router-dom';

import style from "./NavBar.module.css"
import { BsTrash2 } from 'react-icons/bs';

export const LiNavBar = ({favorites, deleteFavorite}) => {
  if (favorites.length===0){
    return (
      <li className={`${style.liDropdown} li-Dropdown`}>
        <a className="dropdown-item pe-1" href="#">Empty</a>
      </li>
    )
  }

  if (favorites.length>0) {
    return (
      favorites.map(item=>{
        let element = 'characters';
        if (item.population) element="planets";
        if (item.model) element="vehicles";
        
        return (
          <li key={item.id} className={`${style.liDropdown} li-Dropdown`}>
            <Link className={`${style.dropdownItem} dropdown-item pe-1`} to={`/${element}/${item.id}`}>
              {item.name?item.name:item.model}
            </Link>
            <BsTrash2 className={style.iconNavBar} onClick={()=>deleteFavorite(item.id)}/>
          </li>
        )
      })
    )
  }
}
