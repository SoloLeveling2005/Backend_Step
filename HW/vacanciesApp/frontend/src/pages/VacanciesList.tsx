import React, {useEffect, useState} from 'react';
import axios from 'axios';


function VacanciesList(props: any) {

    const [vacancies, changeVacancies] = useState([]);


    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/api/vacancies`, {
            headers:{
                "Accept": "application/json",
                "Access-Control-Allow-Origin": "*",
            }
        }).then(response=> {
            console.log(response)
        }).catch(error=>{
            console.log(error)
        });
    });

    return (
        <section className="container mt-3">
            <h2 className="mb-4">Топ вакансий</h2>
            {vacancies.map((item, index)=>(
                <div className="card">
                    <div className="card-header">
                        Quote
                    </div>
                    <div className="card-body">
                        <blockquote className="blockquote mb-0">
                            <p>A well-known quote, contained in a blockquote element.</p>
                            <footer className="blockquote-footer">Someone famous in <cite title="Source Title">Source
                                Title</cite></footer>
                        </blockquote>
                    </div>
                </div>
            ))}

        </section>
    );
};

export default VacanciesList;
