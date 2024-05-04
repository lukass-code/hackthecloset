import React, { useState, useEffect } from 'react';
import './App.css';
import './imageCard'
import ImageCard from './imageCard';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function updateScores(clickedIndex, currentImagesScore, currentImages) {
  var featuresClicked = currentImages[clickedIndex][1]
  for (let i = 0; i < currentImages.length; i++) {
    if (currentImages[i][1]["product_type"] == featuresClicked["product_type"]) {
      currentImagesScore[i] = currentImagesScore[i] + 5;
    } else {
      currentImagesScore[i] = currentImagesScore[i] - 5;
    }
  }
  return currentImagesScore;
}

function checkReplace(currentImagesScore) {
  const replace_list = [];
  for (let i = 0; i < currentImagesScore.length; i++) {
    if (currentImagesScore[i] < 0) {
      replace_list.push(i)
      currentImagesScore[i] = 0;
    }
  }
  console.log(currentImagesScore)
  return replace_list
}

const handlereplaceImages = (currentImages, image_data, index, setCurrentImages) => {
  //console.log(currentImages)
  setCurrentImages(currentImages => {
    const updatedArtists = [...currentImages];
    updatedArtists[index] = image_data;
    return updatedArtists;
  });
};


function replaceImages(replacelist, currentImages, setCurrentImages) {
  for (let i = 0; i < replacelist.length; i++) {
    fetch('/get_image').then(res => res.json()).then(data => {
      handlereplaceImages(currentImages, data, replacelist[i], setCurrentImages);
    });
    console.log(i)
    
  }
}

function App() {
  const [currentImages, setCurrentImages] = useState(0);
  var currentImagesScore = new Array(10).fill(0)

  useEffect(() => {
    fetch('/get_images?number=10').then(res => res.json()).then(data => {
      setCurrentImages(data);
    });
  }, []);

  const handleImageClick = (e) => {
    currentImagesScore = updateScores(e.target.name, currentImagesScore, currentImages);
    //console.log(currentImagesScore);
    replaceImages(checkReplace(currentImagesScore),currentImages, setCurrentImages);
    


  };

  if (currentImages != 0) {
    return (
      <div class="center">
        <Container fluid>
          <Row className='mb-2'>
            {currentImages.slice(0, 5).map((currentImage, index) => (
              <Col className='px-1'> <ImageCard key={Date.now()} handleImageClick={handleImageClick} index={index} imageUrl={currentImage[0][0]} /> </Col>
            ))}
          </Row>
          <Row>
            {currentImages.slice(5, 10).map((currentImage, index) => (
              <Col className='px-1'> <ImageCard key={Date.now()} handleImageClick={handleImageClick} index={index + 5} imageUrl={currentImage[0][0]} /> </Col>
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
