/* Copyright (C) 2012 Kristian Lauszus, TKJ Electronics. All rights reserved.

 This software may be distributed and modified under the terms of the GNU
 General Public License version 2 (GPL2) as published by the Free Software
 Foundation and appearing in the file GPL2.TXT included in the packaging of
 this file. Please note that GPL2 Section 2[b] requires that all works based
 on this software must also be made publicly available under the terms of
 the GPL2 ("Copyleft").
3a
 Contact information
 -------------------

 Kristian Lauszus, TKJ Electronics
 Web      :  http://www.tkjelectronics.com
 e-mail   :  kristianl@tkjelectronics.com
 */
#include <SD.h>
const int chipSelect = 4;
#include <Wire.h>
#include "Kalman.h" // Source: https://github.com/TKJElectronics/KalmanFilter

Kalman kalmanX; // Create the Kalman instances
Kalman kalmanY;
/* IMU Data */
int16_t accX, accY, accZ;
int16_t tempRaw;
int16_t gyroX, gyroY, gyroZ;
//int16_t Vref, VzeroG , sensitivity;
unsigned long time;
//for 1000 loops,it takes 12secs with the delay of 10 ms.otherwise, it takes 2secs for 1000 loops meaning 2ms for each loop

int counter=0;
double magax,magay, magaz;
double accXangle, accYangle; // Angle calculate using the accelerometer
double temp; // Temperature
double gyroXangle, gyroYangle; // Angle calculate using the gyro
double compAngleX, compAngleY; // Calculate the angle using a complementary filter
double kalAngleX, kalAngleY; // Calculate the angle using a Kalman filter
char accXangles[10], accYangles[10];
char magaxs[10],magays[10], magazs[10];
char temps[10];
char times[10];
char gyroXrates[10], gyroYrates[10], gyroZrates[10];

int sensorPin = A0;

uint32_t timer;
uint8_t i2cData[14]; // Buffer for I2C data

void setup() {
  Serial.begin(9600);
  Wire.begin();
  TWBR = ((F_CPU / 400000L) - 16) / 2; // Set I2C frequency to 400kHz

  i2cData[0] = 7; // Set the sample rate to 1000Hz - 8kHz/(7+1) = 1000Hz
  i2cData[1] = 0x00; // Disable FSYNC and set 260 Hz Acc filtering, 256 Hz Gyro filtering, 8 KHz sampling
  i2cData[2] = 0x15; // Set Gyro Full Scale Range to ±2000deg/s
  i2cData[3] = 0x10; // Set Accelerometer Full Scale Range to ±8g
  while (i2cWrite(0x19, i2cData, 4, false)); // Write to all four registers at once
  while (i2cWrite(0x6B, 0x01, true)); // PLL with X axis gyroscope reference and disable sleep mode

  while (i2cRead(0x75, i2cData, 1));
  if (i2cData[0] != 0x68) { // Read "WHO_AM_I" register
    Serial.print(F("Error reading sensor"));
    while (1);
  }

  delay(100); // Wait for sensor to stabilize

  /* Set kalman and gyro starting angle */
  while (i2cRead(0x3B, i2cData, 6));
  accX = ((i2cData[0] << 8) | i2cData[1]);
  accY = ((i2cData[2] << 8) | i2cData[3]);
  accZ = ((i2cData[4] << 8) | i2cData[5]);
  // atan2 outputs the value of -π to π (radians) - see http://en.wikipedia.org/wiki/Atan2
  // We then convert it to 0 to 2π and then from radians to degrees
 
 
  accYangle = (atan2(accX, accZ) + PI) * RAD_TO_DEG;
  accXangle = (atan2(accY, accZ) + PI) * RAD_TO_DEG;

  kalmanX.setAngle(accXangle); // Set starting angle
  kalmanY.setAngle(accYangle);

  
  gyroXangle = accXangle;
  gyroYangle = accYangle;

  compAngleX = accXangle;
  compAngleY = accYangle;
    

  timer = micros();
  
  Serial.print("Initializing SD card...");
  // make sure that the default chip select pin is set to
  // output, even if you don't use it:
  pinMode(4, OUTPUT);
  
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    return;
  }
  Serial.println("card initialized.");
  
}

void loop() {
  /* Update all the values */
  while (i2cRead(0x3B, i2cData, 14));
  accX = ((i2cData[0] << 8) | i2cData[1]);
  accY = ((i2cData[2] << 8) | i2cData[3]);
  accZ = ((i2cData[4] << 8) | i2cData[5]);
  tempRaw = ((i2cData[6] << 8) | i2cData[7]);
  gyroX = ((i2cData[8] << 8) | i2cData[9]);
  gyroY = ((i2cData[10] << 8) | i2cData[11]);
  gyroZ = ((i2cData[12] << 8) | i2cData[13]);
 time = millis();
int sensorval= analogRead(sensorPin);
 if(sensorval >0)
 {
   counter++;
 }


  // make a string for assembling the data to log:
 String dataString = "";

//counter++;
////time to go through 1000 loops
//if(counter==1000)
//{ time = millis();
//  //prints time since program started
//  Serial.println();
//  Serial.println(time);
// counter= 0; 
//}
  
//Magnitude of the vectors

magax= (accX/4096.0);
magay= (accY/4096.0);
magaz= (accZ/4096.0);

  // atan2 outputs the value of -π to π (radians) - see http://en.wikipedia.org/wiki/Atan2
  // We then convert it to 0 to 2π and then from radians to degrees
  accXangle = (atan2(accY, accZ) + PI) * RAD_TO_DEG;
  accYangle = (atan2(accX, accZ) + PI) * RAD_TO_DEG;
   

  double gyroXrate = (double)gyroX / 16.4; // sensitivity scale factor for 2000degs/sec
    double gyroZrate = (double)gyroZ / 16.4;
  double gyroYrate = -((double)gyroY / 16.4);
  //gyroXangle += gyroXrate * ((double)(micros() - timer) / 1000000); // Calculate gyro angle without any filter
  //gyroYangle += gyroYrate * ((double)(micros() - timer) / 1000000);
   //gyroZangle += gyroZrate * ((double)(micros() - timer) / 1000000);
  //gyroXangle += kalmanX.getRate()*((double)(micros()-timer)/1000000); // Calculate gyro angle using the unbiased rate
  //gyroYangle += kalmanY.getRate()*((double)(micros()-timer)/1000000);
  //gyroZangle += kalmanZ.getRate()*((double)(micros()-timer)/1000000);

  //compAngleX = (0.93 * (compAngleX + (gyroXrate * (double)(micros() - timer) / 1000000))) + (0.07 * accXangle); // Calculate the angle using a Complimentary filter
  //compAngleY = (0.93 * (compAngleY + (gyroYrate * (double)(micros() - timer) / 1000000))) + (0.07 * accYangle);


  //kalAngleX = kalmanX.getAngle(accXangle, gyroXrate, (double)(micros() - timer) / 1000000); // Calculate the angle using a Kalman filter
  //kalAngleY = kalmanY.getAngle(accYangle, gyroYrate, (double)(micros() - timer) / 1000000);
  timer = micros();

  temp = ((double)tempRaw + 12412.0) / 340.0;

  /* Print Data */
/*#if 1 // Set to 1 to activate
  Serial.print(accX); Serial.print("\t");
  Serial.print(accY); Serial.print("\t");
  Serial.print(accZ); Serial.print("\t");

  Serial.print(gyroX); Serial.print("\t");
  Serial.print(gyroY); Serial.print("\t");
  Serial.print(gyroZ); Serial.print("\t");
#endif
*/
/*
  Serial.print(accXangle); Serial.print("\t");
  Serial.print(gyroXangle); Serial.print("\t");
  Serial.print(compAngleX); Serial.print("\t");
  Serial.print(kalAngleX); Serial.print("\t");

  Serial.print("\t");

  Serial.print(accYangle); Serial.print("\t");
  Serial.print(gyroYangle); Serial.print("\t");
  Serial.print(compAngleY); Serial.print("\t");
  Serial.print(kalAngleY); Serial.print("\t");
  */

dtostrf(accXangle,3,3,accXangles);
dtostrf(accYangle,3,3,accYangles);
dtostrf(magax,2,3,magaxs);
dtostrf(magaz,2,3,magazs);
dtostrf(magay,2,3,magays);
dtostrf(gyroXrate,3,3,gyroXrates);
dtostrf(gyroYrate,3,3,gyroYrates);
dtostrf(gyroZrate,3,3,gyroZrates);
dtostrf(time,3,3,times);
dtostrf(temp,3,3,temps);

 if (counter>0)
 {

dataString += String(accXangles);
dataString += String("\t");
dataString += String(accYangles);
dataString += String("\t");
dataString += String(magaxs);
dataString += String("\t");
dataString += String(magays);
dataString += String("\t");
dataString += String(magazs);
dataString += String("\t");
dataString += String(gyroXrates);
dataString += String("\t");
dataString += String(gyroYrates);
dataString += String("\t");
dataString += String(gyroZrates);
dataString += String("\t");
dataString += String(times);
dataString += String("\t");
dataString += String(temps);
dataString += String("\t");



File dataFile = SD.open("datalog.txt", FILE_WRITE);

 if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }  
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  } 
 
 }
//Serial.print(accXangle); Serial.print("\t");
//Serial.print(accYangle); Serial.print("\t");


//Serial.print("\t");

 //Serial.print(gyroXangle); Serial.print("\t");
 //Serial.print(gyroYangle); Serial.print("\t");
 // Serial.print(gyroZangle); Serial.print("\t");

//Serial.print("\t");

 //Serial.print(magX); Serial.print("\t");
 //Serial.print(magY); Serial.print("\t");
 //Serial.print(magZ); Serial.print("\t");
//Each loop has 10ms delay

  //Serial.print(accZ); Serial.print("\t");
 // time = millis();
//prints time since program started
//  Serial.println();

//Serial.print(magax); Serial.print("\t");
//Serial.print(magay); Serial.print("\t");
//Serial.print(magaz); Serial.print("\t");
//Serial.print(gyroXrate); Serial.print("\t");
//Serial.print(gyroYrate); Serial.print("\t");
//Serial.print(gyroZrate); Serial.print("\t");
//Serial.print(time); Serial.print("\t");
//Serial.print(temp);Serial.print("\t");

 
// Serial.print("\r\n");
  delay(18); // values are taken 50times per second with with 2ms loop execution and 18ms delay 
}
