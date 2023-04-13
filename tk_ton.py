import tkinter as tk
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/select_origin"

data = {
        "Origin airport":"",
        "Destination airport":"",
        "Date depart":"",
        "Flight name":"",
        "Package name":""
        }

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack(side = "top",fill = "both",expand = True)
        window.grid_columnconfigure(0, weight = 1)
        window.grid_rowconfigure(0, weight = 1)

        self.frames = {}
        for F in (SearchFlight,SelectFlight):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(SearchFlight)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class SearchFlight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_airportlist = requests.get(API_ENDPOINT1)


class SelectFlight():
    pass
