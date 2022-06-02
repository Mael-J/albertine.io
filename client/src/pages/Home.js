import { useContext, useState } from "react";
import { FaBars } from 'react-icons/fa';
import '../CSS/Home.css'
import { useGlobalContext } from '../store/context';

const Home = () => {
  const { openSidebar, isShowedMenu} = useGlobalContext();
    return (
      <div className={`${isShowedMenu ? 'menu-button-showed' : 'menu-button-hidden'}`}>
        <button onClick={openSidebar}  className='sidebar-toggle'>
          <FaBars />
        </button>
    </div>
    );
  };
  
  export default Home;