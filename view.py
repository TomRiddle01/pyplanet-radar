import math

from pyplanet.views.generics.widget import WidgetView
from pyplanet.views.template import TemplateView
from pyplanet.utils import times
import logging


class RadarView(WidgetView):
    
    widget_x = 40
    widget_y = -45

    template_name = 'radar/radarwidget.xml'

    def __init__(self, app):
        super().__init__(self)
        self.app = app
        self.manager = app.context.ui
        self.id = 'pyplanet__widgets_radar'


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

