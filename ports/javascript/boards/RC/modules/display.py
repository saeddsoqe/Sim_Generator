from micropython import const
import framebuf
#from machine import Pin, I2C
import utime
import math
import cdisplay


buffer = bytearray(20)

#replace show (H/W) with valid (S/W)
def raw(data):
    import cdisplay
    cdisplay.raw(data)

def clear(c):
    global buffer
    buffer[0] = 6
    buffer[1] = 0
    buffer[2] = 0
    buffer[3] = 0
    buffer[4] = 0
    buffer[5] = 0
    buffer[6] = 0
    buffer[7] = 0
    buffer[8] = 0
    buffer[9] = 0
    raw(buffer)

def fill(c):
    global buffer
    buffer[0] = 7
    buffer[1] = 0
    buffer[2] = 0
    buffer[3] = 0
    buffer[4] = 0
    buffer[5] = 0
    buffer[6] = 0
    buffer[7] = 0
    buffer[8] = 0
    buffer[9] = 0
    raw(buffer)

def pixel(x, y, c):
    global buffer
    fbuff.pixel(x, y, c)
    raw(buffer)

def scroll(dx, dy):
    global buffer
    fbuff.scroll(dx, dy)
    raw(buffer)

def text(string, x, y, c=1):
    global buffer
    # e_string=string.encode()
    for i in range(0,len(string)):
        buffer[8+i]=ord(string[i])
    buffer[0] = 4
    buffer[1] = 0
    buffer[2] = x
    buffer[3] = y
    buffer[4] = 0
    buffer[5] = 0
    buffer[6] = 0
    buffer[7] = 0
    raw(buffer)

def scroll(string,y, c=1):
    global buffer
    for i in range(0,len(string)):
        buffer[8+i]=ord(string[i])
    buffer[0] = 5
    buffer[1] = 0
    buffer[2] = 0
    buffer[3] = y
    buffer[4] = 0
    buffer[5] = 0
    buffer[6] = 0
    buffer[7] = 0
    raw(buffer)

def hline(x, y, w, c):
    global buffer
    fbuff.hline(x, y, w, c)
    raw(buffer)

def vline(x, y, h, c):
    global buffer
    fbuff.vline(x, y, h, c)
    raw(buffer)

def line(x1, y1, x2, y2, c):
    global buffer
    buffer[0] = 0
    buffer[1] = 0
    buffer[2] = x1
    buffer[3] = y1
    buffer[4] = x2
    buffer[5] = y2
    buffer[6] = 0
    buffer[7] = 0
    buffer[8] = 0
    raw(buffer)

def rect(x, y, w, h, c):
    global buffer
    buffer[0] = 1
    buffer[1] = c
    buffer[2] = x
    buffer[3] = y
    buffer[4] = 0
    buffer[5] = 0
    buffer[6] = 0
    buffer[7] = 0
    buffer[8] = w
    buffer[9] = h
    raw(buffer)

#================= this section under Development========================
#created and ported by Saeed Desouky 
#=====================start of circle==================
#empty circle 
def circle(x,y,r,c): 
    global buffer
    buffer[0] = 2
    buffer[1] = c
    buffer[2] = x
    buffer[3] = y
    buffer[4] = 0
    buffer[5] = 0
    buffer[6] = 0
    buffer[7] = 0
    buffer[8] = r
    raw(buffer)
#=====================End of circle==================


#empty triangle 
def triangle(x1,y1,x2,y2,x3,y3,c): # Draw outline triangle (empty)
    global buffer
    buffer[0] = 3
    buffer[1] = c
    buffer[2] = x1
    buffer[3] = y1
    buffer[4] = x2
    buffer[5] = y2
    buffer[6] = x3
    buffer[7] = y3
    buffer[8] = 0
    buffer[9] = 0
    raw(buffer)

# ============== End of Triangles Code ===============

# fill(0)
raw(buffer)



