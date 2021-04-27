import uuid, ulid
import time, calendar

class UserClickedOnButtonEvent:
    def __init__(self, event_id, button_id, event_type = 'UserClickedOnButton'):
        self._event_id_ = event_id
        self._event_type_ = event_type
        self._button_id_ = button_id
    
    def timestamp(self):
        return ulid.from_uuid(self._event_id_).timestamp().int
    
    def event_id(self):
        return self._event_id_
        
    def event_type(self):
        return self._event_type_
    
    def button_id(self):
        return self._button_id_

    @classmethod
    def create(cls, button_id):
        event_id = uuid.uuid1()
        return cls(event_id, button_id)


class UserLongPressedEvent:
    def __init__(self, event_id, x, y, event_type = 'UserLongPressed'):
        self._event_id_ = event_id
        self._event_type_ = event_type
        self._x_, self._y_ = x, y
    
    def timestamp(self):
        return ulid.from_uuid(self._event_id_).timestamp().int
    
    def event_id(self):
        return self._event_id_
    
    def event_type(self):
        return self._event_type_

    def x(self):
        return self._x_
    
    def y(self):
        return self._y_

    @classmethod
    def create(cls, x, y):
        event_id = uuid.uuid1()
        return cls(event_id, x, y)    


# UserClickedOnButtonEvent("b5796505-68fd-40d5-814a-9d31f3f084b0", "close_button")
# UserClickedOnButtonEvent(event_id="b5796505-68fd-40d5-814a-9d31f3f084b0", button_id="close_button")
# UserClickedOnButtonEvent.create(button_id='blabla')

# UserLongPressedEvent("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 340, 420)
# UserLongPressedEvent(event_id="1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", x=340, y=420)
# UserLongPressedEvent.create(x=340, y=420)