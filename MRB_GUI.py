import MRB_Constants
import tkinter as tk
import threading
import json


class MRB_GUI:
    def __init__(self, controller):
        """Starting point when module is the main routine."""
        self.root = tk.Tk()
        self.top = self.Toplevel(self.root)

        self.load_settings()

        controller.set_gui(self)

        t1 = threading.Thread(target=controller.gui_thread)
        t1.setDaemon(True)
        t1.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.after(0, controller.gui_task)
        self.root.after(0, self.update_gui)
        self.root.mainloop()

    def update_gui(self):
        new_state = self.top.program_state.get()
        if new_state != self.top.previous_state:
            if new_state == MRB_Constants.STATE_CALIBRATION:
                self.top.Ser1_scale.config(state="normal")
                self.top.Ser2_scale.config(state="normal")
                self.top.Ser3_scale.config(state="normal")
            else:
                self.top.Ser1_scale.config(state="disabled")
                self.top.Ser2_scale.config(state="disabled")
                self.top.Ser3_scale.config(state="disabled")

        self.top.previous_state = new_state

        self.root.after(50, self.update_gui)

    def get_settings(self):
        return {
            "PID": {
                "P": self.top.Kp_scale.get(),
                "I": self.top.Ki_scale.get(),
                "D": self.top.Kd_scale.get()
            },
            "SerOffsets": {
                "1": self.top.Ser1_scale.get(),
                "2": self.top.Ser2_scale.get(),
                "3": self.top.Ser3_scale.get()
            }
        }

    def set_settings(self, settings):
        self.top.Kp_scale.set(settings["PID"]["P"])
        self.top.Ki_scale.set(settings["PID"]["I"])
        self.top.Kd_scale.set(settings["PID"]["D"])
        self.top.Ser1_scale.set(settings["SerOffsets"]["1"])
        self.top.Ser2_scale.set(settings["SerOffsets"]["2"])
        self.top.Ser3_scale.set(settings["SerOffsets"]["3"])

    def save_settings(self):
        with open("MRB_settings.json", 'w') as json_file:
            json.dump(self.get_settings(), json_file, indent=4)

    def load_settings(self):
        try:
            with open("MRB_settings.json", 'r') as json_file:  # Load stat JSON file
                settings = json.load(json_file)
                if settings:
                    self.set_settings(settings)
        except FileNotFoundError:
            pass

    def get_root(self):
        return self.root

    def get_top(self):
        return self.top

    def set_connected(self, state):
        if state:
            self.top.Connection_label.configure(background="#1dc104")
            self.top.Connection_label.configure(text=MRB_Constants.CONNECTED)
        else:
            self.top.Connection_label.configure(background="#e00606")
            self.top.Connection_label.configure(text=MRB_Constants.DISCONNECTED)

    def get_program_state(self):
        return self.top.program_state.get()

    def get_select_mode(self):
        return self.top.selection_mode.get()

    def get_servo_offsets(self):
        return self.top.Ser1_scale.get(), self.top.Ser2_scale.get(), self.top.Ser3_scale.get()

    def on_closing(self):
        self.save_settings()
        self.root.destroy()

    class Toplevel:
        def __init__(self, top_layer):
            """This class configures and populates the toplevel window.
               top is the toplevel containing window."""
            top_layer.geometry("834x738+569+208")
            top_layer.title("Ping Pong Ding Dong")
            top_layer.configure(background="#d9d9d9")

            self.program_state = tk.StringVar(None, MRB_Constants.STATE_IDLE)
            self.previous_state = "Off"
            self.selection_mode = tk.StringVar(None, MRB_Constants.BALL_COLOR_CALIBRATION)

            self.Selection_frame = tk.LabelFrame(top_layer)
            self.Selection_frame.place(relx=0.791, rely=0.081, relheight=0.156, relwidth=0.192)
            self.Selection_frame.configure(text="Selection Tool")
            self.Selection_frame.configure(background="#d9d9d9")
            self.Selection_frame.configure(width=160)

            self.Ball_color_calibration_button = tk.Button(self.Selection_frame)
            self.Ball_color_calibration_button.place(relx=0.063, rely=0.174, height=24, width=141, bordermode='ignore')
            self.Ball_color_calibration_button.configure(background="#d9d9d9")
            self.Ball_color_calibration_button.configure(text=MRB_Constants.BALL_COLOR_CALIBRATION)
            self.Ball_color_calibration_button.configure(command=lambda: self.set_select_state(self.Ball_color_calibration_button))
            self.Ball_color_calibration_button.configure(width=141)

            self.Servo_calibration_button = tk.Button(self.Selection_frame)
            self.Servo_calibration_button.place(relx=0.063, rely=0.435, height=24, width=141, bordermode='ignore')
            self.Servo_calibration_button.configure(background="#d9d9d9")
            self.Servo_calibration_button.configure(text=MRB_Constants.SELECT_SERVO_POS)
            self.Servo_calibration_button.configure(command=lambda: self.set_select_state(self.Servo_calibration_button))
            self.Servo_calibration_button.configure(width=141)

            self.Ball_destination_button = tk.Button(self.Selection_frame)
            self.Ball_destination_button.place(relx=0.063, rely=0.696, height=24, width=141, bordermode='ignore')
            self.Ball_destination_button.configure(background="#d9d9d9")
            self.Ball_destination_button.configure(text=MRB_Constants.SELECT_BALL_DEST)
            self.Ball_destination_button.configure(command=lambda: self.set_select_state(self.Ball_destination_button))
            self.Ball_destination_button.configure(width=141)

            self.PID_frame = tk.LabelFrame(top_layer)
            self.PID_frame.place(relx=0.791, rely=0.488, relheight=0.21, relwidth=0.192)
            self.PID_frame.configure(text='PID Controls')
            self.PID_frame.configure(background="#d9d9d9")
            self.PID_frame.configure(width=160)

            self.Kp_scale = tk.Scale(self.PID_frame, from_=0.0, to=100.0)
            self.Kp_scale.place(relx=0.188, rely=0.129, relwidth=0.763, relheight=0.0, height=42, bordermode='ignore')
            self.Kp_scale.configure(background="#d9d9d9")
            self.Kp_scale.configure(highlightbackground="#d9d9d9")
            self.Kp_scale.configure(highlightcolor="black")
            self.Kp_scale.configure(length="122")
            self.Kp_scale.configure(orient="horizontal")
            self.Kp_scale.configure(troughcolor="#d9d9d9")

            self.Ki_scale = tk.Scale(self.PID_frame, from_=0.0, to=100.0)
            self.Ki_scale.place(relx=0.188, rely=0.387, relwidth=0.763, relheight=0.0, height=42, bordermode='ignore')
            self.Ki_scale.configure(background="#d9d9d9")
            self.Ki_scale.configure(highlightbackground="#d9d9d9")
            self.Ki_scale.configure(highlightcolor="black")
            self.Ki_scale.configure(length="122")
            self.Ki_scale.configure(orient="horizontal")
            self.Ki_scale.configure(troughcolor="#d9d9d9")

            self.Kd_scale = tk.Scale(self.PID_frame, from_=0.0, to=100.0)
            self.Kd_scale.place(relx=0.188, rely=0.645, relwidth=0.763, relheight=0.0, height=42, bordermode='ignore')
            self.Kd_scale.configure(background="#d9d9d9")
            self.Kd_scale.configure(highlightbackground="#d9d9d9")
            self.Kd_scale.configure(highlightcolor="black")
            self.Kd_scale.configure(length="122")
            self.Kd_scale.configure(orient="horizontal")
            self.Kd_scale.configure(troughcolor="#d9d9d9")

            self.Kp_message = tk.Message(self.PID_frame)
            self.Kp_message.place(relx=0.063, rely=0.258, relheight=0.148, relwidth=0.113, bordermode='ignore')
            self.Kp_message.configure(background="#d9d9d9")
            self.Kp_message.configure(text='Kp')
            self.Kp_message.configure(width=18)

            self.Ki_message = tk.Message(self.PID_frame)
            self.Ki_message.place(relx=0.063, rely=0.516, relheight=0.148, relwidth=0.125, bordermode='ignore')
            self.Ki_message.configure(background="#d9d9d9")
            self.Ki_message.configure(text='Ki')
            self.Ki_message.configure(width=20)

            self.Kd_message = tk.Message(self.PID_frame)
            self.Kd_message.place(relx=0.063, rely=0.774, relheight=0.148, relwidth=0.125, bordermode='ignore')
            self.Kd_message.configure(background="#d9d9d9")
            self.Kd_message.configure(text='Kd')
            self.Kd_message.configure(width=20)

            self.ServoOffset_frame = tk.LabelFrame(top_layer)
            self.ServoOffset_frame.place(relx=0.791, rely=0.705, relheight=0.21, relwidth=0.192)
            self.ServoOffset_frame.configure(text='Servo offsets')
            self.ServoOffset_frame.configure(background="#d9d9d9")
            self.ServoOffset_frame.configure(width=160)

            self.Ser1_message = tk.Message(self.ServoOffset_frame)
            self.Ser1_message.place(relx=0.063, rely=0.258, relheight=0.148, relwidth=0.125, bordermode='ignore')
            self.Ser1_message.configure(background="#d9d9d9")
            self.Ser1_message.configure(text='#1')
            self.Ser1_message.configure(width=30)

            self.Ser2_message = tk.Message(self.ServoOffset_frame)
            self.Ser2_message.place(relx=0.063, rely=0.516, relheight=0.148, relwidth=0.106, bordermode='ignore')
            self.Ser2_message.configure(background="#d9d9d9")
            self.Ser2_message.configure(text='#2')
            self.Ser2_message.configure(width=60)

            self.Ser3_message = tk.Message(self.ServoOffset_frame)
            self.Ser3_message.place(relx=0.063, rely=0.774, relheight=0.148, relwidth=0.106, bordermode='ignore')
            self.Ser3_message.configure(background="#d9d9d9")
            self.Ser3_message.configure(text='#3')
            self.Ser3_message.configure(width=60)

            self.Ser1_scale = tk.Scale(self.ServoOffset_frame, from_=-15.0, to=15.0)
            self.Ser1_scale.place(relx=0.188, rely=0.129, relwidth=0.763, relheight=0.0, height=42, bordermode='ignore')
            self.Ser1_scale.configure(background="#d9d9d9")
            self.Ser1_scale.configure(highlightbackground="#d9d9d9")
            self.Ser1_scale.configure(highlightcolor="black")
            self.Ser1_scale.configure(length="116")
            self.Ser1_scale.configure(orient="horizontal")
            self.Ser1_scale.configure(troughcolor="#d9d9d9")

            self.Ser2_scale = tk.Scale(self.ServoOffset_frame, from_=-15.0, to=15.0)
            self.Ser2_scale.place(relx=0.188, rely=0.387, relwidth=0.763, relheight=0.0, height=42, bordermode='ignore')
            self.Ser2_scale.configure(background="#d9d9d9")
            self.Ser2_scale.configure(highlightbackground="#d9d9d9")
            self.Ser2_scale.configure(highlightcolor="black")
            self.Ser2_scale.configure(length="116")
            self.Ser2_scale.configure(orient="horizontal")
            self.Ser2_scale.configure(troughcolor="#d9d9d9")

            self.Ser3_scale = tk.Scale(self.ServoOffset_frame, from_=-15.0, to=15.0)
            self.Ser3_scale.place(relx=0.188, rely=0.645, relwidth=0.763, relheight=0.0, height=42, bordermode='ignore')
            self.Ser3_scale.configure(background="#d9d9d9")
            self.Ser3_scale.configure(highlightbackground="#d9d9d9")
            self.Ser3_scale.configure(highlightcolor="black")
            self.Ser3_scale.configure(length="116")
            self.Ser3_scale.configure(orient="horizontal")
            self.Ser3_scale.configure(troughcolor="#d9d9d9")

            self.Connection_frame = tk.LabelFrame(top_layer)
            self.Connection_frame.place(relx=0.791, rely=0.379, relheight=0.102, relwidth=0.192)
            self.Connection_frame.configure(text='Connection Status')
            self.Connection_frame.configure(background="#d9d9d9")
            self.Connection_frame.configure(width=160)

            self.Connection_label = tk.Label(self.Connection_frame)
            self.Connection_label.place(relx=0.063, rely=0.267, height=45, width=140, bordermode='ignore')
            self.Connection_label.configure(background="#a0a0a0")
            self.Connection_label.configure(disabledforeground="#a3a3a3")
            self.Connection_label.configure(font="-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
            self.Connection_label.configure(foreground="#000000")
            self.Connection_label.configure(relief="ridge")
            self.Connection_label.configure(text=MRB_Constants.CONNECTING)
            self.Connection_label.configure(width=134)

            self.Status_frame = tk.LabelFrame(top_layer)
            self.Status_frame.place(relx=0.791, rely=0.244, relheight=0.129, relwidth=0.192)
            self.Status_frame.configure(text='Program state')
            self.Status_frame.configure(background="#d9d9d9")
            self.Status_frame.configure(width=160)
            
            self.Idle_radiobutton = tk.Radiobutton(self.Status_frame, text=MRB_Constants.STATE_IDLE, variable=self.program_state, value="Idle")
            self.Idle_radiobutton.place(relx=0.063, rely=0.211, relheight=0.263, relwidth=0.3, bordermode='ignore')
            self.Idle_radiobutton.configure(activebackground="#d9d9d9")
            self.Idle_radiobutton.configure(anchor='w')
            self.Idle_radiobutton.configure(background="#d9d9d9")
            self.Idle_radiobutton.configure(justify='left')
            
            self.Calibration_radiobutton = tk.Radiobutton(self.Status_frame, text=MRB_Constants.STATE_CALIBRATION, variable=self.program_state, value="Calibration")
            self.Calibration_radiobutton.place(relx=0.063, rely=0.421, relheight=0.263, relwidth=0.538, bordermode='ignore')
            self.Calibration_radiobutton.configure(activebackground="#d9d9d9")
            self.Calibration_radiobutton.configure(anchor='w')
            self.Calibration_radiobutton.configure(background="#d9d9d9")
            self.Calibration_radiobutton.configure(justify='left')
            
            self.Active_radiobutton = tk.Radiobutton(self.Status_frame, text=MRB_Constants.STATE_ACTIVE, variable=self.program_state, value="Active")
            self.Active_radiobutton.place(relx=0.063, rely=0.632, relheight=0.263, relwidth=0.425, bordermode='ignore')
            self.Active_radiobutton.configure(activebackground="#d9d9d9")
            self.Active_radiobutton.configure(anchor='w')
            self.Active_radiobutton.configure(background="#d9d9d9")
            self.Active_radiobutton.configure(justify='left')

            self.Webcam = tk.Canvas(top_layer, width=640, height=480, background="#c9c9c9", highlightthickness=1, highlightbackground="black")
            self.Webcam.grid(row=0, column=0)

            self.Webcam_mask = tk.Canvas(top_layer, width=320, height=240, background="#c9c9c9", highlightthickness=1, highlightbackground="black")
            self.Webcam_mask.grid(row=1, column=0)

            self.set_select_state(self.Ball_color_calibration_button)

        def set_select_state(self, button):
            self.Ball_color_calibration_button.configure(state='normal')
            self.Ball_destination_button.configure(state='normal')
            self.Servo_calibration_button.configure(state='normal')
            button.configure(state='disabled')

            self.selection_mode.set(button['text'])
