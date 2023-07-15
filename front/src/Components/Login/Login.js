import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { useNavigate } from 'react-router-dom';

import { login } from '../../Services/getAutentication'
import { singIn } from '../../Services/createUser'
import { useAppContext } from '../../Context/AppContext'

import style from "./Login.module.css"

export const Login = () => {
  const value = useAppContext();
  const [loginMode, setLoginMode] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [userName, setUserName] = useState('');
  
  const navigate = useNavigate()
  const token = value.store.token;


  const changeLoginForm = () => {
    setLoginMode(!loginMode);
  }

  const handleEmailInput = (e) =>{
    setEmail(e.target.value)
  }
  const handlePasswordInput = (e) =>{
    setPassword(e.target.value)
  }
  const handleUserNameInput = (e) =>{
    setUserName(e.target.value)
  }

  
  const submitFuntion = async(e)=>{
    e.preventDefault();
    
    if (loginMode==true){
      login(email, password, value.actions.setToken, value.actions.setUserId).then(()=>{
        navigate('/');
        setPassword('');
      });
    }
    else {
      singIn(userName, email, password)
      .then(()=>{
        login(email, password, value.actions.setToken, value.actions.setUserId)
      })
      .then(()=>{
        navigate('/');
        setPassword('');
      })
    }

  }


  const singOut = () =>{
    sessionStorage.removeItem("token");
    value.actions.setToken('');
    navigate('/');
  }

  // value.store.userData.user_name

  return (
    <div className={'modal fade'} id={`loginModal`} data-bs-backdrop="static">
      <div className='modal-dialog modal-dialog-centered justify-content-center'>
        <div className={`${style.modal_content} modal-content`}>

          <div className={`col-12`}>
            <button className={style.icon_close} type='button' data-bs-dismiss="modal">
              <ion-icon name="close-outline"></ion-icon>
            </button>

            <div className={style.login}>
            {
              token && token!=="" && token!==undefined ?
              (
                <>
                <h2>Welcome {value.store.userData.user_name}!!</h2>
                <button className={style.log_out} onClick={singOut}>
                <ion-icon name="log-out-outline"></ion-icon>
                  Sing out
                </button>
                </>
              ):(
                <>
                <h2>{loginMode?'Login':'Sing In'}</h2>
                
                <form onSubmit={submitFuntion}>

                  {loginMode?
                    '':
                    <div className={style.input_box}>
                      <span className={style.icon}>
                        <ion-icon name="person-outline"></ion-icon>
                      </span>
                      <input type='text' value={userName} onChange={handleUserNameInput} required/> 
                      <label>Username:</label>
                    </div>
                  }

                  <div className={style.input_box}>
                    <span className={style.icon}>
                      <ion-icon name="mail-outline"></ion-icon>
                    </span>
                    <input type='email' value={email} onChange={handleEmailInput} required/>
                    <label>Email:</label>
                  </div>

                  <div className={style.input_box}>
                    <span className={style.icon}>
                      <ion-icon name="lock-closed-outline"></ion-icon>
                    </span>
                    <input type='password' value={password} onChange={handlePasswordInput} required/> 
                    <label>Password:</label>
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
                      <button type='button' className={style.register_link} onClick={changeLoginForm}>
                        {loginMode?'Sing in':'Login'}
                      </button>
                    </p>
                  </div>
                </form>
                </>
              )
            }

            </div>
          </div>

        </div>
      </div>
    </div>
  )
}
