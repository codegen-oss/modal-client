from modal import App, Period, function
from modal.proto import api_pb2

app = App()


@function(app=app, schedule=Period(seconds=5))
def f():
    pass


def test_schedule(servicer, client):
    with app.run(client=client):
        assert servicer.function2schedule == {"fu-1": api_pb2.Schedule(period=api_pb2.Schedule.Period(seconds=5.0))}
