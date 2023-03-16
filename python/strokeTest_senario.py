import random

import requests
import json
import uuid
import time
import sys
from random import shuffle


def shootRequests(userLoopNum):
    for courseId in range(1,4):
        for courseTimeId in range(1,5):
            for pageNum in range(10):
                for strokeIndex in range(10):
                    stroke_object0 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"DgDRCps+XI+GQY/CVUEAAAAMANgcCD/sUYZBmplVQQAAAC4AuEs9P3sUhkGF61VBAAAAIwBfbVE/pHCFQUjhVkEAAAAXAAUMXj/heoRB16NYQQAAAAwA8FheP/YohEG4HllBAAAACwAucl0/FK6DQWZmWkEAAAAMAMjyXj9I4YJBAABcQQAAAAsA8FheP4XrgUEfhV9BAAAADAAZv10/pHCBQbgeYUEAAABGACRaYT97FH5BUrhuQQAAABcAJFphP65HfUEpXHNBAAAAIgDSjWI/FK57QbgefUEAAABzAG2Raz9I4XpBKVyRQQAAAP8AHMVsPx+Fe0HXo5RBAAAAIgAcxWw/uB59QfYomEEAAAAXAAcSbT8zM39BuB6bQQAAAAwAMHhsPwrXf0HXo5xBAAAADABFK2w/7FGAQZqZnUEAAAALAFneaz9cj4BBzcyeQQAAAAwAMHhsPz0KgUGPwp9BAAAAFwDzXm0/heuBQQAAokEAAAALAG2Raz9I4YJBPQqjQQAAABcAlvdqP0jhhEFmZqRBAAAADACW92o/ZmaGQbgepUEAAAALAJb3aj9I4YZBH4WlQQAAABgAv11qP/YoiEHsUaZBAAAADAD8dmk/KVyJQVK4pkEAAAAWACXdaD8UrotBMzOnQQAAAEYA6MNpP1yPlkFI4aZBAAAADADUEGo/4XqYQeF6pkEAAAAiAPx2aT/sUZxBw/WkQQAAABcAWd5rP3sUnkEK16NBAAAAFwDeq20/AACgQQAAokEAAAAvABzFbD8zM6NBXI+cQQAAAAsA815tPx+Fo0GamZtBAAAAIgAHEm0/heujQeF6mEEAAAAvAPNebT9SuKRBCteRQQAAABYA3qttP8P1pEEfhY9BAAAAGADK+G0/UrikQRSuiUEAAAALAKwtcj97FKRBexSGQQAAAAwACJV0PxSuo0HNzIRBAAAACwC3yHU/KVyjQXE9hEEAAAAXAP98eD/D9aJBSOGCQQAAABcAW+R6P2ZmokGamYFBAAAAGACESno/heuhQVyPfkEAAAALAJn9eT+kcKFB16N8QQAAAAsAezJ+PxSuoUEzM3tBAAAAGAAAAIA/ZmagQa5HeUEAAAAiALhLfT/NzJ5Brkd1QQAAACMAUsx+P8P1nEGF63FBAAAADAAUs38/7FGcQbgecUEAAAAiAI/lfT9cj5pBZmZuQQAAAAwAChh8P3sUmkGkcG1BAAAAFgBHMXs/16OYQR+Fa0EAAAAjAJn9eT8pXJVBH4VnQQAAAC4AZn9+P3sUkkGamWVBAAAADABmf34/j8KRQa5HZUEAAAAjAAAAgD89CpFBzcxkQQAAAC4AAACAPx+Fj0H2KGRBAAAADAAAAIA/w/WOQQAAZEEAAAALAAAAgD9mZo5BAABkQQAAAAwAAACAP4/CjUEK12NBAAAAaAAUs38/XI+KQQrXY0EAAAALAAAAgD/sUYpBAABkQQAAAAwAAACAPwAAikEAAGRBAAAACwAAAIA/FK6JQfYoZEEAAAAMAD0Zfz+kcIlB9ihkQQAAABcAFLN/PzMziUHsUWRBAAAARgAAAIA/UriIQexRZEEAAAAXAAAAgD9xPYhB9ihkQQAAAAsAAACAPxSuh0H2KGRBAAAADAAAAIA/MzOHQQAAZEEAAAA6AAAAgD+PwoVBAABkQQAAACIAAACAPx+FhUEK12NBAAAAIgBl/HY/UriEQQrXY0EAAAAMAA4kWj9mZoRBFK5jQQAAAAwAmf15PgrXg0EUrmNBAAAA","dotCount":78,"strokeKey":"fd65f34e-beb6-4d02-9ca5-476dc9472c2ftest","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674626961740},"surfaceOwnerId":"%s","writerId":"adssg","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object1 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"DQBtkes9Uri8QR+FY0EAAAALAI3fLj9SuLxBCtdjQQAAACMAC5tDP8P1vEEK12NBAAAAFwDPBEw/XI++QSlcX0EAAAAuAGoIVT/hesJBhetRQQAAAAwA2yJXP0jhwkEAAFBBAAAACwAZv10/uB7DQSlcT0EAAABdAHgsbz+uR8NBCtdPQQAAAAsAeCxvPzMzw0H2KFBBAAAAaABvFHM/ZmbEQaRwiUEAAAAjALfIdT97FMZB9iiUQQAAAFAAZfx2P9ejxkGF66FBAAAALwCOYnY/UrjGQaRwo0EAAADFAE/Gbz9I4b5BAACkQQAAABYARStsP/YovEHsUaRBAAAADACXenI/pHC7QdejpEEAAAAXAPx2aT8zM7tBzcykQQAAAFEAvtpiPx+Fu0FSuKRBAAAAXQC0wmY/hevHQRSuo0EAAAAiAMl1Zj9SuMpBMzOjQQAAAAsAtMJmPzMzy0G4HqNBAAAADACgD2c/pHDLQbgeo0EAAAAXAHepZz8UrstBPQqjQQAAANAA3qttP4/Cy0E9CqNBAAAA0ADVk3E/FK7LQT0Ko0EAAACiAEcx+z6amctBw/WiQQAAAAsA4jSEPZqZy0HheqJBAAAA","dotCount":27,"strokeKey":"7b052535-4750-4e38-99ff-6b1edd704ea5test","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674626992924},"surfaceOwnerId":"%s","writerId":"adssg","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object2 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"DADqyTg/j8IAQilcY0EAAAALAB9OQz89CgFCKVxjQQAAABcAfrtUP/YoAUIzM2NBAAAAFwBYW2Q/rkcBQjMzY0EAAABoANQQaj/XowFCUrhiQQAAABcAESppP4XrAkJSuF5BAAAADAD8dmk/7FEDQrgeXUEAAAAYADqQaD+4HgRCFK5bQQAAABYAd6lnP4XrBEI9CltBAAAARgCgD2c/4XoIQj0KW0EAAAAMAKAPZz+4HglCCtdbQQAAAAoAoA9nP1yPCULNzFxBAAAAGAC0wmY/H4UKQgrXX0EAAAAMAAaPZT89CgtChethQQAAACIAvtpiPx+FDEI9CmtBAAAADABsDmQ/w/UMQlK4bkEAAAAjAIHBYz/Xow1CuB55QQAAADsAyvhtP0jhDUL2KIhBAAAAFgAx+3M/KVwNQhSui0EAAAAjAOrJeD/D9QtCXI+QQQAAABcAW+R6P5qZCkIUrpNBAAAACwDhsXw/CtcJQrgelUEAAAD/AFvkej/XowZCPQqZQQAAAEYARzF7Pz0KA0LsUZxBAAAACwCZ/Xk/XI8CQtejnEEAAAAXAFvkej+kcAFCFK6dQQAAACMAHst7P3sUAELhep5BAAAAFgAKGHw/rkf/Qc3MnkEAAACWAMt7dT8Urv9BXI+eQQAAADsAjmJ2P3sUA0IfhZ1BAAAALgC3yHU/CtcGQo/Cm0EAAABGAKIVdj/heg1CH4WZQQAAAHMAohV2P8P1FULD9ZhBAAAAGABRSXc/FK4WQlK4mEEAAAAMAHmvdj8AABdCzcyYQQAAADkAUUl3PxSuGELNzJhBAAAACwBl/HY/CtcYQkjhmEEAAAD/AFFJdz/sURpCSOGYQQAAABgAPJZ3P6RwGkLD9ZhBAAAAFwB5r3Y/mpkaQsP1mEEAAADPADJ+ez8UrhpCw/WYQQAAAF0AN4oZP1yPGkLNzJhBAAAACwA8lvc9XI8aQs3MmEEAAAA=","dotCount":43,"strokeKey":"5ac1c402-ed88-42b7-8d58-a6174e90fd17test","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627008601},"surfaceOwnerId":"%s","writerId":"sdg235","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object3 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"EgAXuc49ZmYyQo/CXUEAAAAXAMt7tT5mZjJCmpldQQAAAAsAsz8fP6RwMkKkcF1BAAAALwDan08/4XoyQsP1XEEAAAA6AItcZz9cjzJC7FFcQQAAADkAZHlvP83MMkJI4VpBAAAADADpRnE/w/UyQpqZWUEAAAAiAOlGcT9cjzNCXI9WQQAAACMAg8dyP1K4NEJI4VJBAAAAFwCDx3I/16M1QgAAUEEAAAAXANWTcT8pXDZCcT1OQQAAAC8ArC1yPxSuN0LXo0xBAAAAIgDVk3E/KVw5QhSuS0EAAAAvANWTcT8fhTtCCtdLQQAAAAsA/vlwP0jhO0L2KExBAAAACwDpRnE/MzM8QtejTEEAAAALANWTcT9cjzxCmplNQQAAAAwA1ZNxP83MPEJcj05BAAAAGAASrXA/MzM9Qs3MUEEAAAAjAOlGcT8Urj1Cw/VUQQAAAAsAwOBxP4XrPUJmZlZBAAAACwDVk3E/exQ+QgrXV0EAAAAXABKtcD8pXD5CPQpbQQAAACMAOxNwP5qZPkJmZl5BAAAADACN324/16M+QkjhXkEAAAAWAG8Ucz9cjz5CCtdfQQAAAA0ACJV0Px+FPkLNzGBBAAAACwCOYnY/7FE+QlK4YkEAAAAuALfIdT9I4TxCj8JpQQAAAAwAy3t1P1yPPEIK12tBAAAACwC3yHU/MzM8QqRwbUEAAAAMAB1IdD8K1ztCH4VvQQAAABcAHUh0Pz0KO0JmZnJBAAAAIwDLe3U/Urg5QrgedUEAAAALAOAudT9xPTlCZmZ2QQAAACMAy3t1PwrXN0LNzHhBAAAAFwDgLnU/AAA3QpqZeUEAAAAXAMDgcT8zMzZCPQp7QQAAAK4AohV2P+F6NULD9XxBAAAAFgDLe3U/cT01Qq5HfUEAAAAjAMt7dT/XozRCj8J9QQAAADoARq5zPylcNEJ7FH5BAAAAIgB5r3Y/SOEzQlyPfkEAAAAMABMweD9SuDNCXI9+QQAAABcA6UZxP3E9M0JI4X5BAAAAGABl/HY/16MyQilcf0EAAAChAHCXej/NzDJCKVx/QQAAABYAmf15P5qZM0Jcj35BAAAAGACtsHk/FK40QuF6fEEAAABdAK2weT9xPTlCMzN7QQAAACIA1hZ5P4XrOkLD9XxBAAAADACtsHk/XI87QpqZfUEAAAAXAJn9eT+kcDxCPQp/QQAAABcArbB5PylcPUJI4YBBAAAACwCtsHk/j8I9QqRwgUEAAAA7AK2weT/sUUBC9iiGQQAAACIAcJd6PylcQULheohBAAAADABwl3o/16NBQq5HiUEAAAAuAPVkfD+uR0JCzcyMQQAAAAwAj+V9PylcQkKuR41BAAAACwB7Mn4/ZmZCQoXrjUEAAAALAD0Zfz9mZkJCw/WOQQAAABgAZn9+P/YoQkKuR5FBAAAAFwAUs38/mplBQpqZk0EAAAAjAAAAgD/D9UBC16OWQQAAABYAAACAPx+FQELhephBAAAAGAAAAIA/ZmZAQlK4mEEAAAAWAAAAgD/2KEBCH4WZQQAAAAwAAACAP83MP0JmZppBAAAAFwAAAIA/FK4+QvYonEEAAAAjAAAAgD+kcD1CrkedQQAAAC8AAACAP5qZO0KuR59BAAAACwAAAIA/MzM7QpqZn0EAAAAWAAAAgD8fhTpCCtefQQAAAAwAAACAP2ZmOkKF659BAAAAIwApZn8/Urg5QoXrn0EAAAALAAAAgD8fhTlCCtefQQAAADsAAACAP1K4OEIK159BAAAACwAAAIA/H4U4QoXrn0EAAABdAAAAgD/D9TdCheufQQAAAC4AKWZ/P1yPNkKamZ9BAAAADADhsXw/AAA2QqRwn0EAAAAWABSzfz/sUTVCPQqfQQAAAAwAFLN/P/YoNULD9Z5BAAAAIwBkeW8/PQo1QlK4nkEAAAAWAMZvlz6F6zRC16OeQQAAAA==","dotCount":86,"strokeKey":"df124703-4330-4377-9d6d-1dd70aa3a58etest","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627023188},"surfaceOwnerId":"%s","writerId":"wefsdklfgn","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object4 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"FQDtzwc+zcxhQgAATEEAAAAXAHEawj7NzGFCAABMQQAAAAwAVVUVP83MYUIAAExBAAAALgAXuU4/hethQgAATEEAAABRAAiVdD/D9WFC4XpMQQAAABYAjmJ2P8P1YULD9UxBAAAAGAC3yHU/mplhQuxRUEEAAAAXAJn9eT9cj2BCzcxYQQAAAEYAZfx2P4XrXUKuR3VBAAAACwCiFXY/4XpdQrgeeUEAAAALAGX8dj8zM11Cw/V8QQAAAAwAohV2PwAAXUJxPX5BAAAAFwD04XQ/FK5cQrgegUEAAAALALfIdT/helxCCteBQQAAAAwAZfx2PylcXEL2KIJBAAAAGACiFXY/7FFcQmZmgkEAAABbAIRKej/helxCcT2CQQAAAC8AEzB4P5qZXEL2KIJBAAAAaADCY3k/rkdgQoXrgUEAAABoADJ+ez9I4WdCXI+AQQAAAFwAMn57PwAAcUJSuH5BAAAALwBwl3o/pHBzQlyPfkEAAAAWAEcxez9mZnRCZmZ+QQAAAAwAMn57Px+FdEJcj35BAAAAFwBwl3o/w/V0QlyPfkEAAADQAD0Zfz89CnVCXI9+QQAAANAAKWZ/P4XrdEJcj35BAAAAaAAAAIA/XI90QlyPfkEAAAAYAAAAgD+F63NCSOF+QQAAABYAAACAPx+Fc0JI4X5BAAAAGAAAAIA/ZmZzQj0Kf0EAAABRAAAAgD8AAHNCPQp/QQAAABYAAACAP0jhckIzM39BAAAA0AAAAIA/CtdyQj0Kf0EAAACAAPVkfD+uR3BCSOF+QQAAAC4AMn57P2ZmbEJxPX5BAAAAFQDgLnU/4XprQpqZfUEAAAAZAOAudT/D9WpC9ih8QQAAAAwAt8h1P0jhakIUrntBAAAAFwC3yHU/UrhqQj0Ke0EAAAAXAB1IdD+amWpCexR6QQAAACIA6UZxP3sUakIK13NBAAAADADVk3E/hetpQlyPckEAAAAjAN6rbT+amWlCFK5rQQAAAAsA1BBqP+F6aULsUWhBAAAACwC/XWo/H4VpQrgeZUEAAAAYAMl1Zj9xPWlCcT1eQQAAABcAY/ZnPwAAaUIzM1tBAAAADAAl3Wg/hetoQo/CWUEAAAALABEqaT+PwmhCzcxYQQAAABcAOpBoPx+FaEJcj1ZBAAAAFwCgD2c/MzNoQhSuU0EAAAALAPx2aT+4HmhCMzNTQQAAAC8A/HZpPwAAaEI9ClNBAAAAFwB3qWc/w/VnQkjhUkEAAACAAMr4bT+F62dCKVxTQQAAABYAZHlvPwAAaELXo1RBAAAAOgAo43c/mploQilcd0EAAAAMAP98eD/NzGhCMzN/QQAAAAsA/3x4P1yPaEJI4ZhBAAAAIwD/fHg/ZmZoQqRwnUEAAAAXAOrJeD8pXGhCuB6fQQAAACMA1hZ5P65HaEIfhaFBAAAAFgDWFnk/9ihoQq5Ho0EAAAANAP98eD/2KGhCj8KjQQAAADkA/3x4PwAAaEJSuKRBAAAADAD/fHg/w/VnQs3MpEEAAAAWAMJjeT+F62dCuB6lQQAAACQA1hZ5P8P1Z0IpXKVBAAAA0ABwl3o/w/VnQqRwpUEAAAAWAFvkej8AAGhCpHClQQAAABcARzF7P8P1Z0KkcKVBAAAADABwl3o/AABoQqRwpUEAAABGAG8UMz+F62dCrkelQQAAAAsAulHMPYXrZ0KuR6VBAAAA","dotCount":75,"strokeKey":"d05cfe2c-4e5f-481f-b078-b3664998c1f1test","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627039521},"surfaceOwnerId":"%s","writerId":"fasdagdsfhf","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object5 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"EABqCBU+pPCHQqRwOUEAAAALACZg8D6k8IdCuB45QQAAAAwAI9dZP8P1h0KuRzlBAAAAIgDUEGo/AACIQpqZOUEAAABSAEaucz89CohCpHA9QQAAAH4AWmFzPz0KiEIAAGxBAAAADACXenI/exSIQs3MbEEAAAA6AG8Ucz/XI4hCzcxsQQAAABcA815tP9cjiELsUWxBAAAAFwBPxm8/rkeIQilca0EAAAAMAKwtcj89iohCcT1qQQAAABYAy3t1P49CiULD9WhBAAAAIwAKGHw/9iiLQsP1aEEAAAAMAKOYfT9SuItCZmZqQQAAABYAj+V9P3G9jELD9XBBAAAADACP5X0/XA+NQhSuc0EAAAAXAClmfz/DdY1Czcx4QQAAABgAAACAP67HjUIK139BAAAAIgAAAIA/7NGNQtejhEEAAAAMAAAAgD+ux41CmpmFQQAAAAsAAACAP/aojULheoZBAAAALgCZ/Xk/16OLQhSujUEAAAAMAI/lfT+PQotCmpmPQQAAAAsAcJd6P+H6ikLXo5BBAAAADAD1ZHw/9qiKQilckUEAAAAMADJ+ez9mZopCFK6RQQAAAC4A4bF8P5qZiUJ7FJJBAAAADAD1ZHw/4XqJQgAAkkEAAAALAB7Lez9mZolCAACSQQAAAEYAuEt9PwpXiUKF65FBAAAA0ADM/nw/KVyJQoXrkUEAAACKAPThdD+Fa4lCAACSQQAAACMAohV2P2bmiUIK15FBAAAAFgC3yHU/AICKQhSukUEAAAAvAMDgcT+kcItCPQqRQQAAABcA/vlwP1yPi0JI4ZBBAAAAFwDpRnE/M7OLQlyPkEEAAAALAP75cD8p3ItC7FGQQQAAABgAtUVuP/YojEIfhY9BAAAAFwBZ3ms/SGGMQlK4jkEAAAAjAPLbZT+ux4xCzcyMQQAAABYAyXVmP2bmjEJ7FIxBAAAALwASrXA/heuMQgrXi0EAAAAjAI5idj9I4YxCmpmLQQAAAFEAAACAP+zRjEKPwotBAAAALgAAAIA/7NGMQgAAjEEAAAAjAOGxfD8p3IxCj8KLQQAAAM8AcJd6P0jhjEKamYtBAAAARgAIlXQ/KdyMQq5Hi0EAAAAuAKGSbj9SuIxCmpmDQQAAADkAT8ZvPxQujEL2KHRBAAAAIwAdSHQ/zcyLQpqZbUEAAAAMAEaucz8UrotC9ihsQQAAABcAbxRzPylci0KPwmlBAAAAFwAx+3M/XA+LQgAAaEEAAAAMADH7cz+k8IpCKVxnQQAAAAsARq5zP+zRikJI4WZBAAAAFwChkm4/pHCKQsP1ZEEAAAAjAMDgcT89CopCUrhiQQAAAAsA6UZxP8P1iUJxPWJBAAAAFwBFK2w/M7OJQrgeYUEAAAAMAJb3aj89iolC9ihgQQAAAAwAlvdqP4VriUIzM19BAAAACwAcxWw/KVyJQlyPXkEAAAAXAFneaz+uR4lChetdQQAAAAwAoA9nP49CiUKkcF1BAAAAFwDdKGY/mhmJQgAAXEEAAAAMAGP2Zz8AAIlCMzNbQQAAACIAq6pqPwrXiEJxPVpBAAAAXQCrqmo/zcyIQo/CWUEAAABoABEqaT+PwohC9ihYQQAAABcAq6pqP3G9iEIUrldBAAAALgBYW2Q/M7OIQj0KV0EAAAALACRaYT8UrohCcT1WQQAAAAwAEKdhP7ieiEK4HlVBAAAACwC+2mI/mpmIQuF6VEEAAAA6AL9daj89iohC9ihUQQAAAFIA1BBqP5qZiELsUVRBAAAALQCDx3I/CteJQhSuU0EAAAA7AAiVdD+kcIxCzcxUQQAAAHMAKON3P5oZj0K4HlVBAAAAogBl/HY/MzOQQrgeVUEAAAAiAFFJdz+PQpBCw/VUQQAAAHQAZfx2P+zRkELD9VRBAAAAxADYHAg/zcyQQsP1VEEAAAALAD6chjzNzJBCzcxUQQAAAA==","dotCount":86,"strokeKey":"dbf4b33a-ce30-4ba0-8179-3ef73b9ab714test","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627058127},"surfaceOwnerId":"%s","writerId":"dfsdfgdf","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object6 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"FgCfjB8/heuXQRSuPkIAAAAYACDRSj8AAJhBUrg+QgAAAC4A815tPwAAmEEK1z5CAAAAOQAKGHw/pHCXQTMzP0IAAAAMAAoYfD/D9ZZBpHA/QgAAABcAj+V9Px+FlUFcj0BCAAAAOgD1ZHw/w/WQQTMzRUIAAAAXADJ+ez8K149B9ihHQgAAAEUAcJd6P6Rwj0HD9UxCAAAALgAKGHw/zcyQQaRwUEIAAAAjAFvkej8AAJJBCtdSQgAAABcAChh8Pylck0EpXFRCAAAAFwDhsXw/PQqVQR+FVUIAAAAjAHCXej+4HpdBPQpXQgAAACMARzF7PylcmUEzM1hCAAAACwCZ/Xk/ZmaaQRSuWEIAAAA6ADH7cz/NzKBBXI9aQgAAABcAl3pyP8P1okE9CltCAAAAFwBZ3ms/4XqkQfYoW0IAAAAMAOjDaT89CqVB9ihbQgAAAAsAESppP4/CpUF7FFtCAAAADAARKmk/zcymQQrXWkIAAAAiADqQaD+F66lB7FFZQgAAADoA50BiP6Rwr0GPwlVCAAAAFwBj9mc/4XqwQdejVEIAAAAMANQQaj/NzLBBMzNUQgAAACMAEq1wP7gesUHD9VJCAAAACwC3yHU/uB6xQY/CUkIAAAAjAFFJdz/Xo7BBCtdRQgAAABcA6sl4PwrXr0EAAFFCAAAACwB7Mn4/pHCvQVK4UEIAAAAjAAAAgD/sUa5BcT1QQgAAACMAAACAP+F6rEHXo09CAAAAIgAAAIA/heupQbgeT0IAAAAWAAAAgD9I4ahBw/VOQgAAAFIAAACAPwrXo0EAAE9CAAAADAAAAIA/w/WiQXsUT0IAAAAXAAAAgD89CqFB4XpPQgAAABcAAACAPxSun0EK109CAAAAFwAAAIA/XI+eQTMzUEIAAAAXABSzfz8pXJ1Bj8JQQgAAABcAPRl/P+xRnEEpXFFCAAAAIwApZn8/SOGaQVK4UkIAAAAXAHsyfj9mZppBrkdTQgAAACMAUsx+P/YomkEAAFRCAAAAFwCP5X0/exSaQc3MVEIAAAA6AHsyfj8AAJpB7FFXQgAAAAsAo5h9P4XrmUGamVdCAAAAIwBmf34/heuZQUjhV0IAAADQAGZ/fj8AAJpBCtdXQgAAANAAAACAPwAAmkEK11dCAAAAfwD4aks/heuZQc3MV0IAAAAMAIdQyT4K15lBj8JXQgAAAA==","dotCount":53,"strokeKey":"eb28ac5a-e614-4f57-8296-144c47773faftest","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627080002},"surfaceOwnerId":"%s","writerId":"2354653gsdf","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object7 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"FgB5r7Y9PQrvQdejN0IAAAAiAEOopD7D9e5BUrg3QgAAACMA7c8HP8P17kFSuDdCAAAALgBxGkI/PQrvQY/CN0IAAADQAMjyXj89Cu9Bj8I3QgAAANAAv11qP7ge70GPwjdCAAAAaAA7E3A/KVzvQVK4N0IAAAAuAIJEaz9SuPBBj8I3QgAAACMA3qttP3sU9EEUrjdCAAAAIwAHEm0/hev3QWZmN0IAAAA5APNebT/Xo/5BUrg2QgAAACMAoZJuPzMzAUJcjzZCAAAALgDeq20/SOECQuxRNkIAAABRAKGSbj+kcAVCKVw2QgAAAAsAjd9uPxSuBUJmZjZCAAAADAChkm4/zcwFQmZmNkIAAAAWAMr4bT+F6wVCpHA2QgAAADAA815tP7geBkKkcDZCAAAALQDK+G0/4XoGQh+FNkIAAADRAEaucz8fhQZCmpk2QgAAAH8APRl/P9ejBkJmZjhCAAAAUAAAAIA/CtcGQj0KQEIAAACLAAAAgD8pXAZCH4VIQgAAAAsAAACAP3E9BkK4HklCAAAADAAAAIA/uB4GQuF6SUIAAAA6AAAAgD8pXAVCAABNQgAAACIAAACAP4XrBEI9Ck9CAAAADAAAAIA/CtcEQq5HT0IAAAAMAAAAgD8K1wRC4XpPQgAAAAsAAACAP83MBEKamU9CAAAADAAAAIA/zcwEQo/CT0IAAAALAAAAgD+PwgRChetPQgAAAC8AAACAP9ejBEIzM1JCAAAACwAAAIA/mpkEQs3MUkIAAAAXAAAAgD/hegRCZmZTQgAAACMAAACAP2ZmBEIfhVNCAAAAxQAAAIA/ZmYEQoXrU0IAAAAiAAAAgD+kcARCj8JUQgAAACIAAACAPx+FBEI9ClZCAAAALwAAAIA/j8IEQo/CV0IAAAAXAAAAgD9I4QRCMzNYQgAAALkArbA5P0jhBEKuR1hCAAAACwAdSDQ+zcwEQnE9WEIAAAA=","dotCount":43,"strokeKey":"45fcb7e5-21ae-4c55-b012-8a3c725a9f9dtest","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627102335},"surfaceOwnerId":"%s","writerId":"asdgdq34gfd","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object8 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"FgBe6kk9XI8rQkjhMkIAAAAiABe5zj1SuCtChesyQgAAABcAqSdjPgrXK0IAADNCAAAAIwCbAwk/SOErQgAAM0IAAAAXAHEaQj9I4StCw/UyQgAAAF0Aea92P0jhK0JI4TJCAAAAIgAyfns/CtcrQgAAM0IAAAAYAEcxez9cjytCMzMzQgAAACIAzP58P83MKkKamTNCAAAADAAKGHw/16MqQo/CM0IAAAAiAJn9eT/NzClCAAA1QgAAAAwA1hZ5P2ZmKUJI4TVCAAAAFwDCY3k/CtcoQgrXNkIAAAAhANYWeT8zMyhCFK44QgAAAA0AKON3P7geKEI9CjlCAAAAXABvFHM/pHAoQpqZQEIAAAAMAP75cD+PwihC7FFBQgAAABcAOxNwPzMzKULD9UFCAAAADAChkm4/CtcpQtejQkIAAAALANQQaj/sUSpCAABDQgAAAAwAq6pqP8P1KkIpXENCAAAACwARKmk/CtcrQhSuQ0IAAAAvAN6rbT+Pwi9C4XpEQgAAABYAyvhtP9ejMUK4HkVCAAAAUQDpRnE/hes3QrgeSUIAAAAYAJd6cj/2KDlCrkdKQgAAABcAbxRzP0jhOUJxPUtCAAAAFwDLe3U/XI86QuF6TEIAAAAXAGX8dj/NzDpCZmZNQgAAAAsAea92P0jhOkJI4U1CAAAAIwD04XQ/j8I6QlyPUEIAAAAXAPThdD9xPTpCUrhSQgAAACMAbxRzP3sUOULD9VRCAAAACwD04XQ/XI84QqRwVUIAAAAYAAiVdD8pXDdCcT1WQgAAABcA/vlwPz0KNkKamVZCAAAAOQD8dmk/zcwwQq5HVkIAAAAMAKuqaj+amS9CzcxVQgAAAAsAv11qP9ejLkIzM1VCAAAADAC/XWo/w/UtQh+FVEIAAAAXAKAPZz8fhSxC9ihSQgAAABcATkNoPz0KLELD9VBCAAAAIwB3qWc/mpkrQgrXTUIAAAAXAHepZz/XoytCXI9LQgAAAAwATkNoP0jhK0JmZkpCAAAAIgD8dmk/rkctQjMzR0IAAAAuABEqaT89CjBCzcxBQgAAACMAESppPwrXMEKuR0BCAAAADAAl3Wg/w/UwQsP1P0IAAAAuAIJEaz9SuDFCpHA8QgAAAAsAq6pqP4XrMUIK1ztCAAAAFwCW92o/PQoyQkjhOkIAAAA6AIJEaz8zMzJCFK43QgAAABgA815tP/YoMkIAADdCAAAAIgChkm4/CtcxQgAANUIAAAAMACZgcD+PwjFCUrg0QgAAACIAPJZ3P1yPMUKkcDRCAAAAIwBl/HY/AAAxQqRwM0IAAAAMAHmvdj/NzDBC9igzQgAAAC4ArbB5P+xRL0KPwjFCAAAAOgCjmH0/exQvQpqZMUIAAABFAEcxez8K1y1CZmYxQgAAABcAW+R6PylcLULsUTFCAAAADAAyfns/9igtQnE9MUIAAAAiAMz+fD9I4SxC9igxQgAAADoAZfx2P4/CLEIzMzFCAAAAFwA9GT8/XI8sQjMzMUIAAAAMALnOhD5xPSxCMzMxQgAAAA==","dotCount":68,"strokeKey":"b3962977-34e3-44da-a326-3c80a6da9803test","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627119526},"surfaceOwnerId":"%s","writerId":"fasdgh","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    stroke_object9 = """{"type":"stroke_added","webBluetoothId":"test","mac":"9C:7B:D2:53:EF:4E","pageInfo":{"section":3,"owner":27,"book":168,"page":%d},"dotsBase64":"FgABg0c+UrhcQqRwMkIAAAD/APnt0j5SuFxCZmYyQgAAAGgAMftzPgrXXELsUTJCAAAAOgAq6QY/hetcQq5HMkIAAAAWACrpRj+F61xCcT0yQgAAAFIAzP58P8P1XEKuRzJCAAAAFwAAAIA/hetcQmZmMkIAAAAXAAAAgD/NzFxC4XoyQgAAABcAAACAP4XrW0LXozJCAAAAFwAAAIA/hetaQoXrMkIAAAALAAAAgD9xPVpCMzMzQgAAABgAAACAPzMzWUIK1zNCAAAAFwAAAIA/rkdYQpqZNEIAAAAjAAAAgD8K11ZC9ig2QgAAAAsAAACAP5qZVkIfhTZCAAAACwAKGHw/7FFWQvYoN0IAAAAjADJ+ez8UrlVCrkc6QgAAACMAW+R6P+F6VUK4Hj1CAAAACwDWFnk/4XpVQlyPPUIAAAAYALfIdT8UrlVCmpk+QgAAAAsAHUh0P4XrVUK4Hj9CAAAAFwChkm4/KVxWQh+FP0IAAAAMABzFbD9SuFZC16M/QgAAAAsAMHhsPx+FV0LNzD9CAAAAIwBOQ2g/KVxaQhSuP0IAAAAiAKAPZz/2KF1Cj8I+QgAAAAwAd6lnP0jhXUIfhT5CAAAADAB3qWc/mpleQj0KPkIAAAAMACXdaD+uR19C9ig9QgAAABYAY/ZnP1K4YEKkcDpCAAAAFwCW92o/KVxhQilcOEIAAAA6ACZgcD8zM2FC7FE0QgAAAAwAHUh0Pz0KYULD9TNCAAAACwB5r3Y/CtdgQtejM0IAAAAYAIRKej+kcGBCrkczQgAAABcAmf15P+xRYEL2KDNCAAAAUQDM/nw/rkdgQuxRM0IAAAAiAGZ/fj9cj2BCzcw0QgAAAEYAPRl/P3sUY0KkcEBCAAAARQAAAIA/XI9lQjMzTUIAAABcAAAAgD+amWdCZmZXQgAAAAwAAACAP83MZ0I9ClhCAAAACwAAAIA/w/VnQq5HWEIAAAAXAAAAgD89CmhCXI9YQgAAAMUArC1yP3sUaEKkcFhCAAAAFwA8lnc+zcxnQvYoWEIAAAA=","dotCount":46,"strokeKey":"1dfc3859-5be3-49f4-bf81-5f4d1b10f372test","strokeProps":{"thickness":0.2,"brushType":0,"color":"rgb(0, 0, 0)","status":"normal","startTime":1674627133262},"surfaceOwnerId":"%s","writerId":"afsdfdbsgsa","originalStrokeKey":"%s"}""" % (
                        pageNum, userLoopNum, uuid.uuid4())
                    objectList = [stroke_object0, stroke_object1, stroke_object2, stroke_object3, stroke_object4,
                                  stroke_object5, stroke_object6,
                                  stroke_object7, stroke_object8, stroke_object9]

                    requests.post("http://localhost:7070/api/v1/neopen/upload/{}/{}/{}".format(userLoopNum, courseId, courseTimeId), json=json.loads(objectList[strokeIndex % 10]))
def main():
    userLoopNum = 100
    for user in range(userLoopNum):
        shootRequests(user)
main()
