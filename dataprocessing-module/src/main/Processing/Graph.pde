import processing.serial.*; 
Serial serial; 

String  accXangle, accYangle, accZangle;
String gyroXangle, gyroYangle, gyroZangle;
//String stringCompX, stringCompY;
//String stringKalmanX, stringKalmanY;

final int width = 1000;
final int height = 680;

float[] gyroX = new float[width];
float[] gyroY = new float[width];
float[] gyroZ = new float[width];

float[] accX = new float[width];
float[] accY = new float[width];
float[] accZ = new float[width];

/*float[] compX = new float[width];
float[] compY = new float[width];

float[] kalmanX = new float[width];
float[] kalmanY = new float[width];
*/
boolean drawValues;

void setup() {  
  size(width, height);
  println(Serial.list()); // Use this to print connected serial devices
  serial = new Serial(this, Serial.list()[0], 115200);
  serial.bufferUntil('\n'); // Buffer until line feed

  for (int i=0;i<width;i++) { // center all variables
    gyroX[i] = height/2;
    gyroY[i] = height/2;
    accX[i] = height/2;
    accY[i] = height/2;
     gyroZ[i] = height/2;
    accZ[i] = height/2;
    //compX[i] = height/2;
    //compY[i] = height/2; 
    //kalmanX[i] = height/2;
    //kalmanY[i] = height/2;
  }
  
  drawGraph(); // Draw graph at startup
}

void draw() {
  /* Draw Graph */
  if(drawValues) {
    drawValues = false;
    drawGraph();
  }
}

void drawGraph() {
  background(255); // white  
  for (int i = 0;i<width;i++) {
    stroke(200); // gray
   // line(i*10, 0, i*10, height);
   // line(0, i*10, width, i*10);
  }
  
  stroke(0); // black
  for (int i = 1; i <= 3; i++)
    line(0, height/4*i, width, height/4*i); // Draw line, indicating 90 deg, 180 deg, and 270 deg
  
  convert();
  drawAxisX();
  drawAxisY();
  drawAxisZ();
}

void serialEvent (Serial serial) {
  // Get the ASCII strings:  
  accXangle = serial.readStringUntil('\t');
  accYangle = serial.readStringUntil('\t');
  accZangle = serial.readStringUntil('\t');
 
  
  serial.readStringUntil('\t'); // Ignore extra tab
  
  gyroXangle = serial.readStringUntil('\t');
  gyroYangle = serial.readStringUntil('\t');
 gyroZangle = serial.readStringUntil('\t');
  //stringKalmanY = serial.readStringUntil('\t');
  
  serial.clear(); // Clear buffer
  drawValues = true; // Draw the graph

  //printAxis(); // Used for debugging
}

void printAxis() {
  print(accXangle);
 print(accYangle);
  print(accZangle);
  
  
  print('\t');
  
  print(gyroXangle);
  print(gyroYangle);
  print(gyroZangle);
//print(stringKalmanY);
  
  println();
}
