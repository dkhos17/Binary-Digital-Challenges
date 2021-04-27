class UserClickedOnButtonEvent:
    def __init__(self, event_id, timestamp, button_id, event_type = 'UserClickedOnButton'):
        self._event_id_ = event_id
        self._timestamp_ = timestamp
        self._event_type_ = event_type
        self._button_id_ = button_id
    
    def timestamp(self):
        return self._timestamp_
    
    def event_id(self):
        return self._event_id_
        
    def event_type(self):
        return self._event_type_
    
    def button_id(self):
        return self._button_id_


class UserLongPressedEvent:
    def __init__(self, event_id, timestamp, x, y, event_type = 'UserLongPressed'):
        self._event_id_ = event_id
        self._timestamp_ = timestamp
        self._event_type_ = event_type
        self._x_, self._y_ = x, y
    
    def timestamp(self):
        return self._timestamp_
    
    def event_id(self):
        return self._event_id_
    
    def event_type(self):
        return self._event_type_

    def x(self):
        return self._x_
    
    def y(self):
        return self._y_    

# UserClickedOnButtonEvent("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "close_button")
# UserClickedOnButtonEvent(event_id="b5796505-68fd-40d5-814a-9d31f3f084b0", timestamp=1619146052, button_id="close_button")

# UserLongPressedEvent("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, 340, 420)
# UserLongPressedEvent(event_id="1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", timestamp=1619146123, x=340, y=420)