import Button from 'react-bootstrap/Button';
import React, { useState, useEffect } from 'react';


function ResetButton(props){
    const handleClick = () =>{
        fetch("./reset_choice");
        props.handleResetClick();
    }

    return(
    <Button className="fixed-element" variant="dark" onClick={handleClick}>Reset</Button>
    );
}

export default ResetButton