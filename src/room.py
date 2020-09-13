class Room:

    def __init__(self, name, regular_fee, vip_fee, till):
        self.name = name
        self.regular_fee = regular_fee
        self.vip_fee = vip_fee
        self.till = till
        self.vip_guest = []
        self.regular_guest = []
        self.songs = []
        self.waiting_line = 0
    
    def add_guest(self, guest):

        if guest.status == "VIP":
            self.vip_guest.append(guest)
        else:
            self.regular_guest.append(guest)
    
    def check_out_guest(self, guest):
        if guest.status == "VIP":
            self.vip_guest.remove(guest)
        else:
            self.regular_guest.remove(guest)
    
    def add_songs(self, song):
        self.songs.append(song)
    
    def restrict_guest(self, guest): 
        if guest.status == "VIP":
            if len(self.vip_guest) >= 5:
                self.waiting_line = len(self.vip_guest) - 5
                #  raise Exception(' Maximum number allowed is 5')
            else:
                self.vip_guest.append(guest)  
        else:
            if len(self.regular_guest) >= 5:
                self.waiting_line = len(self.regular_guest) - 5
            else:
                self.regular_guest.append(guest)    
    
    def guest_can_afford(self, guest):
        outcome = False
        if guest.status == "VIP":
            if guest.wallet >= self.vip_fee:
                guest.pay_fee(self)
                outcome = True
        return outcome
    
    def guest_can_find_song(self, music_artist):
        for song in self.songs:
            if song.artist == music_artist:
                return song.name
    
    def play_song(self, guest):
        for song in self.songs:
            if song.name == guest.favourite_song:
                return guest.celebration
            else:
                return "Nahhh"
    
    def add_drink(self, drink):
        drink["quantity"] += 1
    
    def remove_drink(self, drink):
        drink["quantity"] -= 1
    
    def sell_drink(self, guest, drink):
        self.remove_drink(drink)
        guest.wallet -= drink["Drink"].price
        self.till += drink["Drink"].price
