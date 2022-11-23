from celery import shared_task
from .models import Book
import threading
import time


def wait():
    print("sleeping for 6 seconds")
    time.sleep(6)
    print("Done sleeping")


# asynchronous tasks are defined.
# threading has been used inside the function, in order to show that threading and celery are different.
# The threads execute at the same time and the rest of the code continues.
# The response of the threads will be sent after 6 seconds.
@shared_task
def changeReader(number):
    for i in range(1,number+1):
        try:
            book = Book.objects.get(id=i)
            book.Reader = "asher"
            book.save()

        except Book.DoesNotExist:
            pass
    t1 = threading.Thread(target=wait)
    t2 = threading.Thread(target=wait)

    t1.start()
    t2.start()

    return "Done"
