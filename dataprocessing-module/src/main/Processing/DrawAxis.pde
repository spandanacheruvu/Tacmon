void drawAxisX() {
  /* Draw gyro x-axis */
  noFill();
  stroke(255,255,0); // Yellow
  // Redraw everything
  beginShape();
  for(int i = 0; i<gyroX.length;i++)
    vertex(i,gyroX[i]+100);
  endShape();
  // Put all data one array back
  for(int i = 1; i<gyroX.length;i++)
    gyroX[i-1] = gyroX[i];   
   
  /* Draw acceleromter x-axis */
  noFill();
  stroke(0,255,0); // Green
  // Redraw everything
  beginShape();
  for(int i = 0; i<accX.length;i++)
    vertex(i,accX[i]+100);  
  endShape();
  // Put all data one array back
  for(int i = 1; i<accX.length;i++)
    accX[i-1] = accX[i];   
   
  /* Draw complementary filter x-axis */
  /* noFill();
  stroke(0,0,255); // Blue
  // Redraw everything
  beginShape();
  for(int i = 0; i<compX.length;i++)
    vertex(i,compX[i]+100);
  endShape();
  // Put all data one array back
  for(int i = 1; i<compX.length;i++)
    compX[i-1] = compX[i];  
   */
  /* Draw kalman filter x-axis */
/*  noFill();
  stroke(255,0,0);// Red
  // Redraw everything
  beginShape();
  for(int i = 0; i<kalmanX.length;i++)
    vertex(i,kalmanX[i]+100);  
  endShape();
  // Put all data one array back
  for(int i = 1; i<kalmanX.length;i++)
    kalmanX[i-1] = kalmanX[i]; */
}

void drawAxisY() {
  /* Draw gyro y-axis */
  noFill();
  stroke(0,0,255); // Blue
  // Redraw everything
  beginShape();
  for(int i = 0; i<gyroY.length;i++)
    vertex(i,gyroY[i]+200);
  endShape();
  // Put all data one array back
  for(int i = 1; i<gyroY.length;i++)
   gyroY[i-1] = gyroY[i];
   
  /* Draw acceleromter y-axis */
  noFill();
  stroke(255,0,0); // Red
  // Redraw everything
  beginShape();
  for(int i = 0; i<accY.length;i++)
    vertex(i,accY[i]+200);
  endShape();
  // Put all data one array back
  for(int i = 1; i<accY.length;i++)
    accY[i-1] = accY[i];
   
  /* Draw complementary filter y-axis */
  /*noFill();
  stroke(0,255,255); // Blue
  // Redraw everything
  beginShape();
  for(int i = 0; i<compY.length;i++)
    vertex(i,compY[i]+200);
  endShape();
  // Put all data one array back
  for(int i = 1; i<compY.length;i++)
    compY[i-1] = compY[i];
  */
  /* Draw kalman filter y-axis */
 /* noFill();
  stroke(255,0,0); // Red
  // Redraw everything
  beginShape();
  for(int i = 0; i<kalmanY.length;i++)
    vertex(i,kalmanY[i]+200);
  endShape();
  // Put all data one array back
  for(int i = 1; i<kalmanY.length;i++)
    kalmanY[i-1] = kalmanY[i];
    */
}    

void drawAxisZ() {
  /* Draw gyro z-axis */
  noFill();
  stroke(0,255,255); // Purple?
  // Redraw everything
  beginShape();
  for(int i = 0; i<gyroZ.length;i++)
    vertex(i,gyroZ[i]+200);
  endShape();
  // Put all data one array back
  for(int i = 1; i<gyroZ.length;i++)
   gyroZ[i-1] = gyroZ[i];
   
  /* Draw acceleromter z-axis */
  noFill();
  stroke(255,0,255); // Pink
  // Redraw everything
  beginShape();
  for(int i = 0; i<accZ.length;i++)
    vertex(i,accZ[i]+200);
  endShape();
  // Put all data one array back
  for(int i = 1; i<accZ.length;i++)
    accZ[i-1] = accZ[i];
}
