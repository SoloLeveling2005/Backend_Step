import React, {useEffect, useState} from 'react';
import axios from "axios";


function Vacancy(props: any) {
    const vacancyId = props.id;

    const [vacancy, changeVacancy] = useState(null);


    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/api/vacancy/${vacancyId}`, {}).then((response)=>{
            console.log(response)
        }).catch((error)=>{
            console.log(error)
        });
    });

    return (
        <div>

        </div>
    );
};

export default Vacancy;
