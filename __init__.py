from pyplanet.apps.config import AppConfig
from pyplanet.apps.core.trackmania import callbacks as tm_signals
from pyplanet.apps.core.maniaplanet import callbacks as mp_signals

from pyplanet.apps.core.maniaplanet.callbacks.player import player_chat

from pyplanet.apps.core.maniaplanet.models import Player

import asyncio

from .view import RadarView
from .view import EventInjection
#from .models import CheckpointOrder


class RadarApp(AppConfig):
    game_dependencies = ['trackmania']
    mode_dependencies = ['TimeAttack']
    app_dependencies = ['core.maniaplanet']
    


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def on_init(self):
        await super().on_init()

    async def on_stop(self):
        await super().on_stop()

    async def on_destroy(self):
        await super().on_destroy()

    async def on_start(self):
        await super().on_start()

        #tm_signals.finish.register(self.on_finish)
        #tm_signals.give_up.register(self.on_give_up)
        tm_signals.start_countdown.register(self.on_start_countdown)
        mp_signals.map.map_begin.register(self.on_map_begin)


        self.widget = RadarView(self)
        #self.event_injection = EventInjection(self, self.on_checkcheck_checkpoint)

        await self.widget.display()
        #await self.event_injection.display()


    async def on_map_begin(self, **kwargs):
        await self.widget.display()
        pass

    async def on_start_countdown(self, time, player, flow):
        await self.widget.display()
        pass

