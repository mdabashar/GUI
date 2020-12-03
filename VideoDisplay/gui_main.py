from PIL import Image, ImageTk
from tkinter.ttk import Frame, Label, Button, Style
import tkinter as tk
import cv2

class VideoWindow():
    
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20 # Interval in ms to get the latest frame
        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)
        # Update image on canvas
        self.update_image()
        
    def update_image(self):
        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)


    

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.counter = 0
        self.initUI()


    def initUI(self):

        self.master.title("Attendence System")
        self.pack(fill=tk.BOTH, expand=1)

        Style().configure("TFrame", background="#333")
        
        # image panel background
        img = Image.open('button_background.jpg').resize((1200, 150))
        photo_img = ImageTk.PhotoImage(img)
        label = Label(self, image=photo_img)
        label.image = photo_img
        label.place(x=150, y=500)
        
        img_names = ['b_grad.jpg', 'b_lib.jpg', 'b_style.jpg', 
                     'b_grad.jpg', 'b_lib.jpg', 'b_style.jpg', 
                     'b_grad.jpg', 'b_lib.jpg', 'b_style.jpg']
        for i, img_name in enumerate(img_names):
            img = Image.open(img_name).resize((100, 100))
            photo_img = ImageTk.PhotoImage(img)
            label = Label(self, image=photo_img)
            label.image = photo_img
            label.place(x=150+110*(i+1), y=520)
            
        
        # button background
        img = Image.open('button_background.jpg').resize((150, 645))
        photo_img = ImageTk.PhotoImage(img)
        label = Label(self, image=photo_img)
        label.image = photo_img
        label.place(x=5, y=5)
            
        rep_today = Button(self, text="Report Today", style='TButton', 
                           width=20, command=self.create_window)
        rep_today.place(x=18, y=20)
        
        rep_daily = Button(self, text="Daily Report", width=20)
        rep_daily.place(x=18, y=70)
        
        rep_individual = Button(self, text="Individual Report", width=20)
        rep_individual.place(x=18, y=120)
        
        rep_summary = Button(self, text="Summary", width=20)
        rep_summary.place(x=18, y=170)
        
        rep_advance = Button(self, text="Advance", width=20)
        rep_advance.place(x=18, y=220)
        
        vw = VideoWindow(self, cv2.VideoCapture(0))
        vw.canvas.place(x=180, y=5)
        
        # other background
        img = Image.open('button_background.jpg').resize((430, 480))
        photo_img = ImageTk.PhotoImage(img)
        label = Label(self, image=photo_img)
        label.image = photo_img
        label.place(x=830, y=5)
        
    def create_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)


def main():

    root = tk.Tk()
    root.geometry("1400x650")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()