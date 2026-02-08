from operator import index
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.appbar import MDTopAppBar, MDActionBottomAppBarButton, MDFabBottomAppBarButton
from kivymd.uix.list import MDListItem
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePickerDialVertical
from kivymd.uix.pickers import MDModalDatePicker
from kivy.core.text import LabelBase
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText
from kivy.metrics import dp
from kivy.core.audio import SoundLoader
from kivymd.uix.imagelist import MDSmartTile, MDSmartTileImage
from kivymd.uix.list import *
from kivymd.uix.fitimage import FitImage
from kivy.core.image import Image as CoreImage
import json
import ssl
from paho.mqtt import client as mqtt
from PIL import Image
from io import BytesIO
import os
import requests
import webbrowser

BROKER = "a04c8de99e5d4ac2826036b475aa9e1e.s1.eu.hivemq.cloud"
PORT = 8883



openingsound = SoundLoader.load('openingsound.mp3')
clicksound = SoundLoader.load('click.mp3')
completionsound = SoundLoader.load('complete.mp3')

LabelBase.register(
    name="title-font",  # Internal name for the font
    fn_regular="title-font.ttf"  # Your TTF file in the same folder as main.py
)

def getimg():
    url = "https://drive.google.com/drive/folders/1uaIZ_oxYKYyZ0fafNNb3ooQ7X9Lvqmol?usp=sharing"
    webbrowser.open(url)



def on_message(client, userdata, msg):
    with open("recieve.json", "r") as f:
            record = json.load(f)

    data = json.loads(msg.payload.decode())
    print("Received:", data)


    record['update'].append(data)
    with open("recieve.json", "w") as f:
            json.dump(record, f, indent= 4)

# Source - https://stackoverflow.com/a/77985329
# Posted by Brits, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-29, License - CC BY-SA 4.0

client = mqtt.Client(client_id="python-client", callback_api_version=1)
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.on_message = on_message
client.connect(BROKER, PORT)

client.subscribe("home/esp8266/status")
client.subscribe("espcam")
client.on_message = on_message
client.loop_start()

def connect_mqtt(USERNAME, PASSWORD):
    
    client.username_pw_set(USERNAME, PASSWORD)
    


class topmainscreenbar (MDTopAppBar):
    pass

class MainScreen(MDScreen):
    pass
class LoginScreen(MDScreen):
    pass

class createphoto(MDSmartTile):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Createupdatescreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

class item(MDListItem):
    pass



        

"""
class updatelist (MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.spacing = "12dp"

    def add_item(self):
        # Dynamically add a new item to the list with an icon
        icon = 'bell'  # You can change this to any Material icon name
        item = MDListItem(
            text=f"Item {len(self.root.ids.md_list.children) + 1}",
            secondary_text="awinda",
            tertiary_text="daw",
            icon=icon,
            icon_color=(1, 1, 0, 1)
        )
        self.root.ids.md_list.add_widget(item)

    def remove_item(self):
        # Remove the last item from the list (if available)
        if self.root.ids.md_list.children:
            self.root.ids.md_list.remove_widget(self.root.ids.md_list.children[0])

"""

class MyApp(MDApp):

    def build(self):
        
        self.title = "IV-DV Research application"
        self.theme_cls.primary_palette = "#120F47"
        self.theme_cls.secondary_palette = "#82A5DA"
        self.theme_cls.background_color = "#120F47"  
        self.theme_cls.theme_style = "Light"
        self.icon = "icon.jpeg"
        self.theme_cls.font_styles["Custom"] = {
            "large": {
                "font-name": "nulshuck.otf",
                "font-size": "20sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            },
            "medium": {
                "font-name": "nulshuck.otf",
                "font-size": "22sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            },
            "small": {
                "font-name": "nulshuck.otf",
                "font-size": "12sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            }
        }

        self.theme_cls.font_styles["headingg"] = {
            "large": {
                "font-name": "goodtiming.otf",
                "font-size": "20sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            },

            "medium": {
                "font-name": "goodtiming.otf",
                "font-size": "20sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            },

            "small": {
                "font-name": "goodtiming.otf",
                "font-size": "10sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            }
        }

        self.theme_cls.font_styles["itemf"] = {
            "large": {
                "font-name": "item.otf",
                "font-size": "20sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            },

            "medium": {
                "font-name": "item.otf",
                "font-size": "20sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            },

            "small": {
                "font-name": "item.otf",
                "font-size": "10sp",
                "line-height": 1.2,
                "letter-spacing": "0.15sp"
            }
        }

        self.root = Builder.load_file('main.kv')
        openingsound.play()
        #self.root.ids.screenmanager.current = "mainscreen
        with open("profile.json", "r") as f:
            data = json.load(f)

        if data['User']['name'] == "":
            self.root.current = "silog"
        
        else:
            self.savelogin()
            self.root.current = "mainscreen"


    def load_images(self):
        getimg()
        try:
            url = "http://192.168.1.10:5000/thumbnails"  # your LAN IP
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            image_urls = response.json()
            grid = self.root.ids.grid
            grid.clear_widgets()

            for img_url in image_urls:
                r = requests.get(img_url, timeout=5)
                r.raise_for_status()
                data = BytesIO(r.content)
                ci = CoreImage(data, ext="jpg")

                # Use FitImage instead of Image
                img_widget = FitImage(
                    size_hint_y=None,
                    height=200,
                    source="",           # leave blank if using texture
                )
                img_widget.texture = ci.texture  # assign texture
                grid.add_widget(img_widget)

        except Exception as e:
            print("Failed to load thumbnails:", e)

    Name = "Larme"

    with open("profile.json", "r") as f:
        data = json.load(f)

    Name = data['User']['name']

    def checkitems(self):
        with open("schedule.json", "r") as f:
            data = json.load(f)

        self.root.ids.listahanedit.clear_widgets()

        for index, item in enumerate(data['Schedule']):
            item_widget = MDListItem(
                MDListItemHeadlineText(
                    text=(
                        f"In the day: {item['year']}-{item['month']}-{item['day']}\n"
                        f"Medecine 1, 2, 3: {item['chamber1time']}, "
                        f"{item['chamber2time']}, {item['chamber3time']} give at "
                        f"{item['hour']}:{item['minute']} ({item['type']})"
                    )
                ),
                MDListItemTrailingCheckbox(
                    on_active=lambda checkbox, value, w=None: print(f"Checkbox {index} is {'active' if value else 'inactive'}")
                )
            )

            # store index on the parent
            item_widget.schedule_index = index

            self.root.ids.listahanedit.add_widget(item_widget)

    def remove_schedule(self):
    # 1️⃣ Load JSON
        with open("schedule.json", "r") as f:
            data = json.load(f)

        # 2️⃣ Collect all list items to remove
        items_to_remove = []
        indices_to_remove = []

        for child in self.root.ids.listahanedit.children[:]:
            # check if any trailing checkbox in this list item is active
            for w in child.walk():
                if isinstance(w, MDListItemTrailingCheckbox) and w.active:
                    items_to_remove.append(child)
                    # store index of JSON item
                    index = getattr(child, "schedule_index", None)
                    if index is not None:
                        indices_to_remove.append(index)
                    break  # only one checkbox per list item

        # 3️⃣ Remove from Kivy list
        for item_widget in items_to_remove:
            self.root.ids.listahanedit.remove_widget(item_widget)

        # 4️⃣ Remove from JSON safely (highest index first)
        for i in sorted(indices_to_remove, reverse=True):
            if 0 <= i < len(data['Schedule']):
                data['Schedule'].pop(i)

        # 5️⃣ Save updated JSON
        with open("schedule.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"Removed {len(items_to_remove)} schedule(s) successfully!")
                    


    def add_image(self):
        tile = MDSmartTile(
            source="latest.jpg",
            size_hint=(None, None),
            size=("150dp", "150dp")
        )
        self.root.ids.grid.add_widget(tile)




    def savelogin (self):
        with open("profile.json", "r") as f:
            data = json.load(f)
        
        

        if data['User']['name'] == "":
            inputname = self.root.ids.username.text
            ngaran = self.root.ids.ngaran.text
            Pd = self.root.ids.lockngaran.text
            data['User']['name'] = inputname
            data['User']['ngaran'] = ngaran
            data['User']['password'] = Pd
            with open("profile.json", "w") as f:
                json.dump(data, f, indent= 4)

            with open("profile.json", "r") as f:
                data = json.load(f)

            print(f"recall {data['User']['name']}")
            self.root.ids.mainname.text = f"Hi {data['User']['name']}!"
            openingsound.play()
        else:
            with open("profile.json", "r") as f:
                data = json.load(f)

            print(f"recall {data['User']['name']}")
            self.root.ids.mainname.text = f"Hi, {data['User']['name']}!"
            connect_mqtt(data['User']['ngaran'], data['User']['password'])
            openingsound.play()

        


        with open("recieve.json", "r") as f:
            data = json.load(f)


        for index ,update in enumerate(data['update']):
            screen = Createupdatescreen(name = "screen"+str(index), id = "screen"+str(index))
            """screen.add_widget(
                MDBoxLayout(
                    MDList(
                        MDListItem(MDListItemHeadlineText(text="Back"), on_press=lambda instance: self.change_screen("mainscreen")),
                        MDListItem(MDListItemHeadlineText(text="In the day:" + str(data['update'][index]['Date']))),
                        MDListItem(MDListItemHeadlineText(text="Blood Pressure: " + str(data['update'][index]['bpm']) + " bpm"))
                    ),
                    MDGridLayout(
                        MDSmartTile(
                            MDSmartTileImage(source=str(data['update'][index]['img'][0]), radius=[dp(24), dp(24), 0, 0]),
                            overlap=False,
                            size_hint_y=None,
                            size_hint_x =None,
                            size =(dp(150), dp(150))
                            ),
                        MDSmartTile(
                            MDSmartTileImage(source=str(data['update'][index]['img'][1]), radius=[dp(24), dp(24), 0, 0]),
                            overlap=False,
                            size_hint_y=None,
                            size_hint_x =None,
                            size =(dp(150), dp(150))
                            ),
                        MDSmartTile(
                            MDSmartTileImage(source=str(data['update'][index]['img'][2]), radius=[dp(24), dp(24), 0, 0]),
                            overlap=False,
                            size_hint_y=None,
                            size_hint_x =None,
                            size =(dp(150), dp(150))
                            ),
                        
                        cols=2,
                        spacing=dp(10)

                    ),
                    orientation="vertical",
                    padding=dp(10),
                    size_hint_y=0.9,
                    size_hint_x=0.9,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}

                )
            )
            self.root.add_widget(screen)        """
            self.root.ids.listahan.add_widget(
                item(
                    MDListItemHeadlineText(
                        text=(
                            f"In the day: {data['update'][index]['Date']}\n"
                            f"Blood Pressure: {data['update'][index]['bpm']} bpm"
                        ), 

                        font_style="itemf"
                  
                    )
                    
                )
            )


    def change_theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.root.ids.listcont.md_bg_color = self.theme_cls.secondaryColor
            self.root.ids.logintitle.text_color = self.theme_cls.primaryColor
            clicksound.play()

            
        else:
            self.theme_cls.theme_style = "Dark"
            self.root.ids.listcont.md_bg_color = self.theme_cls.primaryColor
            self.root.ids.logintitle.text_color = self.theme_cls.secondaryColor
            clicksound.play()


        # r = requests.get("http://server-ip:5000/report/esp8266_01")

    def change_screen(self, screen_name):
        self.root.current = screen_name
        print(f"Changed to screen: {screen_name}")

    def refresh_callback(self, interval):
        '''
        A method that updates the state of your application
        while the spinner remains on the screen. '''
        self.root.ids.box.clear_widgets()
        if self.x == 0:
            self.x, self.y = 15, 30

        else:
            self.x, self.y = 0, 15
            self.set_list()
            self.root.ids.refresh_layout.refresh_done()
            self.tick = 0


            Clock.schedule_once(refresh_callback, 1)

    def butest(self):
        print("napindot na")

    def set(self, num):
        self.chamnono = num
        print("Chamber number set to:", self.chamnono)


    def show_time_picker(self, chamno):
        self.chamnono = chamno
        # Create the time picker dialog
        time_picker = MDTimePickerDialVertical()
        time_picker.bind(on_ok=self.on_time_ok)
        time_picker.bind(on_cancel=self.on_time_cancel)
        time_picker.open()

    

    def on_time_cancel(self, instance_time_picker):
        instance_time_picker.dismiss()
        clicksound.play()

    chamber1settime = "00:00:00"
    chamber2settime = "00:00:00"
    chamber3settime = "00:00:00"
    chamnono = None
    hour = None
    minute = None
    year = None
    month = None
    day = None
    type = "custom"
    everyday = "false"



    def on_time_ok(self, instance_time_picker):
        # Print the selected time to the console
        instance_time_picker.dismiss()
        print("Selected time:", instance_time_picker.time)
        clicksound.play()
        
        time_str = str(instance_time_picker.time)
        hour_str, minute_str, second_str = time_str.split(':')

        
        

    
        if self.chamnono == 1:
            chamber1settime = instance_time_picker.time
            print("Chamber 1 time set to:", chamber1settime)

        
            self.hour = hour_str
            print("Hour set to:", self.hour)
            self.minute = minute_str
            print("Minute set to:", self.minute)

            print("successfull to set the schedule")


        

        self.root.ids.chamber1time.text = f"{hour_str}:{minute_str}"
        


    def disable_sched(self, checkbox, value):
        if value:
            print('The checkbox now', checkbox, 'is active', 'and', checkbox.state, 'state')
            self.root.ids.datepickerbutton.disabled = True
            self.everyday = "true"
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
            self.root.ids.datepickerbutton.disabled = False
            self.everyday = "false"

    i = 0
    def saveschedule(self):
        with open("schedule.json", "r") as f:
            data = json.load(f)

        

        if self.everyday == "true":
            type = "everyday"
        else:
            type = "custom"
        
        if self.root.ids.checkcham1.active:
            cham1 = 1

        else: 
            cham1 = 0

        if self.root.ids.checkcham2.active:
            cham2 = 1
        else:
            cham2 = 0
        if self.root.ids.checkcham3.active:
            cham3 = 1
        else:
            cham3 = 0


        structure = {
            "type": type,
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "hour": int(self.hour),
            "minute": int(self.minute),
            "chamber1time": cham1,
            "chamber2time": cham2,
            "chamber3time": cham3
        }

        data['Schedule'].append(structure)
        with open("schedule.json", "w") as f:
            json.dump(data, f, indent= 4)

        print("successfull to save the schedule")
        completionsound.play()

        with open("schedule.json", "r") as f:
            data_dict = json.load(f)  # note: json.load(), not loads()
            
        # Convert Python dict/list to JSON string
        data_str = json.dumps(data_dict)

        client.publish("test", data_str)
        client.publish("home/esp8266/cmd", data_str)
        self.savelogin()
            



    

    def on_select_day(self, instance_date_picker, number_of_day):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The selected date is:{number_of_day}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
            
        ).open()
        
    
    def on_select_month(self, instance_date_picker, number_of_month):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The selected date is:{number_of_month}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
            
        ).open()


    def on_select_year(self, instance_date_picker, number_of_year):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The selected date is:{number_of_year}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
            
        ).open()
        

    def on_ok(self, instance_date_picker):
        print(instance_date_picker.get_date()[0])
        instance_date_picker.dismiss()

        clicksound.play()

        self.year = instance_date_picker.year
        self.month = instance_date_picker.month
        self.day = instance_date_picker.day

        self.root.ids.date.text = str(instance_date_picker.get_date())

    def on_cancel(self, instance_date_picker):
        instance_date_picker.dismiss()
        clicksound.play()

    def show_date_picker(self, *args):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_select_day=self.on_select_day)
        date_dialog.bind(on_select_month=self.on_select_month)
        date_dialog.bind(on_select_year=self.on_select_year)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.open()



#MDScrollViewRefreshLayout:
    #id: refresh_layout
    #refresh_callback: app.refresh_callback
    #root_layout: root
    #spinner_color: "red"
    #circle_color: "white"




if __name__ == '__main__':
    MyApp().run()