class Guest:

    def __init__(self, name, celebration, status, wallet, favourite_song):
        self.name = name
        self.celebration = celebration
        self.status = status
        self.wallet = wallet
        self.favourite_song = favourite_song
    
    def pay_fee(self, room):
        if self.status == "VIP":
            self.wallet -= room.vip_fee
            room.till += room.vip_fee
        else:
            self.wallet -= room.regular_fee
            room.till += room.regular_fee