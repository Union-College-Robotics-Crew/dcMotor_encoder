import rotaryio
import board


class Encoder:

    def __init__(self, pin_A, pin_B):
        self.encoder = rotaryio.IncrementalEncoder(pin_A, pin_B)
        self.prev_count = 0

    def __repr__(self):
        return str(self.encoder.position / 3)

    def get_encoder_position(self):
        return self.encoder.position / 3

    def reset_encoder(self, pin_A, pin_B):
        self.encoder = rotariyo.IncrementalEncoder(board.pin_A, board.pin_B)
        self.prev_count = 0

    def count(self):
        cur_count = self.encoder.position / 3
        dif = cur_count - self.prev_count
        self.prev_count = cur_count

        return dif
