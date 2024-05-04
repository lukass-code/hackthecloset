import React, { useState, useEffect } from 'react';
import './App.css';
import './imageCard'
import ResetButton from './ResetButton';
import ImageCard from './imageCard';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

//Updates the score for each image
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

//Checks is the image score is too low (<0)
function checkReplace(currentImagesScore) {
  const replace_list = [];
  for (let i = 0; i < currentImagesScore.length; i++) {
    if (currentImagesScore[i] < 0) {
      replace_list.push(i)
      currentImagesScore[i] = 0;
    }
  }
  const lowest = Math.min.apply(Math, currentImagesScore);
  console.log(lowest)
  const minIndex = currentImagesScore.indexOf(lowest);
  if (!replace_list.includes(minIndex)) {
    replace_list.push(minIndex);
    currentImagesScore[minIndex] = 0;
  }else{
    console.log("tes")
  }
  console.log(replace_list)
  return replace_list
}

//Updates image data in list
const handlereplaceImages = (currentImages, image_data, index, setCurrentImages) => {
  //console.log(currentImages)
  setCurrentImages(currentImages => {
    const updatedArtists = [...currentImages];
    updatedArtists[index] = image_data;
    return updatedArtists;
  });
};

//Replaces the image in the image list (fetches new image data)
function replaceImages(replacelist, currentImages, setCurrentImages) {
  for (let i = 0; i < replacelist.length; i++) {
    fetch('/get_image').then(res => res.json()).then(data => {
      handlereplaceImages(currentImages, data, replacelist[i], setCurrentImages);
    });
    console.log(i)

  }
}

function sendNewChoiceData(imageData) {
  let json = JSON.stringify(imageData)
  fetch('/set_choice?choice=' + json)
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
    sendNewChoiceData(currentImages[e.target.name][1]) //it is the clicked index
    currentImagesScore = updateScores(e.target.name, currentImagesScore, currentImages);
    //console.log(currentImagesScore);
    replaceImages(checkReplace(currentImagesScore), currentImages, setCurrentImages);



  };

  const handleResetClick = (e) => {
    replaceImages([...Array(10).keys()], currentImages, setCurrentImages);
  }

  if (currentImages != 0) {
    return (
      <div>
        <ResetButton handleResetClick={handleResetClick} />
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
