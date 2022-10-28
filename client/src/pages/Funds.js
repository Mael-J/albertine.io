import { useState, useEffect } from "react";
import { useGlobalContext } from '../store/context';

import DeleteIcon from '@mui/icons-material/Delete';
import '../CSS/Funds.css'
import Select from 'react-select';
import Loading from '../utils/image/loading2.svg';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
// const baseURL = 'http://localhost:4000/api/funds';

//const baseURL = 'http://jtpnrui.cluster030.hosting.ovh.net/api/funds';



const Funds = () => {
    const { openMenu } = useGlobalContext();

    useEffect(()=> {
        openMenu();
        
    }, []);

    useEffect(()=> {document.body.style.backgroundColor = '#252525'})
    //color
    const green = '#32D01B';
    const yellow = '#FFCA17';
    const orange = '#FF6417';
    const red = '#D80000';
    const black = "#000000";
    //color of the graph
    const graphColor = ["#3A2F8F", "#AB5E93", "#FF993A"];

    // format of export
    const [exportFormat, setExportFormat] = useState('json');


    //portfolio code and name
    const [portfolios, setPortfolios] = useState([]);
    //options companies
    const [portList, setPortList] = useState([]);
    //infos on portfolios
    const [portInfos, setPortInfos] = useState([]);
    // check is fetching fund is done
    const [fundIsLoading, setFundIsLoading] = useState(false);
    // marketCAP data
    const [marketCap, setMarketCap] = useState([
        {name :'géante'},
        {name : 'grande'},
        {name :'moyenne'},
        {name : 'petite'},
        {name : 'micro'},]);

    const [histoData, setHistoData] = useState([])
    //sector data
    const [sectorData, setSectorData] = useState([
        {name : "Conso. discrétionnaire"},
        {name : "Conso. de base"},
        {name : "Energie"},
        {name : "Finance"},
        {name : "Immobilier"},
        {name : "Industrie"},
        {name : 'Matériaux'},
        {name : "Santé"},
        {name : "Technologies"},
        {name : "Télécom"},
        {name : "Utilities"}
        ]);

    // bondsType
    const [bondsType, setBondsType] = useState([
        {name : "Gouvernement"},
        {name : "Municipalité"},
        
        {name : "Entreprise"},
        {name : "Titrisé"},
        {name : "Cash"},
        {name : "Dérivés"},

    ]);

    //bondQuality
    const [bondsQuality, setBondsQuality] = useState([
        {name : "AAA"},
        {name : "AA"},
        {name : "A"},
        {name : "BBB"},
        {name : "BB"},
        {name : "B"},
        {name : "< B"},
        {name : "Non noté"},
    ]);



    // style of react select
    const customStyles = {
        menu: (provided, state) => ({
          ...provided,
          
          
          color: 'black',
          zIndex: 10,
          
          
        }),
        container: (provided, state) => ({
            ...provided,
            
            
            width: '20rem',
            
            
          }),
      
      }

    // get fund list based on user input (list of 10 funds)
    const getPortfolioList = (selectedOption) => {

        fetch(`/api/funds/fundlist/${selectedOption}`).then(response => response.json()
        ).then(jsonData => {
            
            setPortList(jsonData);
        }).catch(error=> {
            console.error(error.message);
        });
    }

    const exportData = () => {
        if (exportFormat == 'json') {
            const jsonString = `data:text/json;chatset=latin-1,${encodeURIComponent(
                JSON.stringify(portInfos)
              )}`;
              const link = document.createElement("a");
              link.href = jsonString;
              link.download = "albertine_letempsretrouve.json";
          
              link.click();

        } else if (exportFormat == 'xlsx') {
            const response =  fetch(`/api/funds/download/excel`,
            {
                method : 'POST',
                headers: {"Content-type": "application/json"},
                body: JSON.stringify(portInfos),
                //mode : 'cors',
                //responseType: 'blob'
            }).then((response) => {
                return response
               
            }).then(res => {
                res.blob().then((blob)=> {
                    const url = URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.href = url;
                    link.download = "albertine_letempsretrouve.xlsx";
                
                    link.click();
                    
                  });
                

            }).catch(error => {
                console.error(error.message)
            });

        } else if (exportFormat == 'pdf') {
            const response =  fetch(`/api/funds/download/pdf`,
            {
                method : 'POST',
                headers: {"Content-type": "application/json"},
                body: JSON.stringify(portInfos),
                //mode : 'cors',
                //responseType: 'blob'
            }).then((response) => {
                return response
               
            }).then(res => {
                res.blob().then((blob)=> {
                    const url = URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.href = url;
                    link.download = "albertine_letempsretrouve.pdf";
                
                    link.click();
                    
                  });
                

            }).catch(error => {
                console.error(error.message)
            });

        }

    }




    const analysePort = () =>  {

        setExportFormat('json');

        setMarketCap([ {name :'géante'},
        {name : 'grande'},
        {name :'moyenne'},
        {name : 'petite'},
        {name : 'micro'}]);
        
        setSectorData([{name : "Conso. discrétionnaire"},
        {name : "Conso. de base"},
        {name : "Energie"},
        {name : "Finance"},
        {name : "Immobilier"},
        {name : "Industrie"},
        {name : 'Matériaux'},
        {name : "Santé"},
        {name : "Technologies"},
        {name : "Télécom."},
        {name : "Utilities"}
    ]);
        
        setBondsType([ {name : "Gouvernement"},
        {name : "Municipalité"},
        
        {name : "Entreprise"},
        {name : "Titrisé"},
        {name : "Cash"},
        {name : "Dérivés"}]);
        
        setBondsQuality([{name : "AAA"},
        {name : "AA"},
        {name : "A"},
        {name : "BBB"},
        {name : "BB"},
        {name : "B"},
        {name : "< B"},
        {name : "Non noté"}]);
        
        setPortInfos([]);

        
        if (portfolios.length >0) {
            setFundIsLoading(true);
        } else {
            setFundIsLoading(false);
        }
        
        // portfolios.map((funds, i) => {
        //     if (funds !==null){
        //         setFundIsLoading(true);
                
        //         fetch(`/api/funds/info/${funds['value']}`).then(
        //             response => {
        //                 return response.json()
        //             }
        //         ).then(response => {
        //             //portInfos[i] = response;
                    
        //             setPortInfos(prev => [...prev, response]);
                    
                    
        //             //fetching is done
        //             setFundIsLoading(false);
        //         }).catch(error => {
        //             console.error(error.message);
        //         })
        //     }
        // });

        fetch(`/api/funds/currentdata?code=${JSON.stringify(portfolios)}`).then(response => {
            return response.json();
        }).then(response => {
            setPortInfos(response);
                
                //fetching is done
                 setFundIsLoading(false);
            }).catch(error => {
                console.error(error.message);
            });

        fetch(`/api/funds/historicaldata?code=${JSON.stringify(portfolios)}`).then(response => {
            return response.json();
        }).then(response => {
                setHistoData(response);
                
            }).catch(error => {
                console.error(error.message);
            });

    }
    const modifyPortfolioBis = (listFunds) => {
        
        setPortfolios(listFunds);
       

    }

    //user modify funds in input
    const modifyPortfolio = (index, val) => {
        //we are searching the fund
        
        portfolios[index] = val;
        setPortfolios([...portfolios]);
        
        if (val !==null){
            setFundIsLoading(true);
            fetch(`/api/funds/info/${val['value']}`).then(
                response => {
                    return response.json()
                }
            ).then(response => {
                portInfos[index] = response;
                setPortInfos([...portInfos]);
                
                //fetching is done
                setFundIsLoading(false);
            }).catch(error => {
                console.error(error.message);
            })
        }
                   
        



    }
    // user remove funds in select
    const removePortfolio = (index) => {

        marketCap.forEach(function(v){ delete v[portfolios[index]['label']] });
        setMarketCap(marketCap);
        sectorData.forEach(function(v){ delete v[portfolios[index]['label']]});
        setSectorData(sectorData);
        bondsType.forEach(function(v){ delete v[portfolios[index]['label']]});
        setBondsType(bondsType);
        bondsQuality.forEach(function(v){ delete v[portfolios[index]['label']]});
        setBondsQuality(bondsQuality);
        portfolios.splice(index,1);
        setPortfolios([...portfolios]);
        portInfos.splice(index,1);
        setPortInfos([...portInfos]);
        

    }

    // user add funds in select
    const addPortfolio = () => {
        // portfolios.push({"code" :''});
        setPortfolios([...portfolios, {"value" :'', 'label' :''}]);
        setPortInfos([...portInfos,{}])
    }

    //button to add funds
    const buttonAddInputPort = () => {
        
            return (
            <div className="mt-4">
                <button className="button-addInput" onClick={analysePort} disabled={fundIsLoading}>Analyser</button>
            </div>
            )
        
    }

    const inputPortfolioListBis = () => {
        return (
            <div>
                <div>
                    <label>Choix de fonds (max. 3) </label>
                </div>
                <div>
                    
                    <Select 
                    placeholder={"Entrez un nom ou un isin"}
                    styles = {customStyles}
                    value ={portfolios}
                    options= {portList}
                    onInputChange= {getPortfolioList}
                    onChange = {(val) => modifyPortfolioBis(val)}
                    isMulti
                    isClearable={false}
                    isSearchable={true}
                    className="basic-multi-select"
                    classNamePrefix="select"
                    isOptionDisabled={(option) => portfolios.length >= 3}
                    
                    />

                </div>
            </div>
        )

    }

    //div with funds selection
    const inputPortfolioList = () => {
        if (portfolios.length === 1) {
            return (
                <div>
                    <div>
                        <label>Portefeuille n°{1}</label>
                    </div>
                    <div>
                        
                        <Select 
                        styles= {customStyles}
                        value ={portfolios[0]}
                        options= {portList}
                        onInputChange= {getPortfolioList}
                        onChange = {(val) => modifyPortfolio(0, val)}
                        isClearable={false}
                        isSearchable={true}/>
                    </div>
                </div>
            )
        } 
        else {
            return (
                <div>
                    {portfolios.map((portfolio, i)=> (
                    <div key={`portfolioinput${i}`}>
                        <div>
                            <label>Portefeuille n°{i+1}</label>
                        </div>
                        <div style = {{display: "inline-flex"}}>
                            
                            <Select 
                            styles= {customStyles}
                            value ={portfolio}
                            options= {portList}
                            onInputChange= {getPortfolioList}
                            onChange = {(val) => modifyPortfolio(i, val)}
                            isClearable={false}
                            isSearchable={true}/>
                            
                            
                        
                        
                            <button className="button-delete" onClick={() => removePortfolio(i)}><DeleteIcon/></button>
                        </div>
                    </div>
                    )
                    )}
                </div>
            )
            
        }
    }

    //display animation while fetching
    const waitingSvg = () => {
        return(
            <div className="mt-4">
                <object style={{width : '5%'}} type="image/svg+xml" data={Loading}>svg-animation</object>
            </div>)
        

    }

    // fund info
    const fundInfo = () => {
        if (portInfos.length === 0) {
            return (<div></div>) }
        else if (portInfos[0] === 0) {
            return (<div className="mt-4">Aucunes données à afficher pour ces fonds, veuillez sélectionner d'autres fonds.</div>)
        
        } else {

        
        return (
            <div>
                <div className="mt-4">
                <div>
                <select onChange={(e) => setExportFormat(e.target.value)}>
                    <option value="json">JSON</option>
                    <option value="pdf">PDF</option>
                    <option value="xlsx">XLSX</option>
                </select>
                </div>
                <div>
                <button className = "button-export mt-1" type="button" onClick={exportData}>
                    Exporter les données
                </button>
                </div>
                </div>
                <div className="mt-4">
                    <h2>Objectif de gestion</h2>
                        {portInfos.map((obj, i) => {

                            
                            if (obj // 👈 null and undefined check
                            && Object.keys(obj).length === 0
                            && Object.getPrototypeOf(obj) === Object.prototype){
                                //pass
                            } else {
                                return (
                                    <div key={`objective${i}`} className='objective frame-text' style ={{width : `${90/portfolios.length}%`}}>
                                        <div className="sub-title">{obj['infos']['LegalName']}</div>
                                        <div align ="center">
                                            <div className = 'hline mt-2'></div>
                                        </div>
                                        
                                    <p className="mt-2">{obj['pages']['objective']}</p>
                                    </div>
                                    
                                )
                                
                            }

                        

                    })}
            </div>
            <div className="mt-4">
            <h2>Caractéristiques</h2>
            <div className=" frame-text">
            
                <div className="sub-title">Principales caractéristiques</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                <table className="table-exclude mt-2">
                <thead>
                <tr>
                    <td style ={{width : '30%'}}></td>
                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return (
                                       
                                <td style={{width :`${70/portfolios.length}%`}}>{obj['infos']['LegalName']} </td>

                            )}
                            
                        })}
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                                <td>ISIN</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['pages']['ISIN']}</td>
                            )
                        }})}
                        </tr>
                        <tr>
                                <td>Devise</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['infos']['PriceCurrency']}</td>
                            )
                        }})}
                        </tr>
                        <tr>
                            <td>Actif net</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{(obj['infos']['FundTNAV']/1000000).toFixed(2)} M {obj['infos']['PriceCurrency']}</td>
                            )
                        }})}

                        </tr>
                        <tr>
                            <td>Valeur liquidative</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['infos']['ClosePrice']} {obj['infos']['PriceCurrency']}</td>
                            )
                        }})}

                        </tr>
                        
                        <tr>
                            <td>Eligible PEA</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['pages']['PEA']}</td>
                            )
                        }})}

                        </tr>
                        <tr>
                            <td>Eligible PEA PME</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['pages']['PEAPME']}</td>
                            )
                        }})}

                        </tr>
                        <tr>
                            <td>Structure légale</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['pages']['Structure légale']}</td>
                            )
                        }})}

                        </tr>
                        <tr>
                            <td>UCITS</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['pages']['UCITS']}</td>
                            )
                        }})}

                        </tr>
                        <tr>
                            <td>Société de gestion</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td>{obj['pages']['Société de gestion']}</td>
                            )
                        }})}

                        </tr>
                        <tr>
                            <td>Site internet</td>
                            {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return(
                                <td><a target='_blank' href={`https://${obj['pages']['Site Internet']}`}>{obj['pages']['Site Internet']}</a></td>
                            )
                        }})}

                        </tr>
                        </tbody>
                        </table>
            </div>
            </div>
            <div className="mt-2">
            <h2>Performance (base 100)</h2>
                <LineChart
                    width={500}
                    height={500}
                    data={histoData}
                    margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                    }}>
                    <XAxis dataKey="date"  angle={-45} textAnchor="end" height={120} />
                    <YAxis domain={['auto', 'auto']}/>
                    <Tooltip />
                    <Legend />
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        return(
                        <Line type="monotone" dataKey={obj['infos']['LegalName']} stroke={graphColor[i]} dot={false} />)
                        
                    }
                    })}


                </LineChart>
            </div>
            <div className="mt-2">
                <h2>Performance</h2>
                <div className=" frame-text">
                    <div className="sub-title">Performance cumulée (en %)</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                    <table className="table-data mt-2">
                        <thead>
                            <tr>
                                <td></td>
                                <td>Début de l'année</td>
                                <td>1 jour</td>
                                <td>1 semaine</td>
                                <td>1 mois</td>
                                <td>3 mois</td>
                                <td>6 mois</td>
                                <td>1 an</td>
                                <td>3 ans (annualisée)</td>
                                <td>5 ans (annualisée)</td>
                                <td>10 ans (annualisée)</td>
                            </tr>
                        </thead>
                        <tbody>
                        {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return (
                            <tr key={`cumulativeperformance${i}`} style={{height : '4rem'}}>
                                <td className="first-col">{obj['infos']['LegalName']}</td>
                                {parseFloat(obj['pages']["fund_cumulative_performance_Début d'année"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_Début d'année"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_Début d'année"]}</td>}
                                

                                {parseFloat(obj['pages']["fund_cumulative_performance_1 jour"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_1 jour"]}</td> : 
                                <td style={{color :`${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_1 jour"]}</td>}
                                

                                {parseFloat(obj['pages']["fund_cumulative_performance_1 semaine"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_1 semaine"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_1 semaine"]}</td>}
                                

                                {parseFloat(obj['pages']["fund_cumulative_performance_1 mois"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_1 mois"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_1 mois"]}</td>}

                                {parseFloat(obj['pages']["fund_cumulative_performance_3 mois"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_3 mois"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_3 mois"]}</td>}
                                

                                {parseFloat(obj['pages']["fund_cumulative_performance_6 mois"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_6 mois"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_6 mois"]}</td>}
                                
                                {parseFloat(obj['pages']["fund_cumulative_performance_1 an"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_1 an"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_1 an"]}</td>}
                                
                                {parseFloat(obj['pages']["fund_cumulative_performance_3 ans (annualisée)"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_3 ans (annualisée)"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_3 ans (annualisée)"]}</td>}
                                
                                {parseFloat(obj['pages']["fund_cumulative_performance_5 ans (annualisée)"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_5 ans (annualisée)"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_5 ans (annualisée)"]}</td>}
                                
                                {parseFloat(obj['pages']["fund_cumulative_performance_10 ans (annualisée)"]) <0 ? 
                                <td style={{color : `${red}`, width : '8.5%'}}>{obj['pages']["fund_cumulative_performance_10 ans (annualisée)"]}</td> : 
                                <td style={{color : `${green}`, width : '8.5%'}} >{obj['pages']["fund_cumulative_performance_10 ans (annualisée)"]}</td>}
                                
                                
                            </tr>
                            )
                            
                        }

                    })}

                        </tbody>
                    </table>
                </div>
                <div className=" frame-text mt-4">
                    <div className="sub-title">Performance annuelle (en %)</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                    <table className="table-data mt-2">
                        <thead>
                            <tr>
                                <td></td>
                                <td>{new Date().getFullYear()-7}</td>
                                <td>{new Date().getFullYear()-6}</td>
                                <td>{new Date().getFullYear()-5}</td>
                                <td>{new Date().getFullYear()-4}</td>
                                <td>{new Date().getFullYear()-3}</td>
                                <td>{new Date().getFullYear()-2}</td>
                                <td>{new Date().getFullYear()-1}</td>
                                <td>{new Date().getFullYear()}</td>

                            </tr>
                        </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        return (
                        <tr key={`annualperformance${i}`}>
                            <td className="first-col">{obj['infos']['LegalName']}</td>
                            {parseFloat(obj['pages'][`${new Date().getFullYear()-7}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-7}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-7}_funds_performance`]}</td>}
                            {parseFloat(obj['pages'][`${new Date().getFullYear()-6}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-6}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-6}_funds_performance`]}</td>}

                            {parseFloat(obj['pages'][`${new Date().getFullYear()-5}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-5}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-5}_funds_performance`]}</td>}

                            {parseFloat(obj['pages'][`${new Date().getFullYear()-4}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-4}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-4}_funds_performance`]}</td>}

                            {parseFloat(obj['pages'][`${new Date().getFullYear()-3}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-3}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-3}_funds_performance`]}</td>}

                            {parseFloat(obj['pages'][`${new Date().getFullYear()-2}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-2}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-2}_funds_performance`]}</td>}

                            {parseFloat(obj['pages'][`${new Date().getFullYear()-1}_funds_performance`]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages'][`${new Date().getFullYear()-1}_funds_performance`]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages'][`${new Date().getFullYear()-1}_funds_performance`]}</td>}

                            {parseFloat(obj['pages']["fund_cumulative_performance_Début d'année"]) <0 ? 
                                <td style={{color : `${red}`, width : '10.625%'}}>{obj['pages']["fund_cumulative_performance_Début d'année"]}</td> : 
                                <td style={{color : `${green}`, width : '10.625%'}} >{obj['pages']["fund_cumulative_performance_Début d'année"]}</td>}
                            
                        </tr>
                        )
                        
                    }

                })}

                    </tbody>
                    
                </table>
                </div>
                <div className=" frame-text mt-4">
                    
                    <div className="sub-title">Classement</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                    <table className="table-data mt-2">
                        <thead>
                            <tr>
                                <td></td>
                                <td>{new Date().getFullYear()-7}</td>
                                <td>{new Date().getFullYear()-6}</td>
                                <td>{new Date().getFullYear()-5}</td>
                                <td>{new Date().getFullYear()-4}</td>
                                <td>{new Date().getFullYear()-3}</td>
                                <td>{new Date().getFullYear()-2}</td>
                                <td>{new Date().getFullYear()-1}</td>
                                <td>{new Date().getFullYear()}</td>

                            </tr>
                        </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        //rank
                        const rank7 = obj['pages'][`${new Date().getFullYear()-7}_rank`];
                        const rank6 = obj['pages'][`${new Date().getFullYear()-6}_rank`];
                        const rank5 = obj['pages'][`${new Date().getFullYear()-5}_rank`];
                        const rank4 = obj['pages'][`${new Date().getFullYear()-4}_rank`];
                        const rank3 = obj['pages'][`${new Date().getFullYear()-3}_rank`];
                        const rank2 = obj['pages'][`${new Date().getFullYear()-2}_rank`];
                        const rank1 = obj['pages'][`${new Date().getFullYear()-1}_rank`];
                        const rankCurrent = obj['pages']["current_rank"];

                        let color7 = green
                        if (parseInt(rank7) > 75) {
                            color7 = red
                        } else if (parseInt(rank7) > 50) {
                            color7 = orange
                        } else if ( parseInt(rank7) > 25) {
                            color7 =  yellow
                        }

                        let color6 = green
                        if (parseInt(rank6) > 75) {
                            color6 = red
                        } else if (parseInt(rank6) > 50) {
                            color6 = orange
                        } else if ( parseInt(rank6) > 25) {
                            color6 =  yellow
                        }

                        let color5 = green
                        if (parseInt(rank5) > 75) {
                            color5 = red
                        } else if (parseInt(rank5) > 50) {
                            color5 = orange
                        } else if ( parseInt(rank5) > 25) {
                            color5 =  yellow
                        }
                        
                        let color4 = green
                        if (parseInt(rank4) > 75) {
                            color4 = red
                        } else if (parseInt(rank4) > 50) {
                            color4 = orange
                        } else if ( parseInt(rank4) > 25) {
                            color4 =  yellow
                        }

                        let color3 = green
                        if (parseInt(rank3) > 75) {
                            color3 = red
                        } else if (parseInt(rank3) > 50) {
                            color3 = orange
                        } else if ( parseInt(rank3) > 25) {
                            color3 =  yellow
                        }
                        
                        let color2 = green
                        if (parseInt(rank2) > 75) {
                            color2 = red
                        } else if (parseInt(rank2) > 50) {
                            color2 = orange
                        } else if ( parseInt(rank2) > 25) {
                            color2 =  yellow
                        }
                        
                        let color1 = green
                        if (parseInt(rank1) > 75) {
                            color1 = red
                        } else if (parseInt(rank1) > 50) {
                            color1 = orange
                        } else if ( parseInt(rank1) > 25) {
                            color1 =  yellow
                        }

                        let colorCurrent = green
                        if (parseInt(rankCurrent) > 75) {
                            colorCurrent = red
                        } else if (parseInt(rankCurrent) > 50) {
                            colorCurrent = orange
                        } else if ( parseInt(rankCurrent) > 25) {
                            colorCurrent =  yellow
                        }
                        
                        return (

                            

                        <tr key={`ranking${i}`}>
                            <td className="first-col">{obj['infos']['LegalName']}</td>
                            
                            <td style={{color :`${color7}`, width : '10.625%'}} >{rank7}</td>
                            <td style={{color :`${color6}`, width : '10.625%'}} >{rank6}</td>
                            <td style={{color :`${color5}`, width : '10.625%'}} >{rank5}</td>
                            <td style={{color :`${color4}`, width : '10.625%'}} >{rank4}</td>
                            <td style={{color :`${color3}`, width : '10.625%'}} >{rank3}</td>
                            <td style={{color :`${color2}`, width : '10.625%'}} >{rank2}</td>
                            <td style={{color :`${color1}`, width : '10.625%'}} >{rank1}</td>
                            <td style={{color :`${colorCurrent}`, width : '10.625%'}} >{rankCurrent}</td>
                            
                        </tr>
                        )
                        
                    }

                })}

                    </tbody>
                    
                </table>
            </div>
            
            <h2 className="mt-4">Frais</h2>
            <div className=" frame-text">
                
                <div className="sub-title">Frais</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                <table className="table-data mt-2">
                    <thead>
                        <tr>
                            <td></td>
                            <td>Frais de souscription maximum</td>
                            <td>Frais de rachat maximum</td>
                            <td>Frais de gestion annuels maximum</td>
                            <td>Frais courants</td>
                            <td>Frais de conversion</td>

                        </tr>
                    </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        return (
                        <tr key={`fees${i}`}>
                            <td className="first-col">{obj['infos']['LegalName']}</td>
                            <td style={{width : '17%'}}>{obj['pages']['Frais de souscription max']}</td>
                            <td style={{width : '17%'}}>{obj['pages']['Frais de rachat max.']}</td>
                            <td style={{width : '17%'}}>{obj['pages']['Frais de gestion annuels maximum']}</td>
                            <td style={{width : '17%'}}>{obj['pages']['Frais courants']}</td>
                            <td style={{width : '17%'}}>{obj['pages']['Frais de conversion']}</td>

                        </tr>
                        )
                        
                    }

                })}

                    </tbody>
                    
                </table>
            </div>
            <h2 className="mt-4">Style</h2>
            {portInfos.reduce((n, {numberOfEquityHolding}) => n + numberOfEquityHolding, 0) > 0 ?
            <div className=" frame-text">
                
                <div className="sub-title">Style actions</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                <table className="table-data mt-2">
                    <thead>
                        <tr>
                            <td></td>
                            <td>Rendement des bénéfices</td>
                            <td>Rendement de la valeur comptable</td>
                            <td>Rendement du chiffre d'affaires</td>
                            <td>Rendement des cash flow</td>
                            <td>Taux du dividende</td>
                            <td>Croissance des bénéfices 5 ans</td>
                            <td>Croissance des bénéfices</td>
                            <td>Croissance de la valeur comptable</td>
                            <td>Croissance du chiffre d'affaires</td>
                            <td>Croissance des cash flow</td>
                        </tr>
                    </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        if (obj['marketCap']['assetType'] === "EQUITY" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            let prospectiveEarningsYield = null
                            let prospectiveEarningsYieldColor = green
                            if (obj['stockStyle']["fund"]["prospectiveEarningsYield"] !== null) {
                                prospectiveEarningsYield = obj['stockStyle']["fund"]["prospectiveEarningsYield"]
                                if (prospectiveEarningsYield < 0) {
                                    prospectiveEarningsYieldColor = red
                                }
                            }
                            let prospectiveBookValueYield = null
                            let prospectiveBookValueYieldColor = green
                            if (obj['stockStyle']["fund"]["prospectiveBookValueYield"] !== null) {
                                prospectiveBookValueYield = obj['stockStyle']["fund"]["prospectiveBookValueYield"]
                                if (prospectiveBookValueYield < 0) {
                                    prospectiveBookValueYieldColor = red
                                }
                            }
                            let prospectiveRevenueYield = null
                            let prospectiveRevenueYieldColor = green
                            if (obj['stockStyle']["fund"]["prospectiveRevenueYield"] !== null) {
                                prospectiveRevenueYield = obj['stockStyle']["fund"]["prospectiveRevenueYield"]
                                if (prospectiveRevenueYield < 0) {
                                    prospectiveRevenueYieldColor = red
                                }
                            }
                            let prospectiveCashFlowYield = null
                            let prospectiveCashFlowYieldColor = green
                            if (obj['stockStyle']["fund"]["prospectiveCashFlowYield"] !== null) {
                                prospectiveCashFlowYield = obj['stockStyle']["fund"]["prospectiveCashFlowYield"]
                                if (prospectiveCashFlowYield < 0) {
                                    prospectiveCashFlowYieldColor = red
                                }
                            }
                            let prospectiveDividendYield = null
                            let prospectiveDividendYieldColor = green
                            if (obj['stockStyle']["fund"]["prospectiveDividendYield"] !== null) {
                                prospectiveDividendYield = obj['stockStyle']["fund"]["prospectiveDividendYield"]
                                if (prospectiveDividendYield < 0) {
                                    prospectiveDividendYieldColor = red
                                }
                            }
                            let forecasted5YearEarningsGrowth = null
                            let forecasted5YearEarningsGrowthColor = green
                            if (obj['stockStyle']["fund"]["forecasted5YearEarningsGrowth"] !== null) {
                                forecasted5YearEarningsGrowth = obj['stockStyle']["fund"]["forecasted5YearEarningsGrowth"]
                                if (forecasted5YearEarningsGrowth < 0) {
                                    forecasted5YearEarningsGrowthColor = red
                                }
                            }
                            let forecastedEarningsGrowth = null
                            let forecastedEarningsGrowthColor = green
                            if (obj['stockStyle']["fund"]["forecastedEarningsGrowth"] !== null) {
                                forecastedEarningsGrowth = obj['stockStyle']["fund"]["forecastedEarningsGrowth"]
                                if (forecastedEarningsGrowth < 0) {
                                    forecastedEarningsGrowthColor = red
                                }
                            }

                            let forecastedBookValueGrowth = null
                            let forecastedBookValueGrowthColor = green
                            if (obj['stockStyle']["fund"]["forecastedBookValueGrowth"] !== null) {
                                forecastedBookValueGrowth = obj['stockStyle']["fund"]["forecastedBookValueGrowth"]
                                if (forecastedBookValueGrowth < 0) {
                                    forecastedBookValueGrowthColor = red
                                }
                            }

                            let forecastedRevenueGrowth = null
                            let forecastedRevenueGrowthColor = green
                            if (obj['stockStyle']["fund"]["forecastedRevenueGrowth"] !== null) {
                                forecastedRevenueGrowth = obj['stockStyle']["fund"]["forecastedRevenueGrowth"]
                                if (forecastedRevenueGrowth < 0) {
                                    forecastedRevenueGrowthColor = red
                                }
                            }

                            let forecastedCashFlowGrowth = null
                            let forecastedCashFlowGrowthColor = green
                            if (obj['stockStyle']["fund"]["forecastedCashFlowGrowth"] !== null) {
                                forecastedCashFlowGrowth = obj['stockStyle']["fund"]["forecastedCashFlowGrowth"]
                                if (forecastedCashFlowGrowth < 0) {
                                    forecastedCashFlowGrowthColor = red
                                }
                            }
                            
                        
                        return (
                        <tr key={`stockstyle${i}`}>
                            <td className="first-col">{obj['infos']['LegalName']}</td>
                            
                            {(prospectiveEarningsYield !== null ) ? 
                                <td style={{color : `${prospectiveEarningsYieldColor}`, width : '8.5%'}}>{prospectiveEarningsYield.toFixed(2)}</td> : 
                                null}

                            {(prospectiveBookValueYield !== null ) ? 
                                                            <td style={{color : `${prospectiveBookValueYieldColor}`, width : '8.5%'}}>{prospectiveBookValueYield.toFixed(2)}</td> : 
                                                            null}

                            {(prospectiveRevenueYield !== null ) ? 
                                                            <td style={{color : `${prospectiveRevenueYieldColor}`, width : '8.5%'}}>{prospectiveRevenueYield.toFixed(2)}</td> : 
                                                            null}
                                                        
                            {(prospectiveCashFlowYield !== null ) ? 
                                <td style={{color : `${prospectiveCashFlowYieldColor}`, width : '8.5%'}}>{prospectiveCashFlowYield.toFixed(2)}</td> : 
                                null}

                            {(prospectiveDividendYield !== null ) ? 
                                                            <td style={{color : `${prospectiveDividendYieldColor}`, width : '8.5%'}}>{prospectiveDividendYield.toFixed(2)}</td> : 
                                                            null}
                            {(forecasted5YearEarningsGrowth !== null ) ? 
                                <td style={{color : `${forecasted5YearEarningsGrowthColor}`, width : '8.5%'}}>{forecasted5YearEarningsGrowth.toFixed(2)}</td> : 
                                null}

                            {(forecastedEarningsGrowth !== null ) ? 
                                                            <td style={{color : `${forecastedEarningsGrowthColor}`, width : '8.5%'}}>{forecastedEarningsGrowth.toFixed(2)}</td> : 
                                                            null}

                            {(forecastedBookValueGrowth !== null ) ? 
                                                            <td style={{color : `${forecastedBookValueGrowthColor}`, width : '8.5%'}}>{forecastedBookValueGrowth.toFixed(2)}</td> : 
                                                            null}
                            {(forecastedRevenueGrowth !== null ) ? 
                                <td style={{color : `${forecastedRevenueGrowthColor}`, width : '8.5%'}}>{forecastedRevenueGrowth.toFixed(2)}</td> : 
                                null}

                            {(forecastedCashFlowGrowth !== null ) ? 
                                <td style={{color : `${forecastedCashFlowGrowthColor}`, width : '8.5%'}}>{forecastedCashFlowGrowth.toFixed(2)}</td> : 
                                null}


                            
                        </tr>
                        )}
                        
                    }

                })}

                    </tbody>
                </table>
            </div> : <div></div>}
            
            {portInfos.reduce((n, {numberOfBondHolding}) => n + numberOfBondHolding, 0) > 0 ?
            <div className=" frame-text mt-4">
                
                <div className="sub-title">Style obligations</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                <table className="table-data mt-2">
                    <thead>
                        <tr>
                            <td></td>
                            <td>Duration</td>
                            <td>Duration modifiée</td>
                            <td>Maturité moyenne</td>
                            <td>Qualité du crédit</td>
                            <td>Notation moyenne</td>
                            <td>Coupon moyen</td>
                            <td>Prix moyen</td>
                            <td>Rendement à maturité</td>
                        </tr>
                    </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        if (obj['marketCap']['assetType'] === "FIXEDINCOME" || obj['marketCap']['assetType'] === 'ALLOCATION') {

                        
                        return (
                        <tr key={`bondstyle${i}`}>
                            <td className="first-col" >{obj['infos']['LegalName']}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["avgEffectiveDuration"] !== null ? obj['bondStyle']["fund"]["avgEffectiveDuration"].toFixed(2) : null}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["modifiedDuration"] !== null ? obj['bondStyle']["fund"]["modifiedDuration"].toFixed(2) : null}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["avgEffectiveMaturity"] !== null ?obj['bondStyle']["fund"]["avgEffectiveMaturity"].toFixed(2) : null }</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["avgCreditQualityName"]}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["calculatedAverageCreditRating"]}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["avgCoupon"] !== null ? obj['bondStyle']["fund"]["avgCoupon"].toFixed(2) : null}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["avgPrice"] !== null ? obj['bondStyle']["fund"]["avgPrice"].toFixed(2) : null}</td>
                            <td style={{width : '10.625%'}}>{obj['bondStyle']["fund"]["yieldToMaturity"] !== null ?  obj['bondStyle']["fund"]["yieldToMaturity"].toFixed(2) : null}</td>
                            
                        </tr>
                        )}
                        
                    }

                })}
                    </tbody>
                </table>
            </div>: <div></div>}
            </div> 

            <div>
                {portInfos.reduce((n, {numberOfEquityHolding}) => n + numberOfEquityHolding, 0) > 0 ? 
                <div className="mt-4">
                    <h2>Positions actions</h2>
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        if ("equityHoldingPage" in obj['positions']) {
                        if (obj['positions']["equityHoldingPage"]["numberOfAllHolding"] !==0) {

                            

                            return (
                                <div  className = 'frame-text' style={{display : "inline-grid", width : `${90/portfolios.length}%`}}>
                                    
                                    <div className="sub-title">{obj['infos']['LegalName']}</div>
                                        <div align ="center">
                                            <div className = 'hline mt-2'></div>
                                        </div>
                                    <table className="scroll mt-2" style={{width:'100%', textAlign:'center'}}>
                                        <thead>
                                            <tr>
                                                <td>Nom</td>
                                                <td>Poids</td>
                                                <td>Secteur</td>
                                            </tr>
                                        </thead>
                                        <tbody className="specific-bar">
                                        {obj['positions']["equityHoldingPage"]["holdingList"].map((position,i)=> {
                                        return (
                                        <tr key={`positionsEquity${i}`}>
                                            <td>{position['securityName']}</td>
                                            <td>{position['weighting'].toFixed(2)}</td>
                                            <td>{position['sector']}</td>
                                        </tr>)
                                        })
                                        }
                                        </tbody>
                                        <tfoot>
                                            <tr> 
                                                <td>Total</td> 
                                                <td>{obj['positions']["equityHoldingPage"]["holdingList"].reduce((n, {weighting}) => n + weighting, 0).toFixed(2)}</td> 
                                                <td></td>
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div>

                            )}}


                     }
                    })}
                </div>: <div></div>} 
                

            </div>
            <div>
            {portInfos.reduce((n, {numberOfBondHolding}) => n + numberOfBondHolding, 0) > 0 ? 
            <div className="mt-4">
                <h2>Positions obligations</h2>
                {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        if ("boldHoldingPage" in obj['positions']) {
                        if (obj['positions']["boldHoldingPage"]["numberOfAllHolding"] !==0) {
                            
                            return (
                                <div  className = 'frame-text' style={{display : "inline-grid", width : `${90/portfolios.length}%`}}>
                                    
                                <div className="sub-title">{obj['infos']['LegalName']}</div>
                                    <div align ="center">
                                        <div className = 'hline mt-2'></div>
                                    </div>
                                    <table className="scroll mt-2" style={{width:'100%', textAlign:'center'}}>
                                        <thead>
                                            <tr>
                                                <td>Nom</td>
                                                <td>Poids</td>
                                                <td>Description</td>
                                            </tr>
                                        </thead>
                                        <tbody className="specific-bar">
                                        {obj['positions']["boldHoldingPage"]["holdingList"].map((position,i)=> {
                                        return (
                                        <tr key={`positionsBond${i}`}>
                                            <td>{position['securityName']}</td>
                                            <td>{position['weighting'].toFixed(2)}</td>
                                            <td>{position['secondarySectorName']}</td>
                                        </tr>)
                                        })
                                        }
                                        </tbody>
                                        <tfoot>
                                            <tr> 
                                                <td>Total</td> 
                                                <td>{obj['positions']["boldHoldingPage"]["holdingList"].reduce((n, {weighting}) => n + weighting, 0).toFixed(2)}</td> 
                                                <td></td>
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div>

                                )
                    }}


                     } 
                    })}
            </div>
            : <div></div>} 
            
                

            </div>
            <div>
            {portInfos.reduce((n, {numberOfOtherHolding}) => n + numberOfOtherHolding, 0) > 0 ?
            <div className="mt-4">
                <h2>Autres positions</h2>
                {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        if ("otherHoldingPage" in obj['positions']) {
                        if (obj['positions']["otherHoldingPage"]["numberOfAllHolding"] !==0) {
                            
                            return (
                                <div  className = 'frame-text' style={{display : "inline-grid", width : `${90/portfolios.length}%`}}>
                                    
                                <div className="sub-title">{obj['infos']['LegalName']}</div>
                                    <div align ="center">
                                        <div className = 'hline mt-2'></div>
                                    </div>
                                    <table className="scroll mt-2" style={{width:'100%', textAlign:'center'}}>
                                        <thead>
                                            <tr>
                                                <td>Nom</td>
                                                <td>Poids</td>
                                                <td>Description</td>
                                            </tr>
                                        </thead>
                                        <tbody className="specific-bar">
                                        {obj['positions']["otherHoldingPage"]["holdingList"].map((position,i)=> {
                                        return (
                                        <tr key={`positionsOther${i}`}>
                                            <td>{position['securityName']}</td>
                                            <td>{position['weighting'].toFixed(2)}</td>
                                            <td>{position['secondarySectorName'] === null ? position['morningstarCategory'] : position['secondarySectorName'] }</td>
                                        </tr>)
                                        })
                                        }
                                        </tbody>
                                        <tfoot>
                                            <tr> 
                                                <td>Total</td> 
                                                <td>{obj['positions']["otherHoldingPage"]["holdingList"].reduce((n, {weighting}) => n + weighting, 0).toFixed(2)}</td> 
                                                <td></td>
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div>

                                )
                    }}


                     } 
                    })}
                </div>
                :<div></div>}

            </div>

            <div className="mt-4">
            {portInfos.reduce((n, {numberOfEquityHolding}) => n + numberOfEquityHolding, 0) > 0 ?
            <div style = {{display : "inline-grid"}}>
                <h2>Capitalisation boursière</h2>
                {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "EQUITY" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            marketCap[0][obj['infos']['LegalName']] = obj['marketCap']['fund']['giant'];
                            marketCap[1][obj['infos']['LegalName']] = obj['marketCap']['fund']['large'];
                            marketCap[2][obj['infos']['LegalName']] = obj['marketCap']['fund']['medium'];
                            marketCap[3][obj['infos']['LegalName']] = obj['marketCap']['fund']['small'];
                            marketCap[4][obj['infos']['LegalName']] = obj['marketCap']['fund']['micro'];
                            

                        }


                    }
                    })}

                <div>
                <BarChart
                    width={500}
                    height={500}
                    data={marketCap}
                    margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" stroke="#F5F4FF" />
                    <YAxis/>
                    <Tooltip />
                    <Legend />
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "EQUITY" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            return (
                                <Bar dataKey={obj['infos']['LegalName']} fill={graphColor[i]} />   
                            )                           

                        }


                    }
                    })}
                         
                </BarChart>

                </div>


            </div> : <div></div>}
            {portInfos.reduce((n, {numberOfEquityHolding}) => n + numberOfEquityHolding, 0) > 0 ?
            <div style = {{display : "inline-grid"}}>
                <h2>Répartition par secteur</h2>
                {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "EQUITY" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            sectorData[0][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['consumerCyclical'];
                            sectorData[1][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['consumerDefensive'];
                            sectorData[2][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['energy'];
                            sectorData[3][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['financialServices'];
                            sectorData[4][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['realEstate'];
                            sectorData[5][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['industrials'];
                            sectorData[6][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['basicMaterials'];
                            sectorData[7][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['healthcare'];
                            
                            sectorData[8][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['technology'];
                            sectorData[9][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['communicationServices'];
                            sectorData[10][obj['infos']['LegalName']] = obj['sector']['EQUITY']["fundPortfolio"]['utilities'];
                            

                        }


                    }
                    })}

                <div>
                <BarChart
                    width={500}
                    height={500}
                    data={sectorData}
                    margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" stroke="#F5F4FF" angle={-80} textAnchor="end" interval = {0} height={180}  />
                    <YAxis/>
                    <Tooltip />
                    <Legend />
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "EQUITY" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            return (
                                <Bar dataKey={obj['infos']['LegalName']} fill={graphColor[i]} />   
                            )                           

                        }


                    }
                    })}
                         
                </BarChart>

                </div>


            </div> : <div></div>}
            {portInfos.reduce((n, {numberOfBondHolding}) => n + numberOfBondHolding, 0) > 0 ?
            <div style = {{display : "inline-grid"}}>
                <h2>Types d'obligations</h2>
                {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "FIXEDINCOME" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            bondsType[0][obj['infos']['LegalName']] = obj['sector']['FIXEDINCOME']["fundPortfolio"]['government'];
                            bondsType[1][obj['infos']['LegalName']] = obj['sector']['FIXEDINCOME']["fundPortfolio"]['municipal'];
                            bondsType[2][obj['infos']['LegalName']] = obj['sector']['FIXEDINCOME']["fundPortfolio"]['corporate'];
                            bondsType[3][obj['infos']['LegalName']] = obj['sector']['FIXEDINCOME']["fundPortfolio"]['securitized'];
                            bondsType[4][obj['infos']['LegalName']] = obj['sector']['FIXEDINCOME']["fundPortfolio"]['cashAndEquivalents'];
                            bondsType[5][obj['infos']['LegalName']] = obj['sector']['FIXEDINCOME']["fundPortfolio"]['derivative'];

                        }


                    }
                    })}

                <div>
                <BarChart
                    width={500}
                    height={500}
                    data={bondsType}
                    margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" stroke="#F5F4FF" angle={-45} textAnchor="end" interval = {0} height={120}/>
                    <YAxis/>
                    <Tooltip />
                    <Legend />
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "FIXEDINCOME" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            return (
                                <Bar dataKey={obj['infos']['LegalName']} fill={graphColor[i]} />   
                            )                           

                        }


                    }
                    })}
                         
                </BarChart>

                </div>


            </div> : <div></div>}
            {portInfos.reduce((n, {numberOfBondHolding}) => n + numberOfBondHolding, 0) > 0 ?
            <div style = {{display : "inline-grid"}}>
                <h2>Notation des obligations</h2>
                {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "FIXEDINCOME" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            bondsQuality[0][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityAAA"];
                            bondsQuality[1][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityAA"];
                            bondsQuality[2][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityA"];
                            bondsQuality[3][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityBBB"];
                            bondsQuality[4][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityBB"];
                            bondsQuality[5][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityB"];
                            bondsQuality[6][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityBelowB"];
                            bondsQuality[7][obj['infos']['LegalName']] = obj['creditQuality']['fund']["creditQualityNotRated"];


                        }


                    }
                    })}

                <div>
                <BarChart
                    width={500}
                    height={500}
                    data={bondsQuality}
                    margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" stroke="#F5F4FF" angle={-45} textAnchor="end" interval = {0} height={80}/>
                    <YAxis/>
                    <Tooltip />
                    <Legend />
                    {portInfos.map((obj, i) => {
                    if (obj // 👈 null and undefined check
                    && Object.keys(obj).length === 0
                    && Object.getPrototypeOf(obj) === Object.prototype){
                        //pass
                    } else {
                        
                        if (obj['marketCap']['assetType'] === "FIXEDINCOME" || obj['marketCap']['assetType'] === 'ALLOCATION') {
                            return (
                                <Bar dataKey={obj['infos']['LegalName']} fill={graphColor[i]} />   
                            )                           

                        }


                    }
                    })}
                         
                </BarChart>

                </div>


            </div> : <div></div>}
            </div>

            <div className = "mt-4">
            <h2>Carbone</h2>
            <div className=" frame-text">
                <div className="sub-title">Données carbone</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                    <table className="table-data mt-2">
                    <thead>
                        <tr>
                            <td></td>
                            <td>Score risque carbone</td>
                            <td>% portefeuille couvert</td>
                            <td>Faible teneur en carbone</td>
                            <td>% Impliqué dans des combustibles fossiles</td>

    
                        </tr>
                    </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const isLowCarbon = obj['carbonMetrics']['isLowCarbon']
                            let TFCarbon = '-'
                            let colorCarbon = black

                        if (isLowCarbon== "true") {
                            TFCarbon = 'Oui'
                            colorCarbon = green
                        } else if (isLowCarbon== "false") {
                            TFCarbon = 'Non'
                            colorCarbon = red
                        } 

                            return (
                            <tr key={`carbon${i}`} style={{height : '4rem'}}>
                                <td className="first-col">{obj['infos']['LegalName']}</td>
                                <td style={{width : '21.25%'}}>{obj['carbonMetrics']['carbonRiskScore']}</td>
                                <td style={{width : '21.25%'}}>{ obj['carbonMetrics']['carbonRiskScore'] == null ? null : obj['carbonMetrics']['carbonPortfolioCoveragePct']}</td>
                                <td style={{color :`${colorCarbon}`, width : '21.25%'}}>{TFCarbon}</td>
                                <td style={{width : '21.25%'}}>{obj['carbonMetrics']['fossilFuelInvolvementPct']}</td>
                                
                            </tr>)}
                        })}
                        

                    </tbody>
                    </table>
            </div>
            </div>
            <div className = "mt-4">
                <h2>Durabilité</h2>
                <div className=" frame-text">
                <div className="sub-title">Score de durabilité</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                    <table className="table-data mt-2">
                    <thead>
                        <tr>
                            <td></td>
                            <td>Score entreprises</td>
                            <td>Contribution entreprises</td>
                            <td>Score souverains</td>
                            <td>Contribution souverains</td>

    
                        </tr>
                    </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const CorporateSustainabilityScore = obj['esgData']['esgData']['fundSustainabilityScore']
                            const Sovereignsustainabilityscore = obj['esgData']['esgData']['portfolioSovereignsustainabilityscore']
                            let colorCorpo = green

                        if (parseInt(CorporateSustainabilityScore ) > 30) {
                            colorCorpo = red
                        } else if (parseInt(CorporateSustainabilityScore) > 20) {
                            colorCorpo = orange
                        } else if ( parseInt(CorporateSustainabilityScore) > 10) {
                            colorCorpo =  yellow
                        }

                        let colorSov = green
                        if (parseInt(Sovereignsustainabilityscore ) > 30) {
                            colorSov = red
                        } else if (parseInt(Sovereignsustainabilityscore) > 20) {
                            colorSov = orange
                        } else if ( parseInt(Sovereignsustainabilityscore) > 10) {
                            colorSov =  yellow
                        }

                            return (
                            <tr key={`scoreSustanabilityCorp${i}`} style={{height : '4rem'}}>
                                <td className="first-col">{obj['infos']['LegalName']}</td>
                                <td style={{color :`${colorCorpo}`, width : '21.25%'}}>{obj['esgData']['esgData']['fundSustainabilityScore'] !== null ? obj['esgData']['esgData']['fundSustainabilityScore'].toFixed(2) : null} </td>
                                <td style={{ width : '21.25%'}}>{obj['esgData']['esgData']['sustainabilityRatingCorporateContributionPercent'] !== null ? `${obj['esgData']['esgData']['sustainabilityRatingCorporateContributionPercent'].toFixed(2)} %` : null } </td>
                                <td style={{color :`${colorSov}`, width : '21.25%'}}>{obj['esgData']['esgData']['portfolioSovereignsustainabilityscore'] !== null ? obj['esgData']['esgData']['portfolioSovereignsustainabilityscore'].toFixed(2) : null} </td>
                                <td style={{ width : '21.25%'}}>{obj['esgData']['esgData']['sustainabilityRatingSovereignContributionPercent'] !== null ? `${obj['esgData']['esgData']['sustainabilityRatingSovereignContributionPercent'].toFixed(2)} %`  : null } </td>
                                
                            </tr>)}
                        })}
                        

                    </tbody>
                    </table>
                    
                </div>

                <div className=" frame-text mt-4">
                <div className="sub-title">Répartition ESG*</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                    <table className="table-data mt-2">
                    <thead>
                        <tr>
                            <td></td>
                            <td>Environnement</td>
                            <td>Social</td>
                            <td>Gouvernance</td>
                            <td>Non-alloué</td>
                            
    
                        </tr>
                    </thead>
                    <tbody>
                    {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return (
                            <tr key={`scoreSustanabilitySov${i}`} style={{height : '4rem'}}>
                                <td className="first-col">{obj['infos']['LegalName']}</td>
                                <td>{obj['esgData']['esgScoreCalculation']['environmentalScore'] !== null ? obj['esgData']['esgScoreCalculation']['environmentalScore'].toFixed(2) : null} </td>
                                <td>{obj['esgData']['esgScoreCalculation']['socialScore'] !== null ? obj['esgData']['esgScoreCalculation']['socialScore'].toFixed(2) : null } </td>
                                <td>{obj['esgData']['esgScoreCalculation']['governanceScore'] !== null ? obj['esgData']['esgScoreCalculation']['governanceScore'].toFixed(2) : null } </td>
                                <td>{obj['esgData']['esgScoreCalculation']['portfolioUnallocatedEsgRiskScore'] !== null ? obj['esgData']['esgScoreCalculation']['portfolioUnallocatedEsgRiskScore'].toFixed(2) : null } </td>
                                
                            </tr>)}
                        })}
                        

                    </tbody>
                    <tfoot>
                    <tr> 
                        <td td colSpan={4} style = {{textAlign: "left"}}>*(scores plus faibles = risque plus faible)</td> 

                    </tr>
                    </tfoot>
                    </table>
                    
                </div>

                <div className="frame-text mt-4">
                <div className="sub-title">Engagements</div>
                <div align ="center">
                        <div className = 'hline mt-2'></div>
                </div>
                <table className="table-exclude mt-2">
                <thead>
                <tr>
                    <td style ={{width : '30%'}}></td>
                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return (
                                       
                                <td style={{width :`${70/portfolios.length}%`}}>{obj['infos']['LegalName']} </td>

                            )}
                            
                        })}
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                                <td >Critères ESG inclus dans la gestion</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const eSGIncorporation = obj['esgData']['sustainabilityIntentionality']['eSGIncorporation']
                            let TFeSGIncorporation = '-'
                            let TFeSGIncorporationColor = black
                            if (eSGIncorporation === true) {
                                TFeSGIncorporation = 'Oui'
                                TFeSGIncorporationColor = green
                            } else if (eSGIncorporation === false) {
                                TFeSGIncorporation = 'Non'
                                TFeSGIncorporationColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFeSGIncorporationColor}`}}>{TFeSGIncorporation} </td>

                            )}

                            
                        })}

                            </tr>

                            <tr>
                                <td >Engagement ESG</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const eSGEngagement = obj['esgData']['sustainabilityIntentionality']['eSGEngagement']
                            let TFeSGEngagement = '-'
                            let TFeSGEngagementColor = black
                            if (eSGEngagement === true) {
                                TFeSGEngagement = 'Oui'
                                TFeSGEngagementColor = green
                            } else if (eSGEngagement === false) {
                                TFeSGEngagement = 'Non'
                                TFeSGEngagementColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFeSGEngagementColor}`}}>{TFeSGEngagement} </td>

                            )}

                            
                        })}

                            </tr>
                        <tr>
                                <td>Engagement pour la parité Homme/Femme</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const genderDiversity = obj['esgData']['sustainabilityIntentionality']['genderDiversity']
                            let TFgenderDiversity = '-'
                            let TFgenderDiversityColor = black
                            if (genderDiversity === true) {
                                TFgenderDiversity = 'Oui'
                                TFgenderDiversityColor = green
                            } else if (genderDiversity === false) {
                                TFgenderDiversity = 'Non'
                                TFgenderDiversityColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFgenderDiversityColor}`}}>{TFgenderDiversity} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td >Engagement pour le développement de la communauté</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const communityDevelopment = obj['esgData']['sustainabilityIntentionality']['communityDevelopment']
                            let TFcommunityDevelopment = '-'
                            let TFcommunityDevelopmentColor = black
                            if (communityDevelopment === true) {
                                TFcommunityDevelopment = 'Oui'
                                TFcommunityDevelopmentColor = green
                            } else if (communityDevelopment === false) {
                                TFcommunityDevelopment = 'Non'
                                TFcommunityDevelopmentColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFcommunityDevelopmentColor}`}}>{TFcommunityDevelopment} </td>

                            )}

                            
                        })}

                            </tr>

                            <tr>
                                <td >Engagement dans la réduction des émissions CO2</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const lowCarbonFossilFuelFree = obj['esgData']['sustainabilityIntentionality']['lowCarbonFossilFuelFree']
                            let TFlowCarbonFossilFuelFree = '-'
                            let TFlowCarbonFossilFuelFreeColor = black
                            if (lowCarbonFossilFuelFree === true) {
                                TFlowCarbonFossilFuelFree = 'Oui'
                                TFlowCarbonFossilFuelFreeColor = green
                            } else if (lowCarbonFossilFuelFree === false) {
                                TFlowCarbonFossilFuelFree = 'Non'
                                TFlowCarbonFossilFuelFreeColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFlowCarbonFossilFuelFreeColor}`}}>{TFlowCarbonFossilFuelFree} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td >Engagement dans l'énergie renouvelable</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const renewableEnergy = obj['esgData']['sustainabilityIntentionality']['renewableEnergy']
                            let TFrenewableEnergy = '-'
                            let TFrenewableEnergyColor = black
                            if (renewableEnergy === true) {
                                TFrenewableEnergy = 'Oui'
                                TFrenewableEnergyColor = green
                            } else if (renewableEnergy === false) {
                                TFrenewableEnergy = 'Non'
                                TFrenewableEnergyColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFrenewableEnergyColor }`}} >{TFrenewableEnergy} </td>

                            )}

                            
                        })}

                            </tr>

                            <tr>
                                <td >Investissement focalisé dans l'eau</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const waterFocused = obj['esgData']['sustainabilityIntentionality']['waterFocused']
                            let TFwaterFocused = '-'
                            let TFwaterFocusedColor = black
                            if (waterFocused === true) {
                                TFwaterFocused = 'Oui'
                                TFwaterFocusedColor = green
                            } else if (waterFocused === false) {
                                TFwaterFocused = 'Non'
                                TFwaterFocusedColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFwaterFocusedColor}`}}>{TFwaterFocused} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td >Investissement global dans le secteur environnemental</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const generalEnvironmentalSector = obj['esgData']['sustainabilityIntentionality']['generalEnvironmentalSector']
                            let TFgeneralEnvironmentalSector = '-'
                            let TFgeneralEnvironmentalSectorColor = black
                            if (generalEnvironmentalSector === true) {
                                TFgeneralEnvironmentalSector = 'Oui'
                                TFgeneralEnvironmentalSectorColor = green
                            } else if (generalEnvironmentalSector === false) {
                                TFgeneralEnvironmentalSector = 'Non'
                                TFgeneralEnvironmentalSectorColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFgeneralEnvironmentalSectorColor}`}}>{TFgeneralEnvironmentalSector} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td>Fonds à investissement durable</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const sustainableInvestmentOverall = obj['esgData']['sustainabilityIntentionality']['sustainableInvestmentOverall']
                            let TFsustainableInvestmentOverall = '-'
                            let TFsustainableInvestmentOverallColor = black
                            if (sustainableInvestmentOverall === true) {
                                TFsustainableInvestmentOverall = 'Oui'
                                TFsustainableInvestmentOverallColor = green
                            } else if (sustainableInvestmentOverall === false) {
                                TFsustainableInvestmentOverall = 'Non'
                                TFsustainableInvestmentOverallColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFsustainableInvestmentOverallColor}`}}>{TFsustainableInvestmentOverall} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td>Fonds à impact</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const impactFundOverall = obj['esgData']['sustainabilityIntentionality']['impactFundOverall']
                            let TFimpactFundOverall = '-'
                            let TFimpactFundOverallColor = black
                            if (impactFundOverall === true) {
                                TFimpactFundOverall = 'Oui'
                                TFimpactFundOverallColor = green
                            } else if (impactFundOverall === false) {
                                TFimpactFundOverall = 'Non'
                                TFimpactFundOverallColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFimpactFundOverallColor}`}}>{TFimpactFundOverall} </td>

                            )}

                            
                        })}

                            </tr>

                        </tbody>

                        </table>
                </div>
                
                
                <div className=" frame-text mt-4">
                <div className="sub-title">Politique d'exclusion</div>
                    <div align ="center">
                        <div className = 'hline mt-2'></div>
                    </div>
                <table className="table-exclude mt-2">
                <thead>
                <tr>
                    <td style ={{width : '30%'}}></td>
                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            return (
                                       
                                <td style={{width :`${70/portfolios.length}%`}}>{obj['infos']['LegalName']} </td>

                            )}
                            
                        })}
                        </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td >Exclusion des Cellules souches d'avortement</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesAbortionStemCells = obj['esgData']['sustainabilityIntentionality']['excludesAbortionStemCells']
                            let TFExcludesAbortionStemCells = '-'
                            let TFExcludesAbortionStemCellsColor = black
                            if (excludesAbortionStemCells === true) {
                                TFExcludesAbortionStemCells = 'Oui'
                                TFExcludesAbortionStemCellsColor = green
                            } else if (excludesAbortionStemCells === false) {
                                TFExcludesAbortionStemCells = 'Non'
                                TFExcludesAbortionStemCellsColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesAbortionStemCellsColor}`}}>{TFExcludesAbortionStemCells} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion du divertissement pour adulte</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesAdultEntertainment = obj['esgData']['sustainabilityIntentionality']['excludesAdultEntertainment']
                            let TFExcludesAdultEntertainment = '-'
                            let TFExcludesAdultEntertainmentColor = black
                            if (excludesAdultEntertainment === true) {
                                TFExcludesAdultEntertainment= 'Oui'
                                TFExcludesAdultEntertainmentColor = green
                            } else if (excludesAdultEntertainment === false) {
                                TFExcludesAdultEntertainment = 'Non'
                                TFExcludesAdultEntertainmentColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesAdultEntertainmentColor}`}}>{TFExcludesAdultEntertainment} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion de l'alcool</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesAlcohol = obj['esgData']['sustainabilityIntentionality']['excludesAlcohol']
                            let TFExcludesAlcohol = '-'
                            let TFExcludesAlcoholColor = black
                            if (excludesAlcohol === true) {
                                TFExcludesAlcohol= 'Oui'
                                TFExcludesAlcoholColor = green
                            } else if (excludesAlcohol === false) {
                                TFExcludesAlcohol = 'Non'
                                TFExcludesAlcoholColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesAlcoholColor}`}}>{TFExcludesAlcohol} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion de test animal</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesAnimalTesting = obj['esgData']['sustainabilityIntentionality']['excludesAnimalTesting']
                            let TFExcludesAnimalTesting = '-'
                            let TFExcludesAnimalTestingColor = black
                            if (excludesAnimalTesting === true) {
                                TFExcludesAnimalTesting= 'Oui'
                                TFExcludesAnimalTestingColor = green
                            } else if (excludesAnimalTesting === false) {
                                TFExcludesAnimalTesting= 'Non'
                                TFExcludesAnimalTestingColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesAnimalTestingColor}`}}>{TFExcludesAnimalTesting} </td>

                            )}


                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des armes controversées</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesControversialWeapons = obj['esgData']['sustainabilityIntentionality']['excludesControversialWeapons']
                            let TFExcludesControversialWeapons = '-'
                            let TFExcludesControversialWeaponsColor = black
                            if (excludesControversialWeapons === true) {
                                TFExcludesControversialWeapons= 'Oui'
                                TFExcludesControversialWeaponsColor = green
                            } else if (excludesControversialWeapons === false) {
                                TFExcludesControversialWeapons= 'Non'
                                TFExcludesControversialWeaponsColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesControversialWeaponsColor}`}}>{TFExcludesControversialWeapons} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion de la fourrure</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesFurSpecialtyLeather = obj['esgData']['sustainabilityIntentionality']['excludesFurSpecialtyLeather']
                            let TFExcludesFurSpecialtyLeather = '-'
                            let TFExcludesFurSpecialtyLeatherColor = black
                            if (excludesFurSpecialtyLeather === true) {
                                TFExcludesFurSpecialtyLeather= 'Oui'
                                TFExcludesFurSpecialtyLeatherColor = green
                            } else if (excludesFurSpecialtyLeather === false) {
                                TFExcludesFurSpecialtyLeather= 'Non'
                                TFExcludesFurSpecialtyLeatherColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesFurSpecialtyLeatherColor}`}}>{TFExcludesFurSpecialtyLeather} </td>

                            )}

                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des jeux d'argent</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesGambling = obj['esgData']['sustainabilityIntentionality']['excludesGambling']
                            let TFExcludesGambling = '-'
                            let TFExcludesGamblingColor = black
                            if (excludesGambling === true) {
                                TFExcludesGambling= 'Oui'
                                TFExcludesGamblingColor = green
                            } else if (excludesGambling === false) {
                                TFExcludesGambling= 'Non'
                                TFExcludesGamblingColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesGamblingColor}`}}>{TFExcludesGambling} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des OGM</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesGMOs = obj['esgData']['sustainabilityIntentionality']['excludesGMOs']
                            let TFExcludesGMOs = '-'
                            let TFExcludesGMOsColor = black
                            if (excludesGMOs === true) {
                                TFExcludesGMOs= 'Oui'
                                TFExcludesGMOsColor = green
                            } else if (excludesGMOs === false) {
                                TFExcludesGMOs= 'Non'
                                TFExcludesGMOsColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesGMOsColor}`}}>{TFExcludesGMOs} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des contrats militaires</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesMilitaryContracting = obj['esgData']['sustainabilityIntentionality']['excludesMilitaryContracting']
                            let TFExcludesMilitaryContracting = '-'
                            let TFExcludesMilitaryContractingColor = black
                            if (excludesMilitaryContracting === true) {
                                TFExcludesMilitaryContracting= 'Oui'
                                TFExcludesMilitaryContractingColor = green
                            } else if (excludesMilitaryContracting === false) {
                                TFExcludesMilitaryContracting= 'Non'
                                TFExcludesMilitaryContractingColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesMilitaryContractingColor}`}}>{TFExcludesMilitaryContracting} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion du nucléaire</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesNuclear = obj['esgData']['sustainabilityIntentionality']['excludesNuclear']
                            let TFExcludesNuclear = '-'
                            let TFExcludesNuclearColor = black
                            if (excludesNuclear === true) {
                                TFExcludesNuclear= 'Oui'
                                TFExcludesNuclearColor = green
                            } else if (excludesNuclear === false) {
                                TFExcludesNuclear= 'Non'
                                TFExcludesNuclearColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesNuclearColor}`}}>{TFExcludesNuclear} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion de l'huile de Palme</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesPalmOil = obj['esgData']['sustainabilityIntentionality']['excludesPalmOil']
                            let TFExcludesPalmOil = '-'
                            let TFExcludesPalmOilColor = black
                            if (excludesPalmOil === true) {
                                TFExcludesPalmOil= 'Oui'
                                TFExcludesPalmOilColor = green
                            } else if (excludesPalmOil === false) {
                                TFExcludesPalmOil= 'Non'
                                TFExcludesPalmOilColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesPalmOilColor}`}} >{TFExcludesPalmOil} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des pesticides</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            const excludesPesticides = obj['esgData']['sustainabilityIntentionality']['excludesPesticides']
                            let TFExcludesPesticides = '-'
                            let TFExcludesPesticidesColor = black
                            if (excludesPesticides === true) {
                                TFExcludesPesticides= 'Oui'
                                TFExcludesPesticidesColor = green
                            } else if (excludesPesticides === false) {
                                TFExcludesPesticides= 'Non'
                                TFExcludesPesticidesColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesPesticidesColor}`}}>{TFExcludesPesticides} </td>

                            )}
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des petites armes</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesSmallArms = obj['esgData']['sustainabilityIntentionality']['excludesSmallArms']
                            let TFExcludesSmallArms = '-'
                            let TFExcludesSmallArmsColor = black
                            if (excludesSmallArms === true) {
                                TFExcludesSmallArms= 'Oui'
                                TFExcludesSmallArmsColor = green
                            } else if (excludesSmallArms === false) {
                                TFExcludesSmallArms= 'Non'
                                TFExcludesSmallArmsColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesSmallArmsColor}`}}>{TFExcludesSmallArms} </td>

                            )}

                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion des centrales à charbon</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {
                            
                                const excludesThermalCoal = obj['esgData']['sustainabilityIntentionality']['excludesThermalCoal']
                                let TFExcludesThermalCoal = '-'
                                let TFExcludesThermalCoalColor = black
                                if (excludesThermalCoal === true) {
                                    TFExcludesThermalCoal= 'Oui'
                                    TFExcludesThermalCoalColor = green
                                } else if (excludesThermalCoal === false) {
                                    TFExcludesThermalCoal= 'Non'
                                    TFExcludesThermalCoalColor = red
                                }
                                return (
                                           
                                    <td style={{color : `${TFExcludesThermalCoalColor}`}}>{TFExcludesThermalCoal} </td>
    
                                )}
                                       
                            
                        })}

                            </tr>
                            <tr>
                                <td>Exclusion du tabac</td>
                                {portInfos.map((obj, i) => {
                        if (obj // 👈 null and undefined check
                        && Object.keys(obj).length === 0
                        && Object.getPrototypeOf(obj) === Object.prototype){
                            //pass
                        } else {

                            const excludesTobacco = obj['esgData']['sustainabilityIntentionality']['excludesTobacco']
                            let TFExcludesTobacco = '-'
                            let TFExcludesTobaccoColor = black
                            if (excludesTobacco === true) {
                                TFExcludesTobacco= 'Oui'
                                TFExcludesTobaccoColor = green
                            } else if (excludesTobacco === false) {
                                TFExcludesTobacco= 'Non'
                                TFExcludesTobaccoColor = red
                            }
                            return (
                                       
                                <td style={{color : `${TFExcludesTobaccoColor}`}}>{TFExcludesTobacco} </td>

                            )}

                            
                        })}

                            </tr>
                        </tbody>

                        </table>

                
                </div>
                
            </div>
            <div className="disclaimer mt-5">
                <p>Ce document a été élaboré dans le but de présenter des caractéristiques des fonds dans une volonté de transparence et pour donner facilement à tous, l'accès à de l'information publique. 
                    Il ne présente pas une recommandation, un conseil en investissement ou une offre d'achat.
                Les données sont extraites depuis internet à l'aide d'un programme automatisé, elles n'ont pas été vérifées. Ce document ne peut pas être vendu. Il est issu d'un travail gratuit, libre et indépendant.
                Toutes réclamantions peuvent être adréssées à Albertine SASU par courriel à l'adresse albertine@albertine.io</p>
            </div>   



        </div>
        )}

    }

    return (
        <div align='center' className="mt-4">
            <h1>Analyse de fonds</h1>
            {inputPortfolioListBis()}
            
            {buttonAddInputPort()}
            {fundIsLoading ? waitingSvg() : fundInfo()}  
       
            

        </div>
    
    )
}


export default Funds;

