import math

from pyplanet.views.generics.widget import WidgetView
from pyplanet.views.template import TemplateView
from pyplanet.utils import times
import logging


class RadarView(WidgetView):
    
    widget_x = 0
    widget_y = 0

    template_name = 'radar/radarwidget.xml'

    def __init__(self, app):
        super().__init__(self)
        self.app = app
        self.manager = app.context.ui
        self.id = 'pyplanet__widgets_radar'
        self.paths = []

    async def update_checkpoints(self, paths):
        self.paths = []
        for cps in paths.values():
            cps = [s.replace("_", ",") for s in cps]
            cps = ["<"+c+">" for c in cps]
            self.paths.append(", ".join(cps))

    async def get_context_data(self):
        context = await super().get_context_data()

        # Add facts.
        context.update({
            'num_checkpoints': self.app.instance.map_manager.current_map.num_checkpoints,
            'paths': self.paths,
        })

        return context

class EventInjection(TemplateView):

    template_name = 'radar/event_injection.xml'

    def __init__(self, app, callback):
        super().__init__(self)
        self.app = app
        self.manager = app.context.ui
        self.id = 'pyplanet__views_radar_event'
        self.callback = callback

    async def handle_catch_all(self, player, action, values, **kwargs):
        action_name = "checkpoint__"
        if action.startswith(action_name):
            data = action[len(action_name):].split("|")
            if len(data) == 2 and data[1].isdigit():
                await self.callback(player, data[0], int(data[1]))

