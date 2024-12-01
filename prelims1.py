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
int irPin = 7;

void setup() {
  pinMode(irPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int irState = digitalRead(irPin);
  Serial.println(irState ? "Object Detected" : "No Object");
  delay(100);
}
""",
            "NodeMCU": """
int irPin = D2;

void setup() {
  pinMode(irPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int irState = digitalRead(irPin);
  Serial.println(irState ? "Object Detected" : "No Object");
  delay(100);
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
int potPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);
  Serial.print("Potentiometer Value: ");
  Serial.println(potValue);
  delay(500);
}
""",
            "NodeMCU": """
int potPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);
  Serial.print("Potentiometer Value: ");
  Serial.println(potValue);
  delay(500);
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

Servo myServo;
int servoPin = 9;

void setup() {
  myServo.attach(servoPin);
}

void loop() {
  myServo.write(0); // Move to 0 degrees
  delay(1000);
  myServo.write(90); // Move to 90 degrees
  delay(1000);
  myServo.write(180); // Move to 180 degrees
  delay(1000);
}
""",
            "NodeMCU": """
#include <Servo.h>

Servo myServo;
int servoPin = D2;

void setup() {
  myServo.attach(servoPin);
}

void loop() {
  myServo.write(0); // Move to 0 degrees
  delay(1000);
  myServo.write(90); // Move to 90 degrees
  delay(1000);
  myServo.write(180); // Move to 180 degrees
  delay(1000);
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
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

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
