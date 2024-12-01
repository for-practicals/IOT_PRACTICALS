import streamlit as st

experiments = {
    "PWM Signaling - LED Interfacing": {
        "components": [
            "NodeMCU or Arduino",
            "LED",
            "Resistor (220Ω)",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "LED Anode": "PWM Pin (e.g., Pin 9)",
                "LED Cathode": "GND through Resistor"
            },
            "NodeMCU": {
                "LED Anode": "PWM Pin (e.g., D1)",
                "LED Cathode": "GND through Resistor"
            }
        },
        "code": {
            "Arduino": """
#include <Arduino.h>

int ledPin = 9; // PWM pin

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
}
""",
            "NodeMCU": """
int ledPin = D1; // PWM pin

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 1023; brightness++) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
  for (int brightness = 1023; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
}
"""
        }
    },
    "Interfacing IR Sensor": {
        "components": [
            "NodeMCU or Arduino",
            "IR Sensor",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "OUT": "Digital Pin (e.g., Pin 7)"
            },
            "NodeMCU": {
                "VCC": "3.3V",
                "GND": "GND",
                "OUT": "Digital Pin (e.g., D2)"
            }
        },
        "code": {
            "Arduino": """
#define IR_SENSOR_PIN 7 // ARDUINO 
#define LED_PIN 9// ARDUINO  

void setup() {
  pinMode(IR_SENSOR_PIN, INPUT);  // Set IR sensor pin as input
  pinMode(LED_PIN, OUTPUT);       // Set LED pin as output
}

void loop() {
  int sensorValue = digitalRead(IR_SENSOR_PIN);  // Read the IR sensor output
  if (sensorValue == LOW) {                      // If obstacle detected
    digitalWrite(LED_PIN, HIGH);                 // Turn on LED
  } else {
    digitalWrite(LED_PIN, LOW);                  // Turn off LED
  }
  delay(10);  // Short delay for stability
}
""",
            "NodeMCU": """
#define IR_SENSOR_PIN D5  // NODE MCU
#define LED_PIN D6        // NODE MCU

void setup() {
  pinMode(IR_SENSOR_PIN, INPUT);  // Set IR sensor pin as input
  pinMode(LED_PIN, OUTPUT);       // Set LED pin as output
}

void loop() {
  int sensorValue = digitalRead(IR_SENSOR_PIN);  // Read the IR sensor output
  if (sensorValue == LOW) {                      // If obstacle detected
    digitalWrite(LED_PIN, HIGH);                 // Turn on LED
  } else {
    digitalWrite(LED_PIN, LOW);                  // Turn off LED
  }
  delay(10);  // Short delay for stability
}
"""
        }
    },
    "Interfacing Potentiometer": {
        "components": [
            "NodeMCU or Arduino",
            "Potentiometer",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "Wiper (middle pin)": "Analog Pin (e.g., A0)"
            },
            "NodeMCU": {
                "VCC": "3.3V",
                "GND": "GND",
                "Wiper (middle pin)": "Analog Pin (e.g., A0)"
            }
        },
        "code": {
            "Arduino": """
int potPin = A0;         // Pin connected to potentiometer
int ledPin = 9;          // PWM pin connected to LED
int potValue = 0;        // Variable to store potentiometer value
int pwmValue = 0;        // Variable to store PWM output

void setup() {
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
}

void loop() {
  potValue = analogRead(potPin);              // Read potentiometer value (0-1023)
  pwmValue = map(potValue, 0, 1023, 0, 255);  // Map value to PWM range (0-255)
  analogWrite(ledPin, pwmValue);              // Write PWM value to LED
  delay(10);                                  // Small delay for stability
}
""",
            "NodeMCU": """
int potPin = A0;         // Pin connected to potentiometer (A0 on NodeMCU)
int ledPin = D1;         // PWM pin connected to LED (D1 or other PWM-enabled pin)
int potValue = 0;        // Variable to store potentiometer value
int pwmValue = 0;        // Variable to store PWM output

void setup() {
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
}

void loop() {
  potValue = analogRead(potPin);              // Read potentiometer value (0-1023)
  pwmValue = map(potValue, 0, 1023, 0, 255);  // Map value to PWM range (0-255)
  analogWrite(ledPin, pwmValue);              // Write PWM value to LED
  delay(10);                                  // Small delay for stability
}
"""
        }
    },
    "Interfacing Servo Motor": {
        "components": [
            "NodeMCU or Arduino",
            "Servo Motor",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "VCC": "5V",
                "GND": "GND",
                "Control Pin": "PWM Pin (e.g., Pin 9)"
            },
            "NodeMCU": {
                "VCC": "5V",
                "GND": "GND",
                "Control Pin": "PWM Pin (e.g., D2)"
            }
        },
        "code": {
            "Arduino": """
#include <Servo.h>

Servo myServo;  // Create a servo object

void setup() {
  myServo.attach(9); // ARDunio

}

void loop() {
  for (int angle = 0; angle <= 180; angle++) {  // Rotate from 0° to 180°
    myServo.write(angle);  // Move the servo to the specified angle
    delay(15);  // Wait for the servo to reach the position
  }

  for (int angle = 180; angle >= 0; angle--) {  // Rotate back from 180° to 0°
    myServo.write(angle);  // Move the servo to the specified angle
    delay(15);  // Wait for the servo to reach the position
  }
}
""",
            "NodeMCU": """
#include <Servo.h>

Servo myServo;  // Create a servo object

void setup() {
   myServo.attach(D4);

}

void loop() {
  for (int angle = 0; angle <= 180; angle++) {  // Rotate from 0° to 180°
    myServo.write(angle);  // Move the servo to the specified angle
    delay(15);  // Wait for the servo to reach the position
  }

  for (int angle = 180; angle >= 0; angle--) {  // Rotate back from 180° to 0°
    myServo.write(angle);  // Move the servo to the specified angle
    delay(15);  // Wait for the servo to reach the position
  }
}
"""
        }
    },
    "Interfacing LCD": {
        "components": [
            "NodeMCU or Arduino",
            "LCD Display (16x2)",
            "I2C Module",
            "Breadboard",
            "Jumper Wires"
        ],
        "connections": {
            "Arduino": {
                "SDA": "A4",
                "SCL": "A5",
                "VCC": "5V",
                "GND": "GND"
            },
            "NodeMCU": {
                "SDA": "D2",
                "SCL": "D1",
                "VCC": "3.3V",
                "GND": "GND"
            }
        },
        "code": {
            "Arduino": """
#include <Wire.h>
#include <LiquidCrystal.h>

// Initialize the LCD with the pin configuration for parallel connection
LiquidCrystal lcd(12,11,5,4,3,2);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Arduino LCD Demo");
  delay(2000);
  lcd.clear();
}

void loop() {
  lcd.setCursor(0, 0);
  lcd.print("Count: ");
  for (int i = 0; i <= 10; i++) {
    lcd.setCursor(7, 0);
    lcd.print(i);
    delay(500);
    lcd.setCursor(0, 1);
    lcd.print("Time: ");
    lcd.print(millis() / 1000);
    lcd.print(" sec");
  }
}
""",
            "NodeMCU": """
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("NodeMCU LCD Demo");
  delay(2000);
  lcd.clear();
}

void loop() {
  lcd.setCursor(0, 0);
  lcd.print("Count: ");
  for (int i = 0; i <= 10; i++) {
    lcd.setCursor(7, 0);
    lcd.print(i);
    delay(500);
    lcd.setCursor(0, 1);
    lcd.print("Time: ");
    lcd.print(millis() / 1000);
    lcd.print(" sec");
  }
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
    st.write("*Arduino*")
    for pin, connection in experiment["connections"]["Arduino"].items():
        st.write(f"- *{pin}* → {connection}")

with col2:
    st.write("*NodeMCU*")
    for pin, connection in experiment["connections"]["NodeMCU"].items():
        st.write(f"- *{pin}* → {connection}")

st.subheader("Code")

# Tabs for Arduino and NodeMCU code
tabs = st.radio("Select Platform", ["Arduino", "NodeMCU"])

if tabs == "Arduino":
    st.code(experiment["code"]["Arduino"], language="cpp")
else:
    st.code(experiment["code"]["NodeMCU"], language="cpp")
