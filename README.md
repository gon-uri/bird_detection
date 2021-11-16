<img src="https://github.com/gon-uri/bird_detection/blob/main/img/LogoLSD.png" align="right"
     alt="LSD logo" width="370" height="100">
     
# Bird Detection Algorithm

Machine learning algorithm to identify the presence and location of birds.

Created by Gonzalo Uribarri at [Dynamical Systems Lab](http://www.lsd.df.uba.ar/)

This project has two main objectives:
* Detect the presence of given bird species in audio data gathered by one microphone in the field. In this case, we will focus on "Chingolos" ([Zonotrichia capensis](https://es.wikipedia.org/wiki/Zonotrichia_capensis)). **First version available**
* Detect the presence and location of individuals of a specific bird species in audio data collected by an array of microphones in the field. **Under Development**

## How It Works

### Bird Detection
1. It generates a challenging dataset of '.wav' files combining the vocalizations of the target bird species with real recordings from birds in natural ambients and wind.
2. It reads and preprocesses the data using Torchaudio.
3. It trains a deep 1D-convolutional Neural Network for the classification task.
4. It evaluates the results and saves the model for usage.

### Bird Detection & Localization
1. Loads the vocalizations of the target bird species, real recordings from birds in natural ambients and wind sound.
2. The birds and ambient sounds are located in a simple virtual open field environment.
3. It computes the sound arriving at each microphone in the array.
4. It generates a dataset of '.wav' files with a number of channels equal to the number of microphones in the array.
6. It reads and preprocesses the data using Torchaudio.
7. It trains a deep 1D-convolutional Neural Network for the classification task (Detection) and the regression task (localization).
8. It evaluates the results and saves the model for usage.

## Usage

### Bird vocalizations
You have to locate your .wav files corresponding to the bird vocalizations on "/train" and "/test" folders. You can find vocalization of a given bird species in Xeno-Canto [https://www.xeno-canto.org/](https://www.xeno-canto.org/).

### Kaggle credentials
We use a Kaggle dataset of sounds to get ambient sound and wind sound. Notice you will have to locate your "kaggle.json" API token on your root folder (to create and download your kaggle API token follow this instructions [https://www.kaggle.com/docs/api](https://www.kaggle.com/docs/api)).
