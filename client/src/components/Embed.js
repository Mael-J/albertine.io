
import { useEffect } from "react";
import { useGlobalContext } from '../store/context';
import Manifest from "../utils/article/Manifeste-de-la-finance-verte-et-transparente.pdf";
import "../CSS/Embed.css";

const Embed = () => {

    const { closeMenu, closeSidebar } = useGlobalContext();

    useEffect(()=> {
        closeMenu();
        closeSidebar();
    }, []);
    
    return (
        <div  className="size-pdf">
            <object data={Manifest} type="application/pdf" className="size-pdf">
            
            </object>
        </div>
    )
}

export default Embed;