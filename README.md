### Challenge-5
We can Have EventTuple Class with one field for example: eventType.

So when we want to create EventTuple("some_event_type_here", [(field1, str), (field2, int), ...]) like this,

In __init__() method - we will set self.eventType as "some_event_type_here", and for the rest of the arguemnts in the list

we can make for loop and use SETATTR like this setattr(self, field1, str), setattr(self, field2, int) like this.

So we will have all needed fileds for the returned event.

```python
class EventTuple:
    def __init__(self, etype, attrs):
        self.eventType = etype
        for x in attrs:
            setattr(self, x[0], x[1]) # or check x[1] type and then set some default value.

e = EventTuple("some_event_type_here", [(field1, str), (field2, int)])
# we can use now e.field1 pr e.field2
```

```python
# We can use this method to change display of event, if needed.
def __repr__(self):
  return self.eventType
print(type(e)) # will be self.eventType
```

we can use __import__(module) or getattr(module, name) funcs to manage general class as we want to.
