from pyplanet.apps.config import AppConfig
from pyplanet.apps.core.trackmania import callbacks as tm_signals
from pyplanet.apps.core.maniaplanet import callbacks as mp_signals

from pyplanet.apps.core.maniaplanet.models import Player

from tomriddle.checkcheck.models import CheckpointOrder

import asyncio

from .view import RadarView
from .view import EventInjection


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

        tm_signals.start_countdown.register(self.on_start_countdown)
        mp_signals.map.map_begin.register(self.on_map_begin)

        self.widget = RadarView(self)

        await self.update_paths();
        await self.widget.display()

    async def on_map_begin(self, **kwargs):
        await self.update_paths();
        await self.widget.display()
        pass

    async def on_start_countdown(self, time, player, flow):
        # await self.update_paths();
        await self.widget.display()
        pass

    async def update_paths(self):
        paths = await CheckpointOrder.objects.execute(
            CheckpointOrder.select(CheckpointOrder, Player)
                .join(Player)
                .where(CheckpointOrder.map_id == self.instance.map_manager.current_map.get_id())
        )
        map_checkpoints = self.instance.map_manager.current_map.num_checkpoints

        finished_paths = {}
        for entry in list(paths):
            cps = entry.checkpoints.split("|")
            if map_checkpoints == len(cps):
                finished_paths[entry.player.login] = cps

        await self.widget.update_checkpoints(finished_paths)

