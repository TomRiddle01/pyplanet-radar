# pyplanet-radar

This is a plugin for [PyPlanet](https://github.com/PyPlanet/PyPlanet/).
It also depends on [Checkpoint Verifier](https://github.com/TomRiddle01/pyplanet-checkpoint-verifier/).

It adds a live radar that displays the location of multiple objects.

- Other players (in blue)
- All checkpoints (in grey)
- All taken checkpoints (in grey but smaller)
- The next checkpoint (in yellow)*
- Possible next checkpoints if the plugin ins unsure (in orange)*
- finish line (in red)

\* Depends on the recorded Checkpoint order of [Checkpoint Verifier](https://github.com/TomRiddle01/pyplanet-checkpoint-verifier/) and therefore may sometimes be wrong.


The next checkpoint as seen on the image is directly in front of the car and is displayed in yellow on the radar in the bottom left.
The position of the radar may be changed by clicking on it.
![Radar Example](https://i.imgur.com/deiJjSy.png?1)
