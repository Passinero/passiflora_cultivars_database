# -*- coding: utf-8 -*-

import pandas
import tkinter as tk
import sys
import io

FONT = ("open sans", 14)
ENTRY_FONT = ("calibri", 12)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dataframe = pandas.read_csv("Passiflora_Cultivars_0924.csv")
print(len(dataframe))


def listbox_insert(row):

    list_box.insert(tk.END, f"'{row['Cultivar Name'].title()}'     "
                            f"{row['Female Parent'].title()}   x   "
                            f"{row['Male Parent'].title()}      "
                            f"{row['Breeder'].title()}      "
                            f"{row['Year']}")


def reset():
    name_entry.delete(0, tk.END)
    male_entry.delete(0, tk.END)
    female_entry.delete(0, tk.END)
    breeder_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

    list_box.delete(1, tk.END)


def search():
    name = name_entry.get()
    female = female_entry.get()
    male = male_entry.get()
    breeder = breeder_entry.get()
    year = year_entry.get()

    cat_list = [cat for cat in [name, female, male, breeder, year] if cat]

    value_dict = {name: "Cultivar Name",
                  female: "Female Parent",
                  male: "Male Parent",
                  breeder: "Breeder",
                  year: "Year"
                  }

    if len(cat_list) == 1:
        category = value_dict[cat_list[0]]
        new_df = dataframe[dataframe[category] == cat_list[0]]

        if new_df.empty:
            return

        list_box.insert(tk.END, "")

        for index, row in new_df.iterrows():
            listbox_insert(row)

    elif len(cat_list) == 2:
        cat_1 = value_dict[cat_list[0]]
        cat_2 = value_dict[cat_list[1]]

        double_df = dataframe[(dataframe[cat_1] == cat_list[0]) &
                              (dataframe[cat_2] == cat_list[1])]
        if double_df.empty:
            return

        list_box.insert(tk.END, "")

        for index, row in double_df.iterrows():
            listbox_insert(row)

    elif len(cat_list) == 3:
        cat_1 = value_dict[cat_list[0]]
        cat_2 = value_dict[cat_list[1]]
        cat_3 = value_dict[cat_list[2]]

        triple_df = dataframe[(dataframe[cat_1] == cat_list[0]) &
                              (dataframe[cat_2] == cat_list[1]) &
                              (dataframe[cat_3] == cat_list[2])]

        if triple_df.empty:
            return

        list_box.insert(tk.END, "")

        for index, row in triple_df.iterrows():
            listbox_insert(row)


main_window = tk.Tk()
main_window.minsize(600, 800)
main_window.config(bg="white")
main_window.title("Passiflora Datenbank 09/2024")

name_str = tk.StringVar()

# Labels

name_label = tk.Label(text="Cultivar Name", bg="white", font=FONT)
name_label.grid(row=2, column=0, padx=5, pady=5)

female_label = tk.Label(text="Female Parent", bg="white", font=FONT)
female_label.grid(row=2, column=1, padx=5, pady=5)

male_label = tk.Label(text="Male Parent", bg="white", font=FONT)
male_label.grid(row=2, column=2, padx=5, pady=5)

breeder_label = tk.Label(text="Breeder", bg="white", font=FONT)
breeder_label.grid(row=2, column=3, padx=5, pady=5)

year_label = tk.Label(text="Year", bg="white", font=FONT)
year_label.grid(row=2, column=4, padx=5, pady=5)

# Entries

name_entry = tk.Entry(font=ENTRY_FONT)
name_entry.grid(row=3, column=0, padx=5, pady=20)

female_entry = tk.Entry(font=ENTRY_FONT)
female_entry.grid(row=3, column=1, padx=5, pady=20)

male_entry = tk.Entry(font=ENTRY_FONT)
male_entry.grid(row=3, column=2, padx=5, pady=20)

breeder_entry = tk.Entry(font=ENTRY_FONT)
breeder_entry.grid(row=3, column=3, padx=5, pady=20)

year_entry = tk.Entry(font=ENTRY_FONT)
year_entry.grid(row=3, column=4, padx=5, pady=20)

# Buttons

search_button = tk.Button(text="Search", command=search, font=FONT, bg="#BACD92")
search_button.grid(row=4, column=1)

reset_button = tk.Button(text="Reset", command=reset, font=FONT, bg="#E1ACAC")
reset_button.grid(row=4, column=3)

list_box = tk.Listbox(main_window, width=100, height=30, font=("calibri", 12))
list_box.grid(row=5, column=0, pady=20, padx=20, columnspan=5)
list_box.insert(tk.END, "                                 Cultivar Name         Female Parent            "
                        "Male Parent            Breeder            Year\n")

main_window.mainloop()
