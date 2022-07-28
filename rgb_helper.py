import pygame
import sys

def clamp(n):
  if n < 0: return 0
  elif n > 255: return 255
  else: return n

class RGB:

  def __init__(self, red, green, blue):
    self.r = red
    self.g = green
    self.b = blue

  def red(self):
    return self.r

  def green(self):
    return self.g

  def blue(self):
    return self.b

  def adjust_red(self, delta):
    self.r = clamp(self.r + delta)
    
  def adjust_green(self, delta):
    self.g = clamp(self.g + delta)

  def adjust_blue(self, delta):
    self.b = clamp(self.b + delta)

  def tuple(self):
    return (self.r, self.g, self.b)

  def css_string(self):
    return f'rgb({self.r}, {self.g}, {self.b})'

  def html_string(self):
    return '#'+format(self.r, '02X')+format(self.g, '02X')+format(self.b, '02X')

# Dictionary of RGB tuples and their HTML names
# from https://htmlcolorcodes.com/color-names/
named_colors = {
  (240, 248, 255) : 'AliceBlue', 
  (250, 235, 215) : 'AntiqueWhite', 
  (0, 255, 255) : 'Aqua', 
  (127, 255, 212) : 'Aquamarine', 
  (240, 255, 255) : 'Azure', 
  (245, 245, 220) : 'Beige', 
  (255, 228, 196) : 'Bisque', 
  (0, 0, 0) : 'Black', 
  (255, 235, 205) : 'BlanchedAlmond', 
  (0, 0, 255) : 'Blue', 
  (138, 43, 226) : 'BlueViolet', 
  (165, 42, 42) : 'Brown', 
  (222, 184, 135) : 'BurlyWood', 
  (95, 158, 160) : 'CadetBlue', 
  (127, 255, 0) : 'Chartreuse', 
  (210, 105, 30) : 'Chocolate', 
  (255, 127, 80) : 'Coral', 
  (100, 149, 237) : 'CornflowerBlue', 
  (255, 248, 220) : 'Cornsilk', 
  (220, 20, 60) : 'Crimson', 
  (0, 255, 255) : 'Cyan', 
  (0, 0, 139) : 'DarkBlue', 
  (0, 139, 139) : 'DarkCyan', 
  (184, 134, 11) : 'DarkGoldenrod', 
  (169, 169, 169) : 'DarkGray', 
  (0, 100, 0) : 'DarkGreen', 
  (189, 183, 107) : 'DarkKhaki', 
  (139, 0, 139) : 'DarkMagenta', 
  (85, 107, 47) : 'DarkOliveGreen', 
  (255, 140, 0) : 'DarkOrange', 
  (153, 50, 204) : 'DarkOrchid', 
  (139, 0, 0) : 'DarkRed', 
  (233, 150, 122) : 'DarkSalmon', 
  (143, 188, 139) : 'DarkSeaGreen', 
  (72, 61, 139) : 'DarkSlateBlue', 
  (47, 79, 79) : 'DarkSlateGray', 
  (0, 206, 209) : 'DarkTurquoise', 
  (148, 0, 211) : 'DarkViolet', 
  (255, 20, 147) : 'DeepPink', 
  (0, 191, 255) : 'DeepSkyBlue', 
  (105, 105, 105) : 'DimGray', 
  (30, 144, 255) : 'DodgerBlue', 
  (178, 34, 34) : 'FireBrick', 
  (255, 250, 240) : 'FloralWhite', 
  (34, 139, 34) : 'ForestGreen', 
  (255, 0, 255) : 'Fuchsia', 
  (220, 220, 220) : 'Gainsboro', 
  (248, 248, 255) : 'GhostWhite', 
  (255, 215, 0) : 'Gold', 
  (218, 165, 32) : 'Goldenrod', 
  (128, 128, 128) : 'Gray', 
  (0, 128, 0) : 'Green', 
  (173, 255, 47) : 'GreenYellow', 
  (240, 255, 240) : 'HoneyDew', 
  (255, 105, 180) : 'HotPink', 
  (205, 92, 92) : 'IndianRed', 
  (75, 0, 130) : 'Indigo', 
  (255, 255, 240) : 'Ivory', 
  (240, 230, 140) : 'Khaki', 
  (230, 230, 250) : 'Lavender', 
  (255, 240, 245) : 'LavenderBlush', 
  (124, 252, 0) : 'LawnGreen', 
  (255, 250, 205) : 'LemonChiffon', 
  (173, 216, 230) : 'LightBlue', 
  (240, 128, 128) : 'LightCoral', 
  (224, 255, 255) : 'LightCyan', 
  (250, 250, 210) : 'LightGoldenrodYellow', 
  (211, 211, 211) : 'LightGray', 
  (144, 238, 144) : 'LightGreen', 
  (255, 182, 193) : 'LightPink', 
  (255, 160, 122) : 'LightSalmon', 
  (255, 160, 122) : 'LightSalmon', 
  (32, 178, 170) : 'LightSeaGreen', 
  (135, 206, 250) : 'LightSkyBlue', 
  (119, 136, 153) : 'LightSlateGray', 
  (176, 196, 222) : 'LightSteelBlue', 
  (255, 255, 224) : 'LightYellow', 
  (0, 255, 0) : 'Lime', 
  (50, 205, 50) : 'LimeGreen', 
  (250, 240, 230) : 'Linen', 
  (255, 0, 255) : 'Magenta', 
  (128, 0, 0) : 'Maroon', 
  (102, 205, 170) : 'MediumAquamarine', 
  (0, 0, 205) : 'MediumBlue', 
  (186, 85, 211) : 'MediumOrchid', 
  (147, 112, 219) : 'MediumPurple', 
  (60, 179, 113) : 'MediumSeaGreen', 
  (123, 104, 238) : 'MediumSlateBlue', 
  (123, 104, 238) : 'MediumSlateBlue', 
  (0, 250, 154) : 'MediumSpringGreen', 
  (72, 209, 204) : 'MediumTurquoise', 
  (199, 21, 133) : 'MediumVioletRed', 
  (25, 25, 112) : 'MidnightBlue', 
  (245, 255, 250) : 'MintCream', 
  (255, 228, 225) : 'MistyRose', 
  (255, 228, 181) : 'Moccasin', 
  (255, 222, 173) : 'NavajoWhite', 
  (0, 0, 128) : 'Navy', 
  (253, 245, 230) : 'OldLace', 
  (128, 128, 0) : 'Olive', 
  (107, 142, 35) : 'OliveDrab', 
  (255, 165, 0) : 'Orange', 
  (255, 69, 0) : 'OrangeRed', 
  (218, 112, 214) : 'Orchid', 
  (238, 232, 170) : 'PaleGoldenrod', 
  (152, 251, 152) : 'PaleGreen', 
  (175, 238, 238) : 'PaleTurquoise', 
  (219, 112, 147) : 'PaleVioletRed', 
  (255, 239, 213) : 'PapayaWhip', 
  (255, 218, 185) : 'PeachPuff', 
  (205, 133, 63) : 'Peru', 
  (255, 192, 203) : 'Pink', 
  (221, 160, 221) : 'Plum', 
  (176, 224, 230) : 'PowderBlue', 
  (128, 0, 128) : 'Purple', 
  (102, 51, 153) : 'RebeccaPurple', 
  (255, 0, 0) : 'Red', 
  (188, 143, 143) : 'RosyBrown', 
  (65, 105, 225) : 'RoyalBlue', 
  (139, 69, 19) : 'SaddleBrown', 
  (250, 128, 114) : 'Salmon', 
  (244, 164, 96) : 'SandyBrown', 
  (46, 139, 87) : 'SeaGreen', 
  (255, 245, 238) : 'SeaShell', 
  (160, 82, 45) : 'Sienna', 
  (192, 192, 192) : 'Silver', 
  (135, 206, 235) : 'SkyBlue', 
  (106, 90, 205) : 'SlateBlue', 
  (112, 128, 144) : 'SlateGray', 
  (255, 250, 250) : 'Snow', 
  (0, 255, 127) : 'SpringGreen', 
  (70, 130, 180) : 'SteelBlue', 
  (210, 180, 140) : 'Tan', 
  (0, 128, 128) : 'Teal', 
  (216, 191, 216) : 'Thistle', 
  (255, 99, 71) : 'Tomato', 
  (64, 224, 208) : 'Turquoise', 
  (238, 130, 238) : 'Violet', 
  (245, 222, 179) : 'Wheat', 
  (255, 255, 255) : 'White', 
  (245, 245, 245) : 'WhiteSmoke', 
  (255, 255, 0) : 'Yellow', 
  (154, 205, 50) : 'YellowGreen'
}

# Your code must init pygame before using it
pygame.init()

# win refers to the window that will pop up on the screen
win = pygame.display.set_mode((400, 300))

# Title of the window
pygame.display.set_caption('RGB Helper')

# Start with the color black
current_color = RGB(0, 0, 0)

def run():
  # Setting the font
  appFont = pygame.font.SysFont('ubuntu', 18)

  # Create a rectangle that displays the text of the red value
  redText = appFont.render(str(current_color.r)+' red', True, (0, 0, 0), (255, 255, 255))
  redRect = pygame.Rect(30, 20, 100, 30)
  
  # Similarly, create a rectangle for the green and blue values
  greenText = appFont.render(str(current_color.g)+' green', True, (0, 0, 0), (255, 255, 255))
  greenRect = pygame.Rect(30, 70, 100, 30)

  blueText = appFont.render(str(current_color.b)+' blue', True, (0, 0, 0), (255, 255, 255))
  blueRect = pygame.Rect(30, 120, 100, 30)

  cssText = appFont.render(current_color.css_string(), True, (0, 0, 0), (255, 255, 255))
  cssRect = pygame.Rect(130, 170, 100, 30)

  htmlText = appFont.render(current_color.html_string(), True, (0, 0, 0), (255, 255, 255))
  htmlRect = pygame.Rect(130, 200, 100, 30)
  
  # This is used to display the name of the color if the RGB tuple matches a 
  # named color in the named_colors dictionary
  if current_color.tuple() in named_colors:
    colorNameText = appFont.render(named_colors[current_color.tuple()], True, (0, 0, 0), (255, 255, 255))
  else:
    colorNameText = appFont.render('(unnamed)', True, (0, 0, 0), (255, 255, 255))
  colorNameRect = pygame.Rect(130, 230, 100, 30)
  
  # swatchRect is the rectangle that displays the chosen RGB color on the screen
  swatchRect = pygame.Rect(150, 20, 200, 120)

  # This is the events loop
  for event in pygame.event.get():
    # Check if the user has clicked the X sign to exit
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # Check if the user has typed a letter
    elif event.type == pygame.KEYDOWN:
      # If the user types the letter 'r', increase the red value by 1
      if event.key == pygame.K_r:
        current_color.adjust_red(1)
      # If the user types the letter 't', increase the red value by 8
      elif event.key == pygame.K_t:
        current_color.adjust_red(8)
      elif event.key == pygame.K_e:
        current_color.adjust_red(-1)
      elif event.key == pygame.K_w:
        current_color.adjust_red(-8)
      elif event.key == pygame.K_g:
        current_color.adjust_green(1)
      elif event.key == pygame.K_h:
        current_color.adjust_green(8)
      elif event.key == pygame.K_f:
        current_color.adjust_green(-1)
      elif event.key == pygame.K_d:
        current_color.adjust_green(-8)
      elif event.key == pygame.K_b:
        current_color.adjust_blue(1)
      elif event.key == pygame.K_n:
        current_color.adjust_blue(8)
      elif event.key == pygame.K_v:
        current_color.adjust_blue(-1)
      elif event.key == pygame.K_c:
        current_color.adjust_blue(-8)
      elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
      
  # Fill in the window with a white background
  win.fill((255, 255, 255))

  # Use blit to display text onto a rectange
  win.blit(redText, redRect)
  win.blit(greenText, greenRect)
  win.blit(blueText, blueRect)
  win.blit(cssText, cssRect)
  win.blit(htmlText, htmlRect)
  win.blit(colorNameText, colorNameRect)
  
  # Draw the rectangles onto the window
  pygame.draw.rect(win, (0, 0, 0), redRect, width=1)
  pygame.draw.rect(win, (0, 0, 0), greenRect, width=1)
  pygame.draw.rect(win, (0, 0, 0), blueRect, width=1)
  pygame.draw.rect(win, (255, 255, 255), cssRect, width=1)
  pygame.draw.rect(win, (255, 255, 255), htmlRect, width=1)
  pygame.draw.rect(win, (255, 255, 255), colorNameRect, width=1)
  pygame.draw.rect(win, current_color.tuple(), swatchRect)

  # Update the pygame display
  pygame.display.update()

while True:
  run()
  
