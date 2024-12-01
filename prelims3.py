import streamlit as st

# Experiments data structure
experiments = {
    "Displaying Text/Images using LCD":{
        "components": [
            "NodeMCU",
            "LCD"
        ],
        "connections": {
            "LCD VSS": "nodemcu GND",
            "LCD VDD": "5V",
            "SDA":"D2",
            "SCL":"D1"
        },
        "code": """
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Initialize the LCD with I2C address 0x27 and the size (16x2)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.begin(16, 2);  // Set up the LCD with 16 columns and 2 rows
  
  // Display Text
  lcd.print("Hello, World!");
  delay(2000);  // Wait for 2 seconds before drawing image
  
  // Draw a simple image (heart shape example)
  lcd.clear();
  lcd.setCursor(0, 0);
  
  // Create a heart shape image using custom characters
  byte heart[] = {
    B00011000, B00111100, B01111110, B11111111, B11111111,
    B01111110, B00111100, B00011000
  };
  
  for (int i = 0; i < 8; i++) {
    lcd.createChar(i, heart[i]);  // Create custom character
    lcd.setCursor(i, 1);          // Set cursor to row 1 (second row)
    lcd.write(i);                 // Write custom character to screen
  }
}

void loop() {
  // Nothing to do here as the display is updated in setup
}
"""
    },
    "Controlling an LED using Webpage with NodeMCU": {
        "components": [
            "NodeMCU",
            "LED",
            "Resistor (220Ω)",
            "Jumper Wires",
            "Breadboard"
        ],
        "connections": {
            "LED Positive (Anode)": "D1",
            "LED Negative (Cathode)": "GND"
        },
        "code": """
#include <ESP8266WiFi.h>

const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";

WiFiServer server(80);

void setup() {
  pinMode(D1, OUTPUT);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    String request = client.readStringUntil('\\r');
    client.flush();

    if (request.indexOf("/LED=ON") != -1) {
      digitalWrite(D1, HIGH);
    } else if (request.indexOf("/LED=OFF") != -1) {
      digitalWrite(D1, LOW);
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println();
    client.println("<!DOCTYPE HTML>");
    client.println("<html>");
    client.println("<a href=\"/LED=ON\">Turn LED ON</a><br>");
    client.println("<a href=\"/LED=OFF\">Turn LED OFF</a><br>");
    client.println("</html>");
    delay(1);
  }
}
"""
    },
    "Fire Accident Detection Project using MQ135 and LM35 - Generate Alert using GSM/Mail": {
        "components": [
            "NodeMCU",
            "LM35 Temperature Sensor",
            "MQ135 Gas Sensor",
            "GSM Module",
            "Jumper Wires",
            "Breadboard"
        ],
        "connections": {
            "LM35 Output": "A0",
            "MQ135 Output": "D1",
            "GSM TX": "D7",
            "GSM RX": "D6",
            "VCC (Sensors)": "3.3V",
            "GND (Sensors)": "GND"
        },
        "code": """
#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>

const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";

SoftwareSerial gsmSerial(D7, D6); // GSM module connection

void setup() {
  Serial.begin(9600);
  gsmSerial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  int temp = analogRead(A0);
  int gas = digitalRead(D1);

  if (temp > 50 || gas == HIGH) {
    sendAlert();
  }
  delay(1000);
}

void sendAlert() {
  gsmSerial.println("AT+CMGF=1"); // Set SMS mode
  delay(100);
  gsmSerial.println("AT+CMGS=\"+1234567890\""); // Replace with recipient's phone number
  delay(100);
  gsmSerial.println("ALERT! Fire detected.");
  delay(100);
  gsmSerial.println((char)26); // Ctrl+Z to send the SMS
  delay(100);
}
"""
    },
    "Logistics Tracker Using NodeMCU and GPS": {
        "components": [
            "NodeMCU",
            "GPS Module",
            "Jumper Wires",
            "Breadboard"
        ],
        "connections": {
            "GPS TX": "D1",
            "GPS RX": "D2",
            "VCC": "3.3V",
            "GND": "GND"
        },
        "code": """
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>

SoftwareSerial gpsSerial(D1, D2);
const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";

void setup() {
  Serial.begin(9600);
  gpsSerial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  if (gpsSerial.available()) {
    String gpsData = gpsSerial.readStringUntil('\\n');
    sendGPSData(gpsData);
  }
}

void sendGPSData(String data) {
  WiFiClient client;
  if (client.connect("your-server.com", 80)) {
    client.print("GET /log?data=");
    client.print(data);
    client.println(" HTTP/1.1");
    client.println("Host: your-server.com");
    client.println();
  }
  client.stop();
}
"""
    },
    "Interfacing Gyro and Bluetooth with ATtiny85": {
        "components": [
            "ATtiny85",
            "MPU6050 Gyroscope",
            "HC-05 Bluetooth Module",
            "Jumper Wires",
            "Breadboard"
        ],
        "connections": {
            "Gyro SDA": "Pin 5",
            "Gyro SCL": "Pin 7",
            "HC-05 TX": "Pin 6",
            "HC-05 RX": "Pin 2",
            "VCC (Modules)": "5V",
            "GND (Modules)": "GND"
        },
        "code": """
#include <TroykaDHT.h>
#include <SoftwareSerial.h>
#include <Adafruit_MPU6050.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
SoftwareSerial ble_device(0, 1); // BLE TX-> ATtiny85 PB0, RX-> ATtiny85 PB1
DHT dht(4, DHT22); // DHT22 sensor on PB4

void setup() {
  dht.begin();
  ble_device.begin(9600);
  delay(500);
  
  // Change device name and reset BLE
  ble_device.println("AT+NAMEATtiny85_BLE");
  delay(500);
  ble_device.println("AT+RESET");
  delay(1000);

  Serial.println("MPU6050 Found!");
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  delay(100);
}

void loop() {
  String ble_str = "";
  dht.read();
  
  if (dht.getState() == DHT_OK) {
    // Read DHT22 data and prepare string for BLE
    ble_str += String(millis() / 1000.0) + ","; // Timestamp
    ble_str += String(dht.getTemperatureC(), 2) + ","; // Temperature
    ble_str += String(dht.getHumidity(), 2); // Humidity

    // Send BLE data
    ble_device.println(ble_str);

    // Read MPU6050 data
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    // Print out MPU6050 data
    Serial.print("Accel X: "); Serial.print(a.acceleration.x); Serial.print(", ");
    Serial.print("Y: "); Serial.print(a.acceleration.y); Serial.print(", ");
    Serial.print("Z: "); Serial.println(a.acceleration.z);

    Serial.print("Gyro X: "); Serial.print(g.gyro.x); Serial.print(", ");
    Serial.print("Y: "); Serial.print(g.gyro.y); Serial.print(", ");
    Serial.print("Z: "); Serial.println(g.gyro.z);
  }

  delay(2000); // Wait before the next reading
}
"""
    },
    "Interfacing Ultrasonic Sensors and Other Sensors with NodeMCU": {
        "components": [
            "NodeMCU",
            "Ultrasonic Sensor (HC-SR04)",
            "Other Sensors (e.g., Temperature Sensor)",
            "Jumper Wires",
            "Breadboard"
        ],
        "connections": {
            "Ultrasonic Trigger Pin": "D1",
            "Ultrasonic Echo Pin": "D2",
            "VCC (Sensors)": "3.3V",
            "GND (Sensors)": "GND"
        },
        "code": """
#include <ESP8266WiFi.h>
#include <NewPing.h>

const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";

#define TRIG_PIN D1
#define ECHO_PIN D2
#define MAX_DISTANCE 200

NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  delay(500);
  int distance = sonar.ping_in();
  Serial.print("Distance: "); 
  Serial.print(distance);
  Serial.println(" cm");

  if (distance < 10) {
    Serial.println("Object detected within 10 cm!");
  }
}
"""
    }
}

# Streamlit UI
st.title("Microcontroller Experiments with NodeMCU and Other Platforms")
st.sidebar.title("Select an Experiment")
selected_experiment = st.sidebar.selectbox("Experiments", list(experiments.keys()))

# Display selected experiment details
experiment = experiments[selected_experiment]

st.header(selected_experiment)
st.subheader("Components Required")
st.write(", ".join(experiment["components"]))

st.subheader("Connections")
for pin, connection in experiment["connections"].items():
    st.write(f"- **{pin}** → {connection}")

st.subheader("Code")
st.code(experiment["code"], language="cpp")
