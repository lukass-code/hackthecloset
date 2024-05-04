import React, { useState, useEffect } from 'react';
import './App.css';
import './imageCard'
import ImageCard from './imageCard';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function App() {
  const [currentImages, setCurrentImages] = useState(0);

  useEffect(() => {
    fetch('/get_images?number=10').then(res => res.json()).then(data => {
      setCurrentImages(data);
    });
  }, []);

  const handleImageClick = (e) => {
    console.log(e.target.getAttribute('src'));
    
};

  if (currentImages != 0) {
    return (
      <div class="center">
      <Container fluid>
          <Row className='mb-2'>
          {currentImages.slice(0, 5).map((currentImage) => (
            <Col className='px-1'> <ImageCard handleImageClick={handleImageClick} imageUrl={currentImage[0]} /> </Col>
          ))}
          </Row>
          <Row>
          {currentImages.slice(5, 10).map((currentImage) => (
            <Col className='px-1'> <ImageCard handleImageClick={handleImageClick} imageUrl={currentImage[0]} /> </Col>
          ))}
          </Row>
      </Container>
      </div>
    );
  } else {
    return (
      <div className="App">
      </div>
    );
  }
}

export default App;
