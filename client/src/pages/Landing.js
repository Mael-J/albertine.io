
import { useGlobalContext } from '../store/context';
import { useEffect } from "react";
import Logo from '../assets/logo.png';
import '../CSS/Landing.css';

import Cookies from '../components/Cookies'

const colors = [
    '#D39FC3',
    '#A59FD3',
  ];

const Landing = () => {
    // const [color, setColor] = React.useState(0);

    // React.useEffect(() => {
        
    //     const interval = setInterval(() => {
            
    //         setColor((v) => (v === 0 ? 1 : 0));
            
    //     }, 5000);
    //   }, []);

    const { openMenu } = useGlobalContext();

    useEffect(()=> {
        openMenu();
        document.body.style.backgroundColor = '#A59FD3';
        
    }, []);
   

      return (
        <section>

            <div align = 'center'>
                <img className="logo-landing" src={Logo} alt="Albertine"/>

                <div className="introduction">
                    <p>Albertine gère vos données.</p>
                    <p >Vous aurez tout le temps de vous concentrer sur ce qui importe vraiment.</p>

                </div>
                <div className="mt-5">
                    <a className="discover-button" href="mailto:albertine@albertine.io?subject=Albertine, je veux retrouver du temps">Découvrir</a>
                </div>
            </div>
            {/* <div align="center">
                <Cookies />
            </div> */}
            
            
        </section>
      );

}


export default Landing;