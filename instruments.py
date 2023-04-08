# Abstração e Herança com dataclasses
# Tem enum no Python
# Dataclasses com valor default dão erro
# Para que server o super()

# from abc import ABC, abstractmethod


# class Instrument(ABC):

#     @abstractmethod
#     def play(self):
#         ...


# class Guitar(Instrument):

#     sound: str = "Ding Ding Ding"

#     def play(self):
#         return self.sound


# class Flaute(Instrument):

#     sound: str = "Flu Flu Flu"

#     def play(self):
#         return self.sound



# from abc import ABC, abstractmethod
# from dataclasses import dataclass


# # @dataclass
# class Instrument(ABC):

#     @abstractmethod
#     def play(self):
#         ...


# @dataclass
# class Guitar(Instrument):

#     sound: str = "Ding Ding Ding"

#     def play(self):
#         return self.sound

# @dataclass
# class Flaute(Instrument):

#     sound: str = "Flu Flu Flu"

#     def play(self):
#         return self.sound



# from abc import ABC, abstractmethod
# from dataclasses import dataclass
# from enum import Enum


# class InstrumentalKind(Enum):
#     string = 0
#     wind = 1
#     keys = 2
#     drums = 3


# class ABCInstrument(ABC):

#     @abstractmethod
#     def play(self):
#         ...



# @dataclass
# class DataInstrumentMixin:    # Mixin é um objeto que deve ser utilizado junto com outra classe
#     name: str
#     sound: str
#     kind: str


# class Instrument(DataInstrumentMixin, ABCInstrument):
#     ...



# @dataclass
# class Guitar(Instrument):
#     sound: str = "Ding Ding Ding"
#     kind: str = "string"

#     def play(self):
#         return self.sound

# @dataclass
# class Flaute(Instrument):
#     sound: str = "Flu Flu Flu"
#     kind: str = "wind"

#     def play(self):
#         return self.sound







# from abc import ABC, abstractmethod
# from dataclasses import dataclass
# from enum import Enum


# class InstrumentalKind(Enum):
#     string = 0
#     wind = 1
#     keys = 2
#     drums = 3


# class ABCInstrument(ABC):

#     @abstractmethod
#     def play(self):
#         ...



# @dataclass
# class DataInstrumentMixin:    # Mixin é um objeto que deve ser utilizado junto com outra classe
#     name: str
#     sound: str
#     kind: InstrumentalKind


# class Instrument(DataInstrumentMixin, ABCInstrument):
#     ...



# @dataclass
# class Guitar(Instrument):
#     sound: str = "Ding Ding Ding"
#     kind: InstrumentalKind = InstrumentalKind.string

#     def play(self):
#         return self.sound

# @dataclass
# class Flaute(Instrument):
#     sound: str = "Flu Flu Flu"
#     kind: InstrumentalKind = InstrumentalKind.wind

#     def play(self):
#         return self.sound













from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List


class InstrumentalKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"


class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...



@dataclass
class DataInstrumentMixin:    # Mixin é um objeto que deve ser utilizado junto com outra classe
    name: str
    sound: str
    kind: InstrumentalKind
    colors: List[str] = field(default_factory=list)


class Instrument(DataInstrumentMixin, ABCInstrument):
    ...



@dataclass
class Guitar(Instrument):
    sound: str = "Ding Ding Ding"
    kind: InstrumentalKind = InstrumentalKind.string
    colors: List[str] = field(default_factory=lambda: ['red', 'black'])

    def play(self):
        return self.sound


@dataclass
class ElectricGuitar(Guitar):
    sound: str = "Wha Wha Wha"

    def play(self, distortion="wave"):
        return_from_base_class = super().play()
        if distortion is Distortion.wave:
            return "~~~".join(return_from_base_class.split())
        elif distortion is Distortion.whisper:
            return "...".join(return_from_base_class.split())

        return return_from_base_class



@dataclass
class Flaute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: InstrumentalKind = InstrumentalKind.wind
    colors: List[str] = field(default_factory=lambda: ['brown', 'white']) 

    def play(self):
        return self.sound