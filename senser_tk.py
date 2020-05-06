from tkinter import *
from tkinter import ttk
from sense_hat import SenseHat
import threading

sense = SenseHat()

root = Tk()
frame1 = ttk.Frame(root)
frame1.grid()

label1 = ttk.Label(frame1, text='pitch', width=10)
label1.grid(row=1, column=1)

label_pitch = ttk.Label(frame1, width=10)
label_pitch.grid(row=1, column=2)

label2 = ttk.Label(frame1, text='yaw', width=10)
label2.grid(row=1, column=3)

label_yaw = ttk.Label(frame1, width=10)
label_yaw.grid(row=1, column=4)

label3 = ttk.Label(frame1, text='roll', width=10)
label3.grid(row=1, column=5)

label_roll = ttk.Label(frame1, width=10)
label_roll.grid(row=1, column=6)

label4 = ttk.Label(frame1, text='acceler[x]', width=10)
label4.grid(row=2, column=1)

label_acceler_x = ttk.Label(frame1, width=10)
label_acceler_x.grid(row=2, column=2)

label5 = ttk.Label(frame1, text='acceler[y]', width=10)
label5.grid(row=2, column=3)

label_acceler_y = ttk.Label(frame1, width=10)
label_acceler_y.grid(row=2, column=4)

label6 = ttk.Label(frame1, text='acceler[z]', width=10)
label6.grid(row=2, column=5)

label_acceler_z = ttk.Label(frame1, width=10)
label_acceler_z.grid(row=2, column=6)

label7 = ttk.Label(frame1, text='temperature', width=10)
label7.grid(row=3, column=1)

label_temperature = ttk.Label(frame1, width=10)
label_temperature.grid(row=3, column=2)

label8 = ttk.Label(frame1, text='pressure', width=10)
label8.grid(row=3, column=3)

label_pressure = ttk.Label(frame1, width=10)
label_pressure.grid(row=3, column=4)

label9 = ttk.Label(frame1, text='humidty', width=10)
label9.grid(row=3, column=5)

label_humidty = ttk.Label(frame1, width=10)
label_humidty.grid(row=3, column=6)

def scheduler():
    t = threading.Timer(0.05, scheduler)
    t.start()
    orientation_data = sense.get_orientation()
    label_pitch.configure(text=f'{orientation_data["pitch"]:.4f}')
    label_yaw.configure(text=f'{orientation_data["yaw"]:.4f}')
    label_roll.configure(text=f'{orientation_data["roll"]:.4f}')

    accelerometer_data = sense.get_accelerometer_raw()
    label_acceler_x.configure(text=f'{accelerometer_data["x"]:.4f}')
    label_acceler_y.configure(text=f'{accelerometer_data["y"]:.4f}')
    label_acceler_z.configure(text=f'{accelerometer_data["z"]:.4f}')

    label_temperature.configure(text=f'{sense.get_temperature():.4f}')
    label_pressure.configure(text=f'{sense.get_pressure():.4f}')
    label_humidty.configure(text=f'{sense.get_humidity():.4f}')

t = threading.Thread(target = scheduler)
t.start()

root.mainloop()
