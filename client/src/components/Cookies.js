
import "../CSS/Cookies.css"
import { useGlobalContext } from '../store/context';

const Cookies = () => {

    const { closeCookies, isShowedCookies } = useGlobalContext();
    return(
        <div className={`${isShowedCookies ? 'frame-cookie cookie-showed' : 'frame-cookie cookie-hidden'}`}>
            <div className="text-cookie">
                Ce site utilise des cookies pour améliorer l'expérience utilisateur
                <button className="button-cookie" onClick= {closeCookies}>OK</button>
            </div>
        </div>
    )

}

export default Cookies;