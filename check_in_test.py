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
print("place card")
while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "0x%02x%02x%02x%02x" %(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            username =get_username(card_id)
            if username != 0:
                print(f'Welcome {username}')
            else:
                print(" Access Denied! ")