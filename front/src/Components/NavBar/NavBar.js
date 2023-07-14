import React from "react";
import { Link } from "react-router-dom";

import { useAppContext } from '../../Context/AppContext'
import { LiNavBar } from "./LiNavBar";
import {Login} from "../Login/Login"

import style from "./NavBar.module.css"

export const NavBar = () => {
  const value = useAppContext();


  return (
    <>
    <nav className={`${style.navbar} navbar navbar-expand-sm nav-underline`} data-bs-theme="dark">
      <div className="container-fluid">

        <Link className={`${style.navbarBrand} navbar-brand`} to="/">STAR WARS</Link>
        
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#favoritesDropdown">
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="favoritesDropdown">
          <ul className="navbar-nav nav-underline gap-0 ms-auto">
            
            <li className="nav-item">
              <button className="nav-link" data-bs-toggle="modal" data-bs-target="#loginModal">Sing In</button>
            </li>

            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                Favorites
              </a>

              <ul className="dropdown-menu dropdown-menu-end">
                {
                  <LiNavBar
                    favorites={value.store.favorites}
                    deleteFavorite={value.actions.deleteFavorite} />
                } 
              </ul>
            </li>

          </ul>
        </div>

      </div>
    </nav>
    <Login />
    </>
  );
};
