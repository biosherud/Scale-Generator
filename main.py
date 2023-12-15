import tkinter as tk
from tkinter import scrolledtext
from keys import Scale  # Assuming Scale class is defined in keys.py
import examples
import songs
import re
class ScaleApp:
    def __init__(self, root):
        self.root = root
        root.title("Scale Generator App")
        root.configure(bg='#a888d1')  # Dark background color
        self.selected_key = None  # Variable to store the selected key
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the text area with a different background
        text_and_songs_frame = tk.Frame(self.root, bg='#1e1e1e')
        text_and_songs_frame.grid(row=0, column=0, padx=(20, 20), pady=(25, 10), sticky="nsew")

        # Set up text area
        self.setup_text_area(text_and_songs_frame)

        # Set up songs text area
        self.setup_songs_text_area(text_and_songs_frame)

        # Set up text area for displaying scale information


        # Create a frame for the fretboard with a different background
        fretboard_frame = tk.Frame(self.root, bg='#d4aa00')
        fretboard_frame.grid(row=1, column=0, padx=(20, 20), pady=(10, 25), sticky="nsew")

        # Set up fretboard display
        self.setup_fretboard_display(fretboard_frame)

        # Create a frame for the buttons with a different background
        buttons_frame = tk.Frame(self.root, bg='#d4aa00')
        buttons_frame.grid(row=2, column=0, pady=(0, 20), padx=(20, 20), sticky="nsew")

        # Create buttons for selecting the key
        key_frame = tk.Frame(buttons_frame, bg='#d4aa00')
        key_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.create_key_buttons(key_frame)

        # Create buttons for selecting the scale
        scale_frame = tk.Frame(buttons_frame, bg='#d4aa00')
        scale_frame.grid(row=0, column=1, pady=10, sticky='ew')
        self.create_scale_buttons(scale_frame)

        songs_text_frame = tk.Frame(self.root, bg='#d4aa00')
        songs_text_frame.grid(row=0, column=1, padx=(10, 20), pady=(25, 10), sticky="nsew")




        # Configure row and column weights for proper resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def setup_text_area(self, frame):
        # Set up scrolled text area
        self.text_area = scrolledtext.ScrolledText(frame, width=50, height=15, font=('Courier New', 15), bg='white', fg='black')  # Change fg to black
        self.text_area.pack(side=tk.LEFT, expand=True, fill='both')


    def create_key_buttons(self, frame):
        # Create buttons for each key to generate scales
        keys = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

        for i, key in enumerate(keys):
            button_text = f'Generate {key} Scales'
            button = tk.Button(frame, text=button_text, command=lambda k=key: self.set_selected_key(k),
                               highlightthickness=0, font=('Comic Sans MS', 12), bg='#d4aa00', fg='#1e1e1e')
            button.grid(row=i // 3, column=i % 3, padx=30, pady=10, sticky='ew')

    def create_scale_buttons(self, frame):
        # Create buttons for each scale to display on the fretboard
        scales = ["Major", "Minor", "Ousak", "Xitzaz", "Armoniko", "Sampax", "Xitzaskiar",
                  "Niavent", "Kartsigiar", "Peiraiotikos", "Poimenikos", "Segiax",
                  "Tampaxaniotikos", "Xouzam", "Xouseini", "Rast", "Kiournti",
                  "Lokrikos", "Ludikos", "Mixoludikos", "Ouzal", "Souzinak"]

        for i, scale_name in enumerate(scales):
            button = tk.Button(frame, text=scale_name, command=lambda s=scale_name: self.display_scale(s),
                               bg='#1e1e1e', fg='#61dafb')
            button.grid(row=i // 5, column=i % 5, pady=5, padx=10)

    def setup_songs_text_area(self, frame):
        # Set up scrolled text area for displaying songs
        self.songs_text_area = scrolledtext.ScrolledText(frame, width=50, height=15, font=('Courier New', 15),
                                                         bg='black', fg='white')
        self.songs_text_area.pack(side=tk.LEFT, expand=True, fill='both')
    def setup_fretboard_display(self, frame):
        # Set up fretboard display
        self.fretboard_label = tk.Label(frame, text=examples.fretboard, font=('Courier New', 20), bg='black', fg='white', justify='left', anchor='w')
        self.fretboard_label.pack(expand=True, fill='both')

    def set_selected_key(self, key):
        # Function to set the selected key when "Generate A Scales" button is pressed
        self.selected_key = key
        self.display_scales(self.selected_key)

    def display_scales(self, key):
        if self.selected_key:
            scale_instance = Scale(self.selected_key)

            major_scale, major_chords = scale_instance.major()
            minor_scale, minor_chords = scale_instance.minor()
            ousak_scale, ousak_chords = scale_instance.ousak()
            xitzaz_scale, xitzaz_chords = scale_instance.xitzaz()
            armoniko_scale, armoniko_chords = scale_instance.armoniko()
            sampax_scale, sampax_chords = scale_instance.sampax()
            xitzaskiar_scale, xitzaskiar_chords = scale_instance.xitzaskiar()
            niavent_scale, niavent_chords = scale_instance.niavent()
            kartsigiar_scale, kartsigiar_chords = scale_instance.kartsigiar()
            peiraiotikos_scale, peiraiotikos_chords = scale_instance.peiraiotikos()
            poimenikos_scale, poimenikos_chords = scale_instance.poimenikos()
            segiax_scale, segiax_chords = scale_instance.segiax()
            tampaxaniotikos_scale, tampaxaniotikos_chords = scale_instance.tampaxaniotikos()
            xouzam_scale, xouzam_chords = scale_instance.xouzam()
            xouseini_scale, xouseini_chords = scale_instance.xouseini()
            rast_scale, rast_chords = scale_instance.rast()
            kiournti_scale, kiournti_chords = scale_instance.kiournti()
            lokrikos_scale, lokrikos_chords = scale_instance.lokrikos()
            ludikos_scale, ludikos_chords = scale_instance.ludikos()
            mixoludikos_scale, mixoludikos_chords = scale_instance.mixoludikos()
            ouzal_scale, ouzal_chords = scale_instance.ouzal()
            souzinak_scale, souzinak_chords = scale_instance.souzinak()

            result_text = f'{key} Major Scale: {" ".join(major_scale)}\n'
            result_text += f'Major Chords: {major_chords}\n\n'
            result_text += f'{key} Minor Scale: {" ".join(minor_scale)}\n'
            result_text += f'Minor Chords: {minor_chords}\n\n'
            result_text += f'{key} Ousak Scale: {" ".join(ousak_scale)}\n'
            result_text += f'Ousak Chords: {ousak_chords}\n\n'
            result_text += f'{key} Xitzaz Scale: {" ".join(xitzaz_scale)}\n'
            result_text += f'Xitzaz Chords: {xitzaz_chords}\n\n'
            result_text += f'{key} Armoniko Scale: {" ".join(armoniko_scale)}\n'
            result_text += f'Armoniko Chords: {armoniko_chords}\n\n'
            result_text += f'{key} Sampax Scale: {" ".join(sampax_scale)}\n'
            result_text += f'Sampax Chords: {sampax_chords}\n\n'
            result_text += f'{key} Xitzaskiar Scale: {" ".join(xitzaskiar_scale)}\n'
            result_text += f'Xitzaskiar Chords: {xitzaskiar_chords}\n\n'
            result_text += f'{key} Niavent Scale: {" ".join(niavent_scale)}\n'
            result_text += f'Niavent Chords: {niavent_chords}\n\n'
            result_text += f'{key} Kartsigiar Scale: {" ".join(kartsigiar_scale)}\n'
            result_text += f'Kartsigiar Chords: {kartsigiar_chords}\n\n'
            result_text += f'{key} Peiraiotikos Scale: {" ".join(peiraiotikos_scale)}\n'
            result_text += f'Peiraiotikos Chords: {peiraiotikos_chords}\n\n'
            result_text += f'{key} Poimenikos Scale: {" ".join(poimenikos_scale)}\n'
            result_text += f'Poimenikos Chords: {poimenikos_chords}\n\n'
            result_text += f'{key} Segiax Scale: {" ".join(segiax_scale)}\n'
            result_text += f'Segiax Chords: {segiax_chords}\n\n'
            result_text += f'{key} Tampaxaniotikos Scale: {" ".join(tampaxaniotikos_scale)}\n'
            result_text += f'Tampaxaniotikos Chords: {tampaxaniotikos_chords}\n\n'
            result_text += f'{key} Xouzam Scale: {" ".join(xouzam_scale)}\n'
            result_text += f'Xouzam Chords: {xouzam_chords}\n\n'
            result_text += f'{key} Xouseini Scale: {" ".join(xouseini_scale)}\n'
            result_text += f'Xouseini Chords: {xouseini_chords}\n\n'
            result_text += f'{key} Rast Scale: {" ".join(rast_scale)}\n'
            result_text += f'Rast Chords: {rast_chords}\n\n'
            result_text += f'{key} Kiournti Scale: {" ".join(kiournti_scale)}\n'
            result_text += f'Kiournti Chords: {kiournti_chords}\n\n'
            result_text += f'{key} Lokrikos Scale: {" ".join(lokrikos_scale)}\n'
            result_text += f'Lokrikos Chords: {lokrikos_chords}\n\n'
            result_text += f'{key} Ludikos Scale: {" ".join(ludikos_scale)}\n'
            result_text += f'Ludikos Chords: {ludikos_chords}\n\n'
            result_text += f'{key} Mixoludikos Scale: {" ".join(mixoludikos_scale)}\n'
            result_text += f'Mixoludikos Chords: {mixoludikos_chords}\n\n'
            result_text += f'{key} Ouzal Scale: {" ".join(ouzal_scale)}\n'
            result_text += f'Ouzal Chords: {ouzal_chords}\n\n'
            result_text += f'{key} Souzinak Scale: {" ".join(souzinak_scale)}\n'
            result_text += f'Souzinak Chords: {souzinak_chords}\n'

            self.text_area.delete(1.0, tk.END)  # Clear previous text
            self.text_area.insert(tk.END, result_text)

            self.text_area.tag_add('center', '1.0', 'end')
            self.text_area.tag_configure('center', justify='center')

    def display_scale(self, scale_name):
        if self.selected_key:
            lowercase_scale_name = scale_name.lower()

            # Assuming you have an instance of the Scale class called scale_instance
            scale_instance = Scale(self.selected_key)

            # Use getattr to dynamically call the method
            scale_tuple = getattr(scale_instance, lowercase_scale_name)()

            # The scale_tuple would contain the scale name, scale, and chords
            scale, chords = scale_tuple

            tragoudeta = songs.tragoudia.get(lowercase_scale_name, [])
            songs_text = f"Songs for {scale_name} scale:\n\n" + '\n'.join(tragoudeta)
            self.songs_text_area.delete(1.0, tk.END)  # Clear previous text
            self.songs_text_area.insert(tk.END, songs_text)
            self.songs_text_area.tag_add('center', '1.0', 'end')
            self.songs_text_area.tag_configure('center', justify='center')

            # Display information on top of the fretboard
            info_text = '------------------------------------------------------\n'
            info_text += f"Selected Key: {self.selected_key}\n"
            info_text += f"Scale Name: {scale_name}\n"
            info_text += f"Scale: {scale}\n"
            info_text += f"Chords: {chords}\n"
            info_text += '------------------------------------------------------\n'

            # Update the information on top of the fretboard with centered text
            self.fretboard_label.config(text=info_text, justify='center', anchor='center', fg='white')

            all_notes = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']
            rest_of_notes = []

            for note in all_notes:
                if note not in scale:
                    rest_of_notes.append(note)

            print(rest_of_notes)

            modified_fretboard = examples.fretboard

            for note in rest_of_notes:
                if len(note) == 1:
                    modified_fretboard = re.sub(fr'(?:(?<=\s)|(?<=^)){re.escape(note)}(?:(?=\s)|(?=\n)|(?=$))', '-',
                                                modified_fretboard)
                else:
                    modified_fretboard = re.sub(fr'(?:(?<=\s)|(?<=^)){re.escape(note)}(?:(?=\s)|(?=\n)|(?=$))', '- ',
                                                modified_fretboard)

            print(modified_fretboard)

            self.fretboard_label.config(text=info_text + "\n" + modified_fretboard)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScaleApp(root)
    root.mainloop()
