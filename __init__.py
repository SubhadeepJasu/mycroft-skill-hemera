"""
 Copyright (c) 2018-2019 Subhadeep Jasu <subhajasu@gmail.com>
 Copyright (c) 2018-2019 Hannes Schulze <haschu0103@gmail.com>
 Copyright (c) 2018-2019 Christopher M

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public
 License as published by the Free Software Foundation; either
 version 3 of the License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU General Public License 
 along with this program. If not, see <https://www.gnu.org/licenses/>.

 Authored by: Subhadeep Jasu
"""
 
from adapt.intent import IntentBuilder
from mycroft.api import Api
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG
from mycroft.util.log import getLogger
from mycroft.messagebus.message import Message


__author__ = 'SubhadeepJasu'
LOGGER = getLogger(__name__)

# Each skill is contained within its own class, which inherits base methods
class HemeraSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(HemeraSkill, self).__init__(name="HemeraSkill")

    @intent_file_handler('LaunchApp.intent')
    def handle_launch_app_intent(self, message):
        app_query = message.data ["app_name"];
        LOGGER.debug("Launch App: %s" % app_query)
        self.bus.emit(Message("hemera_action",  
                              {'type': 'launch',  
                               'app': app_query}))  
    @intent_file_handler('HemeraName.intent')
    def handle_launch_app_intent(self, message):
        self.speak_dialog("My name is Hemera, I am a digital personal assitant based on Mycroft")


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return HemeraSkill()

