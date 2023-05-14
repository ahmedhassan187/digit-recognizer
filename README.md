# Handwritten Digit Recognition using LeNet-5 Architecture and Streamlit

This is a project that recognizes handwritten digits using the LeNet-5 architecture and deploys the model using Streamlit, a popular Python library for building interactive web applications.

## Requirements

- Python 3.x
- TensorFlow
- Streamlit
- Numpy
- OpenCv

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/ahmedhassan187/digit-recognizer
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   streamlit run app.py
   ```

4. Open the URL `http://localhost:8501` in your browser to access the web application.

## Usage

1. Upload a photo of a handwritten digit to the web application.

2. The LeNet-5 model will then predict the digit and display the result on the screen.

## Website Link

[Website](https://ahmedhassan187-digit-recognizer-app-cfxypk.streamlit.app/)
## Files

- `app.py`: This is the main file that contains the code for deploying the model using Streamlit.

- `model.ipynb`: This file contains the implementation of the LeNet-5 architecture.

- `Utilites.py`: This file contains the helper functions used for loading and preprocessing the input image.

- `model.h5`: This is the trained model that is used for predicting the digit.

- `requirements.txt`: This file contains the list of required packages and their versions.

## Acknowledgements

This project was made possible thanks to the following resources:

- [MNIST dataset](https://www.tensorflow.org/datasets/catalog/mnist)
- [LeNet-5 Paper](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)
- [Streamlit documentation](https://docs.streamlit.io/)
