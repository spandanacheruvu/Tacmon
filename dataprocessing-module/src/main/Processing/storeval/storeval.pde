import processing.serial.*; 
Serial serial; 

String  magax,magay,magaz;
String accXang, accYang;
String gyroXrate, gyroYrate, gyroZrate;
String time , temp;

PrintWriter output;
final int width = 1000;
final int height = 680;

boolean drawValues;

void setup() {  

  println(Serial.list()); // Use this to print connected serial devices
  serial = new Serial(this, Serial.list()[0], 115200);
  serial.bufferUntil('\n'); // Buffer until line feed

   output = createWriter("sudhamanisitting.txt");
  
 // drawGraph(); // Draw graph at startup
}

void draw() {
  /* Draw Graph */
  if(drawValues) {
    drawValues = false;
  // drawGraph();
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
  

}

void serialEvent (Serial serial) {
  // Get the ASCII strings:  
  
  accXang = serial.readStringUntil('\t');
  accYang = serial.readStringUntil('\t');
  magax = serial.readStringUntil('\t');
  magay = serial.readStringUntil('\t');
  magaz = serial.readStringUntil('\t');
 

  
  gyroXrate = serial.readStringUntil('\t');
  gyroYrate = serial.readStringUntil('\t');
 gyroZrate = serial.readStringUntil('\t');
  //stringKalmanY = serial.readStringUntil('\t');
  time = serial.readStringUntil('\t');
  temp = serial.readStringUntil('\t');
  serial.clear(); // Clear buffer

  printAxis(); // Used for debugging
}

void printAxis() {
  
  output.print(accXang ); 
     output.print(accYang) ; 
   output.print(magax ); 
     output.print(magay ) ; 
   output.print(magaz )  ;
   output.print(gyroXrate );
   output.print(gyroYrate );
   output.print(gyroZrate );
   output.print(time );
   output.print(temp );
   output.print(";" );
 

 
}

void keyPressed(){
   output.flush();   
  output.close();
  exit();
}
