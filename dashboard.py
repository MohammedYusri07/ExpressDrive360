import customtkinter as ctk
import tkintermapview
import tk_tools as tkt
from tkdial import Meter



ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Dashboard")
# app.overrideredirect(True)  # remove window border
app.attributes('-fullscreen',True)
#app.state('zoomed')  # Maximize the window
app.focus_force()  # Force the window to gain focus
#app.geometry("800x600")  # Set the window size

# Add a red close button
def close_program():
    app.destroy()

frame_0 = ctk.CTkFrame(master=app)
frame_0.place(relx=0.03, rely=0.05, relwidth=0.45, relheight=0.45)

frame_1 = ctk.CTkFrame(master=app)
frame_1.place(relx=0.03, rely=0.51, relwidth=0.45, relheight=0.45)

frame_2 = ctk.CTkFrame(master=app)
frame_2.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.905)

close_button = ctk.CTkButton(master=app, text="X",command=close_program,fg_color="red", hover_color="#ff6666")
close_button.place(relx=0.955, rely=0.005, relwidth=0.04, relheight=0.03)


my_font = ctk.CTkFont(family="digital-7", size=100  )
speed_label = ctk.CTkLabel(frame_0, text="100" ,font=my_font)
speed_label.pack(padx=(50,0), side="left")

speed_label = ctk.CTkLabel(frame_0, text="km/h" )
speed_label.pack(padx=10 , side="left")

meter1 = Meter(frame_0, radius=300, start=50, end=-50, border_width=0,
               fg="", text_color="white", start_angle=-45, end_angle=270,
               text_font="DS-Digital 30", scale_color="white", needle_color="red")
meter1.set_mark(140, 160) # set red marking from 140 to 160
meter1.set(-5)
meter1.pack(padx=10,side="left")

# create map widget
map_widget = tkintermapview.TkinterMapView(frame_1, corner_radius=5)
map_widget.pack(padx=10,pady=10,fill="both",expand=True)

# set current widget position and zoom
map_widget.set_position(7.4089, 80.6080)  # Paris, France
map_widget.set_zoom(60)
marker_3 = map_widget.set_marker(7.4089, 80.6080)


ot_font = ctk.CTkFont(family="Robot Crush", size=35  )
entry = ctk.CTkEntry(frame_2, placeholder_text="Vehicle is going to OverTake",font=ot_font,width=300,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.1,rely=0.1,relheight=0.08, relwidth=0.8)

entry = ctk.CTkEntry(frame_2, placeholder_text="Do Not OverTake !!!",font=ot_font,width=300,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.1,rely=0.3,relheight=0.08, relwidth=0.8)

entry = ctk.CTkEntry(frame_2, placeholder_text="Slow Down !!!",font=ot_font,width=300,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.1,rely=0.5,relheight=0.08, relwidth=0.8)

def send_event():
    print("button pressed")

send_button = ctk.CTkButton(frame_2, text="Overtake", command=send_event)
send_button.place(relx=0.3, rely=0.7, relwidth=0.17, relheight=0.12)

def button_event():
    print("button pressed")

button = ctk.CTkButton(frame_2, text="Cruise Control", command=button_event)
button.place(relx=0.55, rely=0.7, relwidth=0.17, relheight=0.12)

app.mainloop()
