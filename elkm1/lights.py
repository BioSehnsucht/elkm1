"""Definition of an ElkM1 Light"""

from .const import Max, TextDescriptions
from .elements import Element, Elements
from .message import add_message_handler, ps_encode, pc_encode, pf_encode, \
                     pn_encode, pt_encode


class Light(Element):
    """Class representing a Light"""
    def __init__(self, index, elk):
        super().__init__(index, elk)
        self.status = 0

    def turn_off(self):
        """(Helper) Turn off light"""
        self._elk.send(pf_encode(self._index))

    def turn_on(self, brightness=100, time=0):
        """(Helper) Turn on light"""
        if brightness == 100:
            self._elk.send(pn_encode(self._index))
        else:
            self._elk.send(pc_encode(self._index, 9, brightness, time))

    def toggle(self):
        """(Helper) Toggle light"""
        self._elk.send(pt_encode(self._index))

class Lights(Elements):
    """Handling for multiple lights"""
    def __init__(self, elk):
        super().__init__(elk, Light, Max.LIGHTS.value)
        add_message_handler('PC', self._pc_handler)
        add_message_handler('PS', self._ps_handler)

    def sync(self):
        """Retrieve lights from ElkM1"""
        for i in range(4):
            self.elk.send(ps_encode(i))
        self.get_descriptions(TextDescriptions.LIGHT.value)

    # pylint: disable=unused-argument
    def _pc_handler(self, housecode, index, light_level):
        self.elements[index].setattr('status', light_level)

    def _ps_handler(self, bank, statuses):
        for i in range(bank*64, (bank+1)*64):
            self.elements[i].setattr('status', statuses[i-bank*64])
