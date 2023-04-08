from instruments import Instrument, Guitar, Flaute, ElectricGuitar, Distortion

# x = Instrument()

gianini = Guitar("Gianini m2")
print(gianini.play())
print(gianini.colors)


flaute = Flaute("Yamanha", colors=["silver"])
print(flaute.play())
print(flaute.colors)


lespaul = ElectricGuitar("lespaul m1")
print(lespaul.play(distortion=Distortion.whisper))
