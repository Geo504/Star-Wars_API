import React, { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'

import { login } from '../../Services/getAutentication'

import style from "./Login.module.css"

export const Login = () => {
  const [loginMode, setLoginMode] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const changeLoginForm = () => {
    setLoginMode(!loginMode);
  }

  const handleEmailInput = (e) =>{
    setEmail(e.target.value)
  }
  const handlePasswordInput = (e) =>{
    setPassword(e.target.value)
  }

  
  const submitFuntion = async(e)=>{
    const urlSuffix = loginMode ? 'login' : 'singup';

    e.preventDefault();
    const token_num = await (login(`${process.env.REACT_APP_API_URL}/api/auth/${urlSuffix}`, {email, password}));
    console.log(token_num)
  }

  return (
    <div className=' modal fade' id={`loginModal`} data-bs-backdrop="static">
      <div className='modal-dialog modal-dialog-centered justify-content-center'>
        <div className={`${style.modal_content} modal-content`}>

          <div className={`col-12`}>
            <button className={style.icon_close} type='button' data-bs-dismiss="modal">
              <ion-icon name="close-outline"></ion-icon>
            </button>

            <div className={style.login}>
              <h2>{loginMode?'Login':'Register'}</h2>
              
              <form onSubmit={submitFuntion}>
                <div className={style.input_box}>
                  <span className={style.icon}>
                    <ion-icon name="mail-outline"></ion-icon>
                  </span>
                  <input type='email' value={email} onChange={handleEmailInput} required/>
                  <label>email</label>
                </div>

                <div className={style.input_box}>
                  <span className={style.icon}>
                    <ion-icon name="lock-closed-outline"></ion-icon>
                  </span>
                  <input type='password' value={password} onChange={handlePasswordInput} required/> 
                  <label>password</label>
                </div>

                <div className={style.remember_forgot}>
                  <label>
                    <input type='checkbox' />
                    {loginMode?'Remember me':'I agreed to the terms & conditions'}
                  </label>
                  {loginMode?(<Link className={style.forgot_link} to='#'>Forgot Password?</Link>):''}
                </div>

                <button type='submit' className={style.submit_btn}>{loginMode?'Login':'Register'}</button>
                
                <div className={style.login_register}>
                  <p>
                    {loginMode?"Don't have an account?":"You already have an account?"}
                    <button className={style.register_link} onClick={changeLoginForm}>
                      {loginMode?'Register':'Login'}
                    </button>
                  </p>
                </div>
              </form>

            </div>
          </div>

        </div>
      </div>
    </div>
  )
}
