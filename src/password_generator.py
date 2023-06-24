########################################################
#---------------- github.com/duruburak ----------------#
########################################################

import secrets
import string
import tkinter as tk

import customtkinter
import pyperclip



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.chosen_password_length: int = 12
        self.chosen_symbols_choice: bool = True
        self.chosen_uppercase_choice: bool = True

        self.minsize(600, 500)
        self.geometry("600x500")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.title("Password Generator")

        self.password_frame = customtkinter.CTkFrame(self, corner_radius=15)
        self.password_frame.pack(pady=25, anchor=tk.CENTER)

        self.label_password_length = customtkinter.CTkLabel(self.password_frame, font=(
            "Rajdhani Medium", 17, "bold"), text="Password Length: ")
        self.label_password_length.pack(padx=10, side="left")

        self.var_password_length = customtkinter.IntVar(value=12)
        self.password_length = customtkinter.CTkSlider(self.password_frame, from_=6, to=30, number_of_steps=24, variable=self.var_password_length,
                                                       progress_color="#19A7CE", button_color="#FB2576", button_hover_color="#D800A6", fg_color="#0B2447",
                                                       command=self.set_live_password_length)
        self.password_length.pack(padx=10, side="left")

        self.live_status_password_length = customtkinter.CTkLabel(self.password_frame, width=30, font=(
            "Roboto Mono Regular", 17, "normal"), text=self.var_password_length.get())
        self.live_status_password_length.pack(padx=10, side="left")

        self.var_symbols_choice = customtkinter.StringVar(value="Symbols Included")
        self.symbols_choice = customtkinter.CTkSwitch(self, text="Symbols Included", command=self.symbols_switch_event,
                                                      variable=self.var_symbols_choice, onvalue="Symbols Included", offvalue="No Symbols",
                                                      fg_color="#BE9FE1", progress_color="#E84545", button_color="#FF78C4",
                                                      button_hover_color="#850E35", font=("Bahnschrift", 17, "normal"))
        self.symbols_choice.pack(pady=25, anchor=tk.CENTER)

        self.var_uppercase_choice = customtkinter.StringVar(
            value="Uppercase Included")
        self.uppercase_choice = customtkinter.CTkSwitch(self, text="Uppercase Included", command=self.uppercase_switch_event,
                                                        variable=self.var_uppercase_choice, onvalue="Uppercase Included", offvalue="No Uppercase",
                                                        fg_color="#BE9FE1", progress_color="#E84545", button_color="#CD104D",
                                                        button_hover_color="#850E35", font=("Bahnschrift", 17, "normal"))
        self.uppercase_choice.pack(pady=25, anchor=tk.CENTER)

        self.generate_btn = customtkinter.CTkButton(self, text="Generate", text_color="#F7C8E0", command=lambda: self.generate_password(
            self.chosen_password_length, self.chosen_symbols_choice, self.chosen_uppercase_choice),
            font=("Bauhaus 93", 18, "normal"))
        self.generate_btn.pack(pady=15, anchor=tk.CENTER)

        self.var_password = customtkinter.StringVar(value="")
        self.password_generation = customtkinter.CTkEntry(self, width=400, font=(
            "Bahnschrift", 20, "normal"), textvariable=self.var_password)
        self.password_generation.pack(pady=15, anchor=tk.CENTER)

        self.copy_password = customtkinter.CTkButton(self, width=50, fg_color="#EA906C", font=(
            "Harrington", 17, "bold"), text="COPY", command=self.copy_to_clipboard)
        self.copy_password.pack(pady=8, anchor=tk.CENTER)


    def contains_upper(self, password: str) -> bool:
        """Checks whether a password contains uppercase characters"""

        for char in password:
            if char.isupper():
                return True

        return False  # There were no uppercase chars


    def contains_symbols(self, password: str) -> bool:
        """Checks whether a password contains symbols"""

        for char in password:
            if char in string.punctuation:
                return True

        return False  # There were no uppercase chars


    def generate_password(self, length: int, symbols: bool, uppercase: bool):
        """
        Generates a password based on the users specifications

        :param length: The length of the password
        :param symbols: Password should include symbols
        :param uppercase: Password should include uppercase letters
        :return: str
        """

        # Create a combination of characters to choose from
        combination: str = string.ascii_lowercase + string.digits

        # If the user wants symbols, add punctuation to the combination
        if symbols:
            combination += string.punctuation

        # If the user wants uppercase, add uppercase to the combination
        if uppercase:
            combination += string.ascii_uppercase

        # Get the length of the combination characters
        combination_length: int = len(combination)

        # Create a new password variable
        password: str = ''

        # Append to the password a new random character for each iteration
        for _ in range(length):
            password += combination[secrets.randbelow(combination_length)]

        self.password_generation.delete(0, "end")
        self.password_generation.insert(0, password)


    def symbols_switch_event(self):

        if self.var_symbols_choice.get() == "Symbols Included":
            self.chosen_symbols_choice = True

        else:
            self.chosen_symbols_choice = False

        self.symbols_choice.configure(text=self.var_symbols_choice.get())
        self.update_idletasks()


    def uppercase_switch_event(self):

        if self.var_uppercase_choice.get() == "Uppercase Included":
            self.chosen_uppercase_choice = True

        else:
            self.chosen_uppercase_choice = False

        self.uppercase_choice.configure(text=self.var_uppercase_choice.get())
        self.update_idletasks()


    def set_live_password_length(self, value):

        self.chosen_password_length = int(value)

        self.live_status_password_length.configure(text=int(value))
        self.update_idletasks()


    def copy_to_clipboard(self):
        pyperclip.copy(self.var_password.get())


def main():
    app = App()
    app.mainloop()



if __name__ == '__main__':
    main()
