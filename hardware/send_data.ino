#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Ahmedsaed";
const char* password = "ahmedsaed2652003";

const char* apiEndpoint = "http://165.227.131.111:9998/api/data/update"; // Replace with your API endpoint 165.227.131.111:9998
const int buttonPin = 2; // Replace with the GPIO pin where your button is connected

bool buttonState = false;

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set up button pin
  pinMode(buttonPin, INPUT_PULLDOWN);

  Serial.println("Press the button to send data...");
}

void loop() {
  // Read button state
  bool newButtonState = digitalRead(buttonPin);

  // Check if the button is pressed
  if (newButtonState != buttonState && newButtonState == HIGH) {
    Serial.println("Button pressed!");

    // Your sensor data
    float temperature = 25.5;
    float ph = 7.0;
    float waterLevel = 0.5;

    // Create JSON payload
    String payload = "{\"temperature\":" + String(temperature) + ",\"ph\":" + String(ph) + ",\"water_level\":" + String(waterLevel) + "}";

    // Send PUT request
    sendPutRequest(apiEndpoint, payload);

    Serial.println("Data sent successfully");
  }

  // Update button state
  buttonState = newButtonState;

  // Add a delay to avoid button debouncing
  delay(50);
}

void sendPutRequest(const char* url, String payload) {
  HTTPClient http;

  // Begin HTTP connection
  http.begin(url);

  // Set content type to JSON
  http.addHeader("Content-Type", "application/json");

  // Send PUT request with payload
  int httpResponseCode = http.PUT(payload);

  // Check for a successful response
  if (httpResponseCode > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
  } else {
    Serial.print("HTTP Request failed with error code: ");
    Serial.println(httpResponseCode);
  }

  // End HTTP connection
  http.end();
}
