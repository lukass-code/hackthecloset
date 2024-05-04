import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import React, { useState, useEffect } from 'react';
import Image from 'react-bootstrap/Image';


function ImageCard(props) {
    return (
      <Card className="imageCard" style={{ cursor: "pointer" }}>
        <Card.Body>
          <Card.Text>
          <Image name={props.index} onClick={props.handleImageClick} src={props.imageUrl} fluid/>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

export default ImageCard;