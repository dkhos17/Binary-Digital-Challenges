### Challenge-5
We can create a function EventTuple, which will handle arg1 and arg2,
where the arg1 is the type of event and arg2 is the list of event arguments.
So we can make switch with event types(arg1) and than return one of the already written classes,
but at first we should cast the arguments in right type which is also given(str or int) or we can write method which cast tup[0] as tup[1].
RET something like this: UserClickedOnButtonEvent.create(str(arg2[0][0])) or UserLongPressedEvent(int(arg2[0][0]), int(arg2[1][0]))