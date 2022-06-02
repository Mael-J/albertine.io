import React, { useState, useContext } from 'react';

const AppContext = React.createContext();

const AppProvider = ({ children }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isShowedMenu, setIsShowedMenu] = useState(true);
  const [isShowedCookies, setIsShowedCookies] = useState(true);

  const openSidebar = () => {
    setIsSidebarOpen(true);
  };
  const closeSidebar = () => {
    setIsSidebarOpen(false);
  };
  const openMenu = () => {
    setIsShowedMenu(true);
  };
  const closeMenu = () => {
    setIsShowedMenu(false);
  };

  const closeCookies = () => {
    setIsShowedCookies(false);
  };


  return (
    <AppContext.Provider
      value={{
        isSidebarOpen,
        openSidebar,
        closeSidebar,
        isShowedMenu,
        closeMenu,
        openMenu,
        closeCookies,
        isShowedCookies,


      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useGlobalContext = () => {
  return useContext(AppContext);
};

export { AppContext, AppProvider };
