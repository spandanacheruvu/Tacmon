




//convert all axis
final int minAngle = 0;
final int maxAngle = 360;

void convert() {
  /* Convert the gyro x-axis */
  if (gyroXangle != null) {
    // Trim off any whitespace:
    gyroXangle = trim(gyroXangle);
    // Convert to an float and map to the screen height, then save in buffer:    
    gyroX[gyroX.length-1] = map(float(gyroXangle), minAngle, maxAngle, 0, height);
  }
  
  /* Convert the gyro y-axis */
  if (gyroYangle != null) {    
    // Trim off any whitespace:
    gyroXangle = trim(gyroXangle);
    // Convert to an float and map to the screen height, then save in buffer:   
    gyroY[gyroY.length-1] = map(float(gyroYangle), minAngle, maxAngle, 0, height);
  }
   /* Convert the gyro z-axis */
  if (gyroZangle != null) {    
    // Trim off any whitespace:
    gyroZangle = trim(gyroZangle);
    // Convert to an float and map to the screen height, then save in buffer:   
    gyroZ[gyroZ.length-1] = map(float(gyroZangle), minAngle, maxAngle, 0, height);
  }


  
  /* Convert the accelerometer x-axis */
  if (accXangle != null) {
    // Trim off any whitespace:
    accXangle = trim(accXangle);
    // Convert to an float and map to the screen height, then save in buffer:    
    accX[accX.length-1] = map(float(accXangle), minAngle, maxAngle, 0, height);
  }
  
  /* Convert the accelerometer y-axis */
  if (accYangle != null) {
    // Trim off any whitespace:
    accYangle = trim(accYangle);
    // Convert to an float and map to the screen height, then save in buffer:        
    accY[accY.length-1] = map(float(accYangle), minAngle, maxAngle, 0, height);
  }
     /* Convert the accelerometer z-axis */
  if (accZangle != null) {
    // Trim off any whitespace:
    accZangle = trim(accZangle);
    // Convert to an float and map to the screen height, then save in buffer:        
    accZ[accZ.length-1] = map(float(accZangle), minAngle, maxAngle, 0, height);
  }

  /* Convert the complementary filter x-axis 
     if (stringCompX != null) {
    // Trim off any whitespace:
    stringCompX = trim(stringCompX);
    // Convert to an float and map to the screen height, then save in buffer:    
    compX[compX.length-1] = map(float(stringCompX), minAngle, maxAngle, 0, height);
  }
  */
  /* Convert the complementary filter y-axis 
  if (stringCompY != null) {
    // Trim off any whitespace:
    stringCompY = trim(stringCompY);
    // Convert to an float and map to the screen height, then save in buffer:    
    compY[compY.length-1] = map(float(stringCompY), minAngle, maxAngle, 0, height);
  */
  
  /* Convert the complementary filter z-axis 
  if (stringCompY != null) {
    // Trim off any whitespace:
    stringCompY = trim(stringCompY);
    // Convert to an float and map to the screen height, then save in buffer:    
    compY[compY.length-1] = map(float(stringCompY), minAngle, maxAngle, 0, height);

 
  }*/
  
  /* Convert the kalman filter x-axis 
  if (stringKalmanX != null) {
    // Trim off any whitespace:
    stringKalmanX = trim(stringKalmanX);
    // Convert to an float and map to the screen height, then save in buffer:    
    kalmanX[kalmanX.length-1] = map(float(stringKalmanX), minAngle, maxAngle, 0, height);
  }
  */
  /* Convert the kalman filter y-axis 
  if (stringKalmanY != null) {
    // Trim off any whitespace:
    stringKalmanY = trim(stringKalmanY);
    // Convert to an float and map to the screen height, then save in buffer:    
    kalmanY[kalmanY.length-1] = map(float(stringKalmanY), minAngle, maxAngle, 0, height);
 */
 /* Convert the kalman filter y-axis 
  if (stringKalmanY != null) {
    // Trim off any whitespace:
    stringKalmanY = trim(stringKalmanY);
    // Convert to an float and map to the screen height, then save in buffer:    
    kalmanY[kalmanY.length-1] = map(float(stringKalmanY), minAngle, maxAngle, 0, height);
*/
  }
