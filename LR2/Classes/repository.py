from typing import Generic, TypeVar, List

T = TypeVar('T')

class Repository(Generic[T]):
    def __init__(self):
        self.__items: List[T] = []

    def add(self, item: T):
        self.__items.append(item)

    def get_all(self) -> List[T]:
        return self.__items