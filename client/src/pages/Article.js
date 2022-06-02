import { useGlobalContext } from '../store/context';
import { useEffect } from "react";
import '../CSS/Article.css';
import { BsDownload } from 'react-icons/bs'; 

const Article = () => {

    const { openMenu } = useGlobalContext();

    useEffect(()=> {
        openMenu();
        document.body.style.backgroundColor = '#A59FD3'
        
    }, []);

    

    return (
        <div align = 'center'>
            <h1 className='title-article'>Articles</h1>
            <table className='table-article'>
                <thead className='thead-article'>
                    <tr>
                        <td style= {{width: "50%"}}>
                            Description
                        </td>
                        <td style= {{width: "25%"}}>
                            Mise à jour
                        </td>
                        <td style= {{width: "25%"}}>
                            Télécharger
                        </td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <a className = "link-article" href={"/#/pdf/manifeste"} target='_blank'>Manisfeste de la finance verte</a>
                            
                        </td>
                        <td>01/06/2022</td>
                        <td><a className = "link-article" href={"/#/pdf/manifeste"} target='_blank'>{<BsDownload />}</a></td>
                    </tr>
                </tbody>
            </table>

        </div>
    )

}

export default Article;