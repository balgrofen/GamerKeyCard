
#active buzzer setup
buzzer = Pin(33, Pin.OUT)
buzzer.value(0)
def beep(duration_ms=200):
    buzzer.value(1)  # Turn buzzer on
    sleep_ms(duration_ms)
    buzzer.value(0)  # Turn buzzer off
 
# user setup with card IDs
rfid_name = ["Simi",
             "Guba",]
rfid_uid = ["0x03b69831",
            "0x13162606"]

def get_username(uid):
    index = 0
    try:
        index = rfid_uid.index(uid)
        return rfid_name[index]
    except:
        index = -1
        print("RFID is not recognized")
        return 0

def w84crd(): #Wait for card method shows constantly when there are no cards present
    display.fill(0)
    image_choice_bullet_off_bits = bytearray(b'\x00?\xf0\x00\x00?\xf0\x00\x03\xf0?\x00\x03\xf0?\x00\x0f\x00\x03\xc0\x0f\x00\x03\xc0<\x00\x00\xf0<\x00\x00\xf00\x00\x0000\x00\x000\xf0\x00\x00<\xf0\x00\x00<\xc0\x00\x00\x0c\xc0\x00\x00\x0c\xc0\x00\x00\x0c\xc0\x00\x00\x0c\xc0\x00\x00\x0c\xc0\x00\x00\x0c\xf0\x00\x00<\xf0\x00\x00<0\x00\x0000\x00\x000<\x00\x00\xf0<\x00\x00\xf0\x0f\x00\x03\xc0\x0f\x00\x03\xc0\x03\xf0?\x00\x03\xf0?\x00\x00?\xf0\x00\x00?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    fb_image_choice_bullet_off_bits = framebuf.FrameBuffer(image_choice_bullet_off_bits, 30, 32, framebuf.MONO_HLSB)
    display.blit(fb_image_choice_bullet_off_bits, 88, 22)

    display.text("Varom a", 8, 27, 1)

    display.text("Szolnoki Gamer", 7, 4, 1)

    display.text("Kartyat", 8, 39, 1)

    display.show()

def approved(name): #approved method gets a string that will show on the name field
    display.fill(0)
    image_choice_right_bits = bytearray(b'\x00\x0f\xf0\x00\x00\x0f\xf0\x00\x00\xf0\x0f\x00\x00\xf0\x0f\x00\x03\x03\xc0\xc0\x03\x03\xc0\xc0\x0c<<0\x0c<<00\xc0\x03\x0c0\xc0\x03\x0c3\x00\x00\xcc3\x00\x00\xcc\xc3\x00\x0c\xc3\xc3\x00\x0c\xc3\xcc003\xcc003\xcc\x0c\xc03\xcc\x0c\xc03\xc3\x03\x00\xc3\xc3\x03\x00\xc33\x00\x00\xcc3\x00\x00\xcc0\xc0\x03\x0c0\xc0\x03\x0c\x0c<<0\x0c<<0\x03\x03\xc0\xc0\x03\x03\xc0\xc0\x00\xf0\x0f\x00\x00\xf0\x0f\x00\x00\x0f\xf0\x00\x00\x0f\xf0\x00')

    display.text("Bejohetsz", 8, 27, 1)

    display.text("Szolnoki Gamer", 7, 4, 1)
    display.text(name, 8, 39, 1) #eleg csak a valtozot atadni majd 

    fb_image_choice_right_bits = framebuf.FrameBuffer(image_choice_right_bits, 32, 32, framebuf.MONO_HLSB)
    display.blit(fb_image_choice_right_bits, 87, 21)

    display.show()
    sleep(2)


def denied(): # denied screen when the card is not recognised
    display.fill(0)
    image_download_bits = bytearray(b'\x00\xff\xfc\x00\x00\xff\xfc\x00\x03\x00\x03\x00\x03\x00\x03\x00\x0c?\xf0\xc0\x0c?\xf0\xc00\xc0\x0c00\xc0\x0c0\xc3\x00\x03\x0c\xc3\x00\x03\x0c\xcc00\xcc\xcc00\xcc\xcc\x0c\xc0\xcc\xcc\x0c\xc0\xcc\xcc\x03\x00\xcc\xcc\x03\x00\xcc\xcc\x0c\xc0\xcc\xcc\x0c\xc0\xcc\xcc00\xcc\xcc00\xcc\xc3\x00\x03\x0c\xc3\x00\x03\x0c0\xc0\x0c00\xc0\x0c0\x0c?\xf0\xc0\x0c?\xf0\xc0\x03\x00\x03\x00\x03\x00\x03\x00\x00\xff\xfc\x00\x00\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    display.text("Gamerbol", 8, 27, 1)

    display.text("Szolnoki Gamer", 7, 4, 1)

    display.text("Kitiltva", 8, 39, 1)

    fb_image_download_bits = framebuf.FrameBuffer(image_download_bits, 30, 32, framebuf.MONO_HLSB)
    display.blit(fb_image_download_bits, 87, 21)

    display.show()
    sleep(2)
    
# Start web server in a background thread
_thread.start_new_thread(webpage.start, ())
    

while True:
    w84crd() #showing the main screen
    (stat, tag_type) = rdr.request(rdr.REQIDL) #checking for idle cards
    if stat == rdr.OK: # if card scanned
        (stat, raw_uid) = rdr.anticoll() #check for collision
        if stat == rdr.OK: #if there is no collision 
            card_id = "0x%02x%02x%02x%02x" %(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]) #reading the card id
            username =get_username(card_id) #checking against users
            beep()
            if username != 0: #if a user is found get_username did not return zero show approved screen with username
                approved(username)
            else: #if the user is not found (get_username returned zero) show the denied screen
                denied()