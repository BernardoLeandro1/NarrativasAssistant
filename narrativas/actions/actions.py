# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionSayFriends(Action):

    def name(self) -> Text:
        return "action_say_friends"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name") == "Fallen":
            dispatcher.utter_message(text="Fallen is a good friend of mine")
        elif tracker.get_slot("name") == "Sir Alden" or tracker.get_slot("name") == "Alden":
            dispatcher.utter_message(text="Sir Alden is a good friend of mine")
        elif tracker.get_slot("name") == "Mira":
            dispatcher.utter_message(text="Mira is a good friend of mine")
        else:
            dispatcher.utter_message(text="My friends are Fallen, Sir Alden and Mira.")

        return []


class ActionMeetFriends(Action):

    def name(self) -> Text:
        return "action_meet_friends"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name") == "Fallen":
            dispatcher.utter_message(text="I met Fallen after Sir Alden told me to go talk to her about the Valloria's Stormbringer. She was working at her dad's Tavern in middle of the Capital City and I had to gain her trust by completing a side mission for her.")
        elif tracker.get_slot("name") == "Sir Alden" or tracker.get_slot("name") == "Alden":
            dispatcher.utter_message(text="I met Sir Alden during a crisis when villages near the capital were under mysterious attacks. He sought my help to decode symbols found at a crime scene. We rode through the rain to a village where I worked all night, discovering the symbols were part of a dark ritual. Our successful collaboration and mutual respect grew from there. Over several missions, we formed a strong alliance. So, when Malakar's threat emerged, Sir Alden knew he could rely on me.")
        elif tracker.get_slot("name") == "Mira":
            dispatcher.utter_message(text="I met Mira in the middle of my quest with Sir Alden and Fallen. She was from Rivertown, and she was near the Old Stone Bridge that had been destroyed by Malakar. She told us she was trying to fix the bridge but she couldn't because Malakar took her strength away when he took her Crystal of Lareth. She joined us in our quest after we promised to find her Crystal.")
        else:
            dispatcher.utter_message(text="I don't know them")

        return []

class ActionOpinionFriends(Action):

    def name(self) -> Text:
        return "action_opinion_friends"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name") == "Fallen":
            dispatcher.utter_message(text="Fallen? She's... intriguing, to say the least. There's a mystery about her, like she's carrying the weight of her past on her shoulders. Some might find her aloof, distant even, but I sense there's more to her than meets the eye.")
        elif tracker.get_slot("name") == "Sir Alden" or tracker.get_slot("name") == "Alden":
            dispatcher.utter_message(text="Sir Alden? He's a good man, no doubt. But there's an air about him, a sternness that can be intimidating. Some find it reassuring, like a shield against the world's troubles. Others, well, they might see him as too rigid, too set in his ways. But when the chips are down, there's no one I'd rather have by my side. He has AURA!")
        elif tracker.get_slot("name") == "Mira":
            dispatcher.utter_message(text="Mira is like a beacon of light in the darkest of times. Her unwavering faith and devotion to her beliefs are truly inspiring. Despite facing numerous challenges, she never loses her resolve. Having her with us on this journey... well, it makes all the difference.")
        else:
            dispatcher.utter_message(text="I have no opinion on that")

        return []

class ActionObjectsUse(Action):

    def name(self) -> Text:
        return "action_objects_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("object") == "Valloria's Stormbringer":
            dispatcher.utter_message(text="The Valloria's Stormbringer is a legendary artifact, forged in the heart of a raging tempest by ancient sorcerers of unparalleled skill. It is said to be a sword of immense power. The Stormbringer is both a symbol of authority and a weapon of unparalleled might, wielded by the bravest champions of Valloria in times of dire need.")
        elif tracker.get_slot("object") == "Map of Realms":
            dispatcher.utter_message(text="It's more than just a piece of parchment with markings on it; it's a guide, a lifeline in this vast and unpredictable world. Imagine a finely crafted map, adorned with intricate illustrations depicting the landscapes, cities, and pathways of our realm. But it's not just for show; this map has a magic of its own. It's enchanted to reveal hidden routes, warn of dangers ahead, and even provide glimpses into places unseen. Without it, our journey would be like sailing blind through a stormy sea.")
        elif tracker.get_slot("object") == "Arcane's Diary":
            dispatcher.utter_message(text="Imagine a book bound in leather, its pages etched with ancient runes glowing softly with inner power. It held the dark secrets of Malakar, the malevolent sorcerer who sought to plunge our kingdom into eternal darkness. Breaking its seals unleashed a torrent of dark energy, corrupting everything it touched. Yet, within its pages, I believe that lays the key to understanding Malakar's power, his weaknesses, and the dark spells he wielded.")
        elif tracker.get_slot("object") == "Crystal of Lareth":
            dispatcher.utter_message(text="It's a remarkable artifact, truly. Picture a radiant gemstone, shimmering with divine light, imbued with the power to amplify and channel divine energies. It's said to enhance healing spells, banish darkness, and inspire hope in those who wield it. A true beacon of light in the fight against the forces of evil.")
        elif tracker.get_slot("object") == None:
            dispatcher.utter_message(text="Troughout our quest we needed to use a lof of different objects. The main ones where the Map of Realms, the Valloria's Stormbringer, the Arcane's Diary and the Crystal of Lareth.")
        else:
            dispatcher.utter_message(text="i don't know that object")

        return []

class ActionPlaces(Action):

    def name(self) -> Text:
        return "action_places"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("place") == "Valloria":
            dispatcher.utter_message(text="Valloria, ah, it's more than just a city to me—it's my home. he winding streets, the towering spires, they're all familiar sights that I've grown up with. But what truly captivates me is its rich history, hidden within every cobblestone and whispered in every gust of wind. It's a city alive with stories, where the past mingles with the present, inviting me to unravel its mysteries at every turn.")
        elif tracker.get_slot("place") == "Eclipse Hill":
            dispatcher.utter_message(text="It's a place that sends shivers down your spine just thinking about it. As you climb, the air seems charged with a strange energy, and the sky above turns an ominous shade of red. When you reach the summit, you're greeted by a sight that's both awe-inspiring and chilling—twisted shadows dance across the jagged cliffs, casting an eerie glow over everything.")
        elif tracker.get_slot("place") == "Cavern of Echoes":
            dispatcher.utter_message(text="The Cavern of Echoes, now that's a place shrouded in mystery and wonder. Deep within the heart of the northern forest lies this labyrinthine network of caves and tunnels, where the very walls seem to whisper secrets of ages past. It's a place of trials and tribulations, where one must confront their fears and test their mettle against the unknown. I know we did it.")
        elif tracker.get_slot("place") == "Rivertown":
            dispatcher.utter_message(text="Rivertown, ah, it's a quaint little hamlet nestled along the banks of the gentle river that meanders through our lands. It may not boast the grandeur of Valloria, but it holds its own charm. The rustic cottages, the bustling market square, and the serene riverbanks—it's a place where time seems to slow down, where the rhythms of life flow as steadily as the river itself. It's a haven for weary travelers and a beacon of warmth and hospitality in our realm.")
        elif tracker.get_slot("place") == None:
            dispatcher.utter_message(text="Our quest started in Valloria. Me, Sir Alden and Fallen. We went to Rivertown, east of the gates. There we met Mira, and she joined us. We then, went through the forest and entered the Cavern of Echoes. Afterwatds we arrived at the Eclipse Hill.")
        else:
            dispatcher.utter_message(text="i don't know that place")

        return []

class ActionParents(Action):

    def name(self) -> Text:
        return "action_parents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("parent") == "mother":
            dispatcher.utter_message(text="My mother passed away when I was very young and I have little to no memories of her.")
        elif tracker.get_slot("parent") == "father":
            dispatcher.utter_message(text="Me and my father used to be together always and he taught me evertyhing I know. When I was a 12 years old he got very sick due to Malakar's curses.")
        elif tracker.get_slot("parent") == None:
            dispatcher.utter_message(text="Me and my father used to be together always and he taught me evertyhing I know. When I was a 12 years old he got very sick due to Malakar's curses. My mother passed away when I was very young and I have little to no memories of her.")
        else:
            dispatcher.utter_message(text="i don't know who that is.")

        return []