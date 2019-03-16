#include <SPI.h>
#include <Wire.h>
#include <time.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SSD1306_LCDWIDTH 128
#define SSD1306_LCDHEIGHT 64
Adafruit_SSD1306 display(128, 64);

void setup()   {     
  Serial.begin(115200);
  
  display.begin(SSD1306_SWITCHCAPVCC, 0x3c, false);  // initialize with the I2C addr 0x3D (for the 128x64)
  display.setTextSize(1);
  display.setTextColor(WHITE);
}

static int run = 0;
static int start = 0;

void loop() {  
  display.clearDisplay();

  run++;
  
  display.setCursor(0, 0);
  display.printf("CLT2019 %i Arduino", run);

  int i = 0;
  
  for (int y=8 ; y<56 ; y+=8) {
      for (int x=0 ; x<119 ; x+=8) {
          display.setCursor(x, y);
          display.printf("%c", '0' + (((run + i) * 17) % 36));
          i++;
      }
  }    

  display.display();
}
