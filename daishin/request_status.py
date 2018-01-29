from enum import Enum


class RequestStatus(Enum):
    error = -1
    success = 0
    wait = 1
