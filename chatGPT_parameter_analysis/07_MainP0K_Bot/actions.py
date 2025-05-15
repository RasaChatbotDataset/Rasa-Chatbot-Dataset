import sqlite3
import random
from datetime import datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect('restaurant.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS reservation(code INTEGER, date TEXT, num_people INTEGER)")

    def retrieve_entry(self, code):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservation WHERE code=?", (code,))
            return cursor.fetchone()

    def delete_entry(self, code):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reservation WHERE code=?", (code,))
            return cursor.fetchone()

    def insert_entry(self, code, date, num_people):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor().execute("INSERT INTO reservation (code, date, num_people) VALUES (?, ?, ?)",
                                  (code, date, num_people))
            conn.commit()

class Reservation:
    def __init__(self, code, date, num_people):
        self.date = date
        self.code = code
        self.num_people = num_people

    def __str__(self):
        return f"Reservation details: Date={self.date}, Code={self.code}, Num People={self.num_people}"

class ActionManageDate(Action):
    def name(self) -> Text:
        return "action_save_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = Database("restaurant.db")
        db.create_table()

        date_rasa = tracker.get_slot("date")
        date_final = datetime.now().strftime('%Y-%m-%d')
        response = f"Vous avez réservé pour le : {date_final}"

        dispatcher.utter_message(text=response)
        return [SlotSet("date_convertie", date_final)]

class ActionManagePeople(Action):
    def name(self) -> Text:
        return "action_save_people"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_of_people = tracker.get_slot("people")
        response = f"Vous avez réservé pour : {number_of_people} personne(s)"
        dispatcher.utter_message(text=response)
        return []

class ActionConfirmation(Action):
    def name(self) -> Text:
        return "action_confirm_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot("date_convertie")
        people = tracker.get_slot("people")
        code = random.randint(1, 1000)

        db = Database("restaurant.db")
        db.insert_entry(code, date, people)

        response = (f"Vous avez réservé pour {people} personnes pour le {date}, "
                    f"votre numéro de réservation est le {code}")

        dispatcher.utter_message(text=response)
        return []

class AskRetrieveReservation(Action):
    def name(self) -> Text:
        return "action_retrieve_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        code = int(tracker.get_slot("code"))
        db = Database("restaurant.db")
        result = db.retrieve_entry(code)
        if result:
            reservation = Reservation(result[0], result[1], result[2])
            response = f"Voici votre code : {code}"
            dispatcher.utter_message(text=response)
            dispatcher.utter_message(text="Voici les détails de votre réservation :")
            dispatcher.utter_message(text=str(reservation))
        else:
            dispatcher.utter_message(text="Le code n'est pas valide")
        return []

class ActionDailyMenu(Action):
    def name(self) -> Text:
        return "action_daily_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.regal.fr/recettes/legumes/croquettes-de-legumes-au-zaatar-et-houmous-de-petits-pois-17354"
        dispatcher.utter_message(text="Je suis le menu du jour!")
        dispatcher.utter_message(text=url)
        return []

class ActionAllergens(Action):
    def name(self) -> Text:
        return "action_allergens"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.economie.gouv.fr/dgccrf/Publications/Vie-pratique/Fiches-pratiques/Allergene-alimentaire"
        dispatcher.utter_message(text="Je suis une liste d'allergènes")
        dispatcher.utter_message(text=url)
        return []

class ActionWholeMenu(Action):
    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.osmozbistro.com/la-carte/"
        dispatcher.utter_message(text="Je suis la carte")
        dispatcher.utter_message(text=url)
        return []

class ActionDeleteReservation(Action):
    def name(self) -> Text:
        return "action_delete_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        code = int(tracker.get_slot("code"))
        db = Database("restaurant.db")
        result = db.retrieve_entry(code)
        if result:
            reservation = Reservation(result[0], result[1], result[2])
            response = f"Voici votre code : {code}"
            dispatcher.utter_message(text=response)
            dispatcher.utter_message(text="Voici les détails de votre réservation :")
            dispatcher.utter_message(text=str(reservation))
            db.delete_entry(code)
            dispatcher.utter_message(text="Votre réservation est bien supprimée")
        else:
            dispatcher.utter_message(text="Le code n'est pas valide")
        return []
