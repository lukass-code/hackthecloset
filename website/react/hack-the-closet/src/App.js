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
    if (currentImages[i][1]["section"] == featuresClicked["section"]) {
      currentImagesScore[i] = currentImagesScore[i] + 5;
    } else {
      currentImagesScore[i] = currentImagesScore[i] - 5;
    }
  }
}

function checkReplace(currentImagesScore) {
  const replace_list = [];
  for (let i = 0; i < currentImagesScore.length; i++) {
    if (currentImagesScore[i] < 0) {
      replace_list.push(i)
    }
  }
  return replace_list
}

function replaceImages(replacelist, setCurrentImages) {
  for (let i = 0; i < replacelist.length; i++) {
    fetch('/get_images?number=10').then(res => res.json()).then(data => {
      setCurrentImages(data);
    });
  }
}

function App() {
  const [currentImages, setCurrentImages] = useState(0);
  const currentImagesScore = new Array(10).fill(0)

  useEffect(() => {
    fetch('/get_images?number=10').then(res => res.json()).then(data => {
      setCurrentImages(data);
    });
  }, []);

  const handleImageClick = (e) => {
    updateScores(e.target.name, currentImagesScore, currentImages)
    //console.log(currentImagesScore);
    console.log(checkReplace(currentImagesScore));
    replaceImages(checkReplace(currentImagesScore), setCurrentImages);


  };

  if (currentImages != 0) {
    return (
      <div class="center">
        <Container fluid>
          <Row className='mb-2'>
            {currentImages.slice(0, 5).map((currentImage, index) => (
              <Col className='px-1'> <ImageCard handleImageClick={handleImageClick} index={index} imageUrl={currentImage[0][0]} /> </Col>
            ))}
          </Row>
          <Row>
            {currentImages.slice(5, 10).map((currentImage, index) => (
              <Col className='px-1'> <ImageCard handleImageClick={handleImageClick} index={index + 5} imageUrl={currentImage[0][0]} /> </Col>
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
