# Automated Jitropha Planting And Oil Extraction

## Description

To expedite the cultivation of Jatropha curcas plants and maximize efficiency, we will implement an advanced approach. We intend to develop automated systems powered by artificial intelligence, streamlining the planting process and significantly reducing the resources required for Jatropha plants to reach maturity.

Furthermore, as an integral part of our solution, we plan to establish a dedicated facility equipped with state-of-the-art technology. This facility will house automated systems designed to extract oil from Jatropha seeds efficiently. The extracted oil will undergo meticulous processing, ensuring it meets the necessary standards to serve as a viable and clean fuel alternative.

By combining artificial intelligence in the cultivation process and investing in a cutting-edge oil extraction facility, we aim to not only enhance the overall efficiency of our solution but also contribute to a sustainable future by accelerating the production of biofuel from Jatropha oil. This strategic approach aligns with our commitment to minimizing environmental impact and advancing renewable energy practices.

## Data Collection

The data collection process is a crucial aspect of our solution. For the computer vision models, we gathered the data from public datasets and online sources. The data includes images of Jatropha leaves and seeds, which will be used to train the models for health and ripeness prediction.

The data can be found in the `data` directory, which should be extracted to the `jitropha` directory. The `jitropha` directory contains the following subdirectories:
- `leaf`: Contains images of Jatropha leaves, categorized into `diseased` and `healthy` subdirectories.
- `seed`: Contains images of Jatropha seeds, categorized into `ripe` and `unripe` subdirectories.

## Model Training

The model training process involves training three computer vision models:
- The first model is a health prediction model that predicts whether a Jatropha leaf is healthy or diseased.
- The second model is a ripeness prediction model that predicts whether a Jatropha seed is ripe or unripe.
- The third model is a reinforcement learning (RL) model that provides recommendations based on environmental data.

The first 2 models are trained using TensorFlow and Keras, and the training process is detailed in the following Jupyter notebooks:
- `jitropha-health.ipynb`: This notebook contains the code for training the health prediction model using images of Jatropha leaves.
- `jitropha-ripeness.ipynb`: This notebook contains the code for training the ripeness prediction model using images of Jatropha seeds.

The RL model is trained using the Stable Baselines library, and the training process is detailed in the following Jupyter notebook:
- `jitropha-recommendation-system.ipynb`: This notebook contains the code for training the RL model to provide recommendations based on environmental data.

The trained models are saved in the `Training/{model_name}` directory:

## Mobile Application

The mobile application is designed to provide a user-friendly interface for monitoring and managing the Jatropha cultivation process. The application allows users to view real-time environmental data, receive health and ripeness predictions, and access recommendations from the RL model.

The mobile application is built using the Flutter framework, and the source code can be found in the `mobile_application` directory.

![IMPORTANT]
The mobile application is a submodule of the main repository. To clone the repository with the submodule, use the following command:
```bash
git clone --recurse-submodules <repository_url>
```

The application is designed to run on both Android and iOS devices. To run the application, follow the instructions in the `mobile_application/README.md` file.

## API Server

The API server is designed to provide endpoints for data fetching and model inference. The server is built using the Flask framework and provides routes for retrieving environmental data and making predictions using the trained models.

The API is hosted on Firebase/Google Cloud Platform and can be hosted on a local server as well. The source code for the API server can be found in the `API` directory.

To run the API server, run `run.py` using python3.8. The server will start on `http://localhost:5000` by default.

## How To Use

1. You need to have git lfs installed to clone this repository. If you don't have Git LFS (Large File Storage) installed, you can install it from [here](https://git-lfs.github.com/).
1. Clone the repository using the following command:
   ```bash
   git clone --recurse-submodules <repository_url>
   ```
    Replace `<repository_url>` with the URL of the repository.
1. Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```
1. Run the API server using the following command:
    ```bash
    python run.py
    ```
1. Follow the instructions in the `mobile_application/README.md` file to run the mobile application.

## API Documentation

### Data Fetching

API Documentation:

1. **Endpoint:** `/api/data/temperature/<int:n>`
   - **Method:** GET
   - **Description:** Retrieve the specified number (`n`) of latest temperature records.
   - **Parameters:**
     - `n` (Optional): Number of records to retrieve. Defaults to 5 if not specified.

2. **Endpoint:** `/api/data/light_intensity/<int:n>`
   - **Method:** GET
   - **Description:** Retrieve the specified number (`n`) of latest light intensity records.
   - **Parameters:**
     - `n` (Optional): Number of records to retrieve. Defaults to 5 if not specified.

3. **Endpoint:** `/api/data/co2_level/<int:n>`
   - **Method:** GET
   - **Description:** Retrieve the specified number (`n`) of latest CO2 level records.
   - **Parameters:**
     - `n` (Optional): Number of records to retrieve. Defaults to 5 if not specified.

4. **Endpoint:** `/api/data/water_ph_value/<int:n>`
   - **Method:** GET
   - **Description:** Retrieve the specified number (`n`) of latest water pH value records.
   - **Parameters:**
     - `n` (Optional): Number of records to retrieve. Defaults to 5 if not specified.

## Model Inference

1. Health Prediction Route

##### Route:
`POST /api/models/health`

##### Description:
This route receives an image file and utilizes a pre-trained TensorFlow model to predict whether the image represents a healthy or unhealthy object based on the provided image data.

##### Request Parameters:
- Method: `POST`
- Headers:
  - `Content-Type: multipart/form-data`
- Form Data:
  - `image`: File (Image file to be predicted)

##### Response:
- Content Type: `application/json`
- Body:
  - `prediction`: Boolean (True if the model predicts the object as healthy, False otherwise)

##### Example Usage:

**Request:**
```http
POST /api/models/health
Content-Type: multipart/form-data

<Attach image file to the request>
```

```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "image=@./jitropha/leaf/diseased/0018_0001.JPG" http://165.227.131.111:9998/api/models/health;
```

**Response:**
```json
{
  "prediction": true
}
```

2. Ripe Prediction Route

##### Route:
`POST /api/models/ripe`

##### Description:
This route accepts an image file and performs prediction using a pre-trained TensorFlow model. The model predicts whether the image represents a ripe object based on the given image data.

##### Request Parameters:
- Method: `POST`
- Headers:
  - `Content-Type: multipart/form-data`
- Form Data:
  - `image`: File (Image file to be predicted)

##### Response:
- Content Type: `application/json`
- Body:
  - `prediction`: Boolean (True if the model predicts the object as ripe, False otherwise)

3. Recommendation RL Model Route

**Route:** `/api/models/recommendation`

**Method:** `POST`

**Description:**
This API route is designed to receive a JSON payload containing environmental data (temperature, pH, water level) and provide a recommendation using a pre-trained Reinforcement Learning (RL) model.

**Request:**
- **Type:** JSON
- **Structure:**
  - `temperature` (float): The temperature value.
  - `ph` (float): The pH value.
  - `water_level` (float): The water level value.

**Example Request:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"temperature": 25.5, "ph": 7.0, "water_level": 0.5}' http://localhost:5000/api/models/recommendation
```

**Response:**
- **Type:** JSON
- **Structure:**
  - `prediction` (list): The recommended action based on the RL model.

**Example Response:**
```json
{"prediction": [0, 0, 0]}
```

**Notes:**
- The RL model is loaded from a pre-trained PPO (Proximal Policy Optimization) model file (`best_model.zip`).
- The API internally uses the model to simulate interactions with an environment and provides a recommendation.
- The returned `prediction` list represents the recommended action or decision.

**Important:**
- Ensure that the Flask API is running and accessible at the specified URL before making requests.
- Adjust the values in the request payload according to your specific use case.
