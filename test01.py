import calendar
import tkinter as tk
c = calendar.TextCalendar()
m = c.formatmonth(2023, 5)
root = tk.Tk()
t = tk.Text(root, height = 6, width=20 )
t.insert(tk.END, m)
t.pack()
tk.mainloop()