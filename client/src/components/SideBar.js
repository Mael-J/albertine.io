import React from 'react';
import Logo from '../assets/logo.png'
import { useGlobalContext } from '../store/context';
import { FaTimes, FaLinkedin, FaLemon, FaGithub} from 'react-icons/fa';
import { GiCherry } from 'react-icons/gi';
import { GiKiwiFruit } from 'react-icons/gi';
import '../CSS/SideBar.css'


const Sidebar = () => {
  const { isSidebarOpen, closeSidebar } = useGlobalContext();

  return (
    <aside className={`${isSidebarOpen ? 'sidebar show-sidebar' : 'sidebar'}`}>
      <div className='sidebar-header'>
        <img src={Logo} className='logo-sidebar' alt='Albertine' />
        <button className='close-btn' onClick={closeSidebar}>
          <FaTimes />
        </button>
      </div>
      <ul className='links'>
        <li key = {1}>
        <a href={"/"}>
                {<GiCherry />}
                {'Accueil'}
              </a>
        </li>
        <li key = {2}>
        <a href={"/#/funds"}>
                {<FaLemon />}
                {'Analyse de fonds'}
              </a>
        </li>
        <li key = {3}>
        <a href={"/#/articles"}>
                {<GiKiwiFruit />}
                {'Articles'}
              </a>
        </li>
      </ul>
      <ul className='social-icons'>
        <li key={1}>
            <a href="https://www.linkedin.com/company/albertine-letempsretrouve" target="_blank">{<FaLinkedin />}</a>
        </li>
        <li key={2}>
          <a href="https://github.com/Mael-J/albertine.io" target="_blank">{<FaGithub />}</a>
        </li>
      </ul>
    </aside>
  );
};

export default Sidebar;
