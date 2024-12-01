import streamlit as st

experiments = {
    "INTERFACING HC-05": {
        "components": [
            "HC-05 Bluetooth Module",
            "Arduino or NodeMCU",
            "Jumper Wires",
            "Breadboard"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "TX": "Pin 0 (RX)",
                "RX": "Pin 1 (TX)"
            },
            "NodeMCU": {
                "VCC": "3.3V",
                "GND": "GND",
                "TX": "D2",
                "RX": "D3"
            }
        },
        "code": {
            "Arduino": """
#include <SoftwareSerial.h>

SoftwareSerial Bluetooth(2, 3); // RX -> Pin 2, TX -> Pin 3
char data = 0;

void setup() {
  Bluetooth.begin(9600); // Start HC-05 communication
  pinMode(8, OUTPUT); 
  pinMode(9, OUTPUT);  
  pinMode(10, OUTPUT);  
  pinMode(11, OUTPUT); 
}

void loop() {
  if (Bluetooth.available() > 0) { // Check if data is received
    data = Bluetooth.read(); // Read the incoming data
    if (data != '\n') { // Ignore newline characters
      Bluetooth.print("Received: ");
      Bluetooth.println(data);
    }
    // Control LEDs
    if (data == 'a') digitalWrite(8, HIGH);  
    else if (data == 'b') digitalWrite(8, LOW); 
    if (data == 'c') digitalWrite(9, HIGH);  
    else if (data == 'd') digitalWrite(9, LOW); 
    if (data == 'e') digitalWrite(10, HIGH);  
    else if (data == 'f') digitalWrite(10, LOW); 
    if (data == 'g') digitalWrite(11, HIGH);  
    else if (data == 'h') digitalWrite(11, LOW); 
  }
}
""",
            "NodeMCU": """
#include <SoftwareSerial.h>

SoftwareSerial Bluetooth(D1, D2); // RX -> D1, TX -> D2

void setup() {
  Serial.begin(9600); // Start serial monitor
  Bluetooth.begin(9600); // Start Bluetooth communication
  Serial.println("NodeMCU Ready!");
}

void loop() {
  // Send commands to Arduino through HC-05
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read user input from Serial Monitor
    Bluetooth.write(command); // Send the command to Arduino
    Serial.print("Sent: ");
    Serial.println(command);
  }

  // Read and display any response from Arduino
  if (Bluetooth.available() > 0) {
    char response = Bluetooth.read();
    Serial.print("Received from Arduino: ");
    Serial.println(response);
  }
}
"""
        }
    },
    "INTERFACING ACCELEROMETER": {
        "components": [
            "Accelerometer Module (e.g., MPU6050)",
            "NodeMCU or Arduino",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "SDA": "A4",
                "SCL": "A5"
            },
            "NodeMCU": {
                "VCC": "3.3V",
                "GND": "GND",
                "SDA": "D2",
                "SCL": "D1"
            }
        },
        "code": {
            "Arduino": """
#include <math.h> 

const int x_out = A1;  // Connect x_out of module to A1 of UNO board
const int y_out = A2;  // Connect y_out of module to A2 of UNO board
const int z_out = A3;  // Connect z_out of module to A3 of UNO board

void setup() {  
  Serial.begin(9600);  // Start serial communication
}

void loop() { 
  int x_adc_value, y_adc_value, z_adc_value;
  double x_g_value, y_g_value, z_g_value;
  double roll, pitch, yaw;

  // Read analog values from the accelerometer
  x_adc_value = analogRead(x_out);  // Digital value of voltage on x_out pin
  y_adc_value = analogRead(y_out);  // Digital value of voltage on y_out pin
  z_adc_value = analogRead(z_out);  // Digital value of voltage on z_out pin

  // Print raw ADC values
  Serial.print("x = ");
  Serial.print(x_adc_value);
  Serial.print("\t\t");
  Serial.print("y = ");
  Serial.print(y_adc_value);
  Serial.print("\t\t");
  Serial.print("z = ");
  Serial.print(z_adc_value);
  Serial.print("\t\t");

  // Convert ADC values to g (acceleration in terms of gravity)
  x_g_value = (((double)(x_adc_value * 5) / 1024) - 1.65) / 0.330;  // Acceleration in x-direction in g units
  y_g_value = (((double)(y_adc_value * 5) / 1024) - 1.65) / 0.330;  // Acceleration in y-direction in g units
  z_g_value = (((double)(z_adc_value * 5) / 1024) - 1.80) / 0.330;  // Acceleration in z-direction in g units

  // Calculate roll, pitch, and yaw angles using atan2 for more stable angle calculation
  roll = (((atan2(y_g_value, z_g_value) * 180) / 3.14) + 180);  // Roll calculation
  pitch = (((atan2(z_g_value, x_g_value) * 180) / 3.14) + 180);  // Pitch calculation
  yaw = (((atan2(x_g_value, y_g_value) * 180) / 3.14) + 180);    // Yaw calculation

  // Print calculated angles
  Serial.print("Roll = ");
  Serial.print(roll);
  Serial.print("\t");
  Serial.print("Pitch = ");
  Serial.print(pitch);
  Serial.print("\n\n");

  delay(1000);  // Wait 1 second before taking new readings
}
""",
            "NodeMCU": """
#include <math.h>

const int x_out = A0;  // Use A0 pin of NodeMCU for analog input (single pin available)
const int y_out = D2;  // Use D2 pin as digital output for Y axis (or choose another GPIO pin)
const int z_out = D1;  // Use D1 pin as digital output for Z axis (or choose another GPIO pin)

void setup() {  
  Serial.begin(9600);  // Start serial communication
}

void loop() { 
  int x_adc_value, y_adc_value, z_adc_value;
  double x_g_value, y_g_value, z_g_value;
  double roll, pitch, yaw;

  // Read analog values from the accelerometer
  x_adc_value = analogRead(x_out);  // Digital value of voltage on x_out pin
  y_adc_value = digitalRead(y_out);  // Assuming these are digital outputs for y and z (you may need to change this)
  z_adc_value = digitalRead(z_out);  // Same as above

  // Print raw ADC values
  Serial.print("x = ");
  Serial.print(x_adc_value);
  Serial.print("\t\t");
  Serial.print("y = ");
  Serial.print(y_adc_value);
  Serial.print("\t\t");
  Serial.print("z = ");
  Serial.print(z_adc_value);
  Serial.print("\t\t");

  // Convert ADC values to g (acceleration in terms of gravity)
  x_g_value = (((double)(x_adc_value * 3.3) / 1024) - 1.65) / 0.330;  // Acceleration in x-direction in g units
  y_g_value = (((double)(y_adc_value * 3.3) / 1024) - 1.65) / 0.330;  // Acceleration in y-direction in g units
  z_g_value = (((double)(z_adc_value * 3.3) / 1024) - 1.80) / 0.330;  // Acceleration in z-direction in g units

  // Calculate roll, pitch, and yaw angles using atan2 for more stable angle calculation
  roll = (((atan2(y_g_value, z_g_value) * 180) / 3.14) + 180);  // Roll calculation
  pitch = (((atan2(z_g_value, x_g_value) * 180) / 3.14) + 180);  // Pitch calculation
  yaw = (((atan2(x_g_value, y_g_value) * 180) / 3.14) + 180);    // Yaw calculation

  // Print calculated angles
  Serial.print("Roll = ");
  Serial.print(roll);
  Serial.print("\t");
  Serial.print("Pitch = ");
  Serial.print(pitch);
  Serial.print("\n\n");

  delay(1000);  // Wait 1 second before taking new readings
}
"""
        }
    },
    "INTERFACING GYROSCOPE": {
        "components": [
            "Gyroscope Module (e.g., MPU6050)",
            "NodeMCU or Arduino",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "SDA": "A4",
                "SCL": "A5"
            },
            "NodeMCU": {
                "VCC": "3.3V",
                "GND": "GND",
                "SDA": "D2",
                "SCL": "D1"
            }
        },
        "code": {
            "Arduino": """
#include <Wire.h>  
#include <MPU6050.h>  

MPU6050 mpu;  // Create an MPU6050 object

#define SDA_PIN 4  // Custom SDA pin
#define SCL_PIN 5  // Custom SCL pin

void setup() { 
  Serial.begin(115200);  // Start serial communication
  Serial.println("Initialize MPU6050");

  // Initialize the Wire library with custom SDA and SCL pins
  Wire.begin(SDA_PIN, SCL_PIN);

  // Initialize the MPU6050 sensor
  while (!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G)) {
    Serial.println("Could not find MPU6050, check wiring!");
    delay(500);  // Wait before retrying
  }
  Serial.println("MPU6050 Initialized");
}

void loop() { 
  // Read raw accelerometer values
  Vector rawAccel = mpu.readRawAccel();  
  // Read normalized accelerometer values
  Vector normAccel = mpu.readNormalizeAccel();  

  // Print the raw and normalized accelerometer data
  Serial.print("Raw X = "); Serial.print(rawAccel.XAxis); 
  Serial.print(" Y = "); Serial.print(rawAccel.YAxis); 
  Serial.print(" Z = "); Serial.println(rawAccel.ZAxis);

  Serial.print("Norm X = "); Serial.print(normAccel.XAxis); 
  Serial.print(" Y = "); Serial.print(normAccel.YAxis); 
  Serial.print(" Z = "); Serial.println(normAccel.ZAxis);

  delay(500);  // Delay before the next reading
}
""",
            "NodeMCU": """
#include <Wire.h>  
#include <MPU6050.h>  

MPU6050 mpu;  // Create an MPU6050 object

#define SDA_PIN 4  // Custom SDA pin
#define SCL_PIN 5  // Custom SCL pin

void setup() { 
  Serial.begin(115200);  // Start serial communication
  Serial.println("Initialize MPU6050");

  // Initialize the Wire library with custom SDA and SCL pins
  Wire.begin(SDA_PIN, SCL_PIN);

  // Initialize the MPU6050 sensor
  while (!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G)) {
    Serial.println("Could not find MPU6050, check wiring!");
    delay(500);  // Wait before retrying
  }
  Serial.println("MPU6050 Initialized");
}

void loop() { 
  // Read raw accelerometer values
  Vector rawAccel = mpu.readRawAccel();  
  // Read normalized accelerometer values
  Vector normAccel = mpu.readNormalizeAccel();  

  // Print the raw and normalized accelerometer data
  Serial.print("Raw X = "); Serial.print(rawAccel.XAxis); 
  Serial.print(" Y = "); Serial.print(rawAccel.YAxis); 
  Serial.print(" Z = "); Serial.println(rawAccel.ZAxis);

  Serial.print("Norm X = "); Serial.print(normAccel.XAxis); 
  Serial.print(" Y = "); Serial.print(normAccel.YAxis); 
  Serial.print(" Z = "); Serial.println(normAccel.ZAxis);

  delay(500);  // Delay before the next reading
}
"""
        }
    },
    "INTERFACING COLOR SENSOR": {
        "components": [
            "Color Sensor (e.g., TCS3200)",
            "NodeMCU or Arduino",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "S0": "Pin 2",
                "S1": "Pin 3",
                "S2": "Pin 4",
                "S3": "Pin 5",
                "OUT": "Pin 6"
            },
            "NodeMCU": {
                "VCC": "3.3V",
                "GND": "GND",
                "S0": "D2",
                "S1": "D3",
                "S2": "D4",
                "S3": "D5",
                "OUT": "D6"
            }
        },
        "code": {
            "Arduino": """
#define S0 2
#define S1 3
#define S2 4
#define S3 5
#define OUT 6

void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(OUT, INPUT);
  digitalWrite(S0, LOW);
  digitalWrite(S1, HIGH);
}

void loop() {
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  int red = pulseIn(OUT, LOW);
  digitalWrite(S3, HIGH);
  int blue = pulseIn(OUT, LOW);
  digitalWrite(S2, HIGH);
  digitalWrite(S3, LOW);
  int green = pulseIn(OUT, LOW);
  Serial.print("Red: "); Serial.print(red);
  Serial.print(" Green: "); Serial.print(green);
  Serial.print(" Blue: "); Serial.println(blue);
  delay(500);
}
""",
            "NodeMCU": """
#define S0 D2
#define S1 D3
#define S2 D4
#define S3 D5
#define OUT D6

void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(OUT, INPUT);
  digitalWrite(S0, LOW);
  digitalWrite(S1, HIGH);
}

void loop() {
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  int red = pulseIn(OUT, LOW);
  digitalWrite(S3, HIGH);
  int blue = pulseIn(OUT, LOW);
  digitalWrite(S2, HIGH);
  digitalWrite(S3, LOW);
  int green = pulseIn(OUT, LOW);
  Serial.print("Red: "); Serial.print(red);
  Serial.print(" Green: "); Serial.print(green);
  Serial.print(" Blue: "); Serial.println(blue);
  delay(500);
}
"""
        }
    }
}

# Streamlit UI
st.title("Microcontroller Experiments")
st.sidebar.title("Select an Experiment")
selected_experiment = st.sidebar.selectbox("Experiments", list(experiments.keys()))

# Display selected experiment details
experiment = experiments[selected_experiment]

st.header(selected_experiment)
st.subheader("Components Required")
st.write(", ".join(experiment["components"]))

st.subheader("Connections")
col1, col2 = st.columns(2)

with col1:
    st.write("**Arduino**")
    for pin, connection in experiment["connections"]["Arduino"].items():
        st.write(f"- **{pin}** → {connection}")

with col2:
    st.write("**NodeMCU**")
    for pin, connection in experiment["connections"]["NodeMCU"].items():
        st.write(f"- **{pin}** → {connection}")

st.subheader("Code")

# Tabs for Arduino and NodeMCU code
tabs = st.radio("Select Platform", ["Arduino", "NodeMCU"])

if tabs == "Arduino":
    st.code(experiment["code"]["Arduino"], language="cpp")
else:
    st.code(experiment["code"]["NodeMCU"], language="cpp")
