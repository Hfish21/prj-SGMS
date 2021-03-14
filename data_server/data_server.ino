/////////////////////////////////////////////////////////////////
//         ESP32 Web Server Project  v1.00                     //
//       Get the latest version of the code here:              //
//         http://educ8s.tv/esp32-web-server                   //
/////////////////////////////////////////////////////////////////


#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>  //https://github.com/bbx10/WebServer_tng
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)

WebServer server ( 80 );
Adafruit_BMP280 bmp;

const char* ssid     = "Fishy-Fi";
const char* password = "fishfi2019";


void setup() {

  //initializeSensor();
  connectToWifi();
  beginServer();

}

void loop() {
  server.handleClient();
  delay(1000);
}

void connectToWifi() {
  WiFi.enableSTA(true);

  delay(2000);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      //Serial.print(".");
  }

}

void beginServer() {
  server.on ( "/", handleRoot);
  server.begin();
}

void handleRoot(){
  /*
  String temp = String(bmp.readTemperature());
  String pressure = String(bmp.readPressure());

  String msg = "<h1>Temperature: " + temp + " F</h1>";
  msg += "<h1>Pressure: " + pressure + " Pa</h1>";
  */
  server.send ( 200, "text/html", "hello" );

}
