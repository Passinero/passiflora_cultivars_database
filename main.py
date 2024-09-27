# -*- coding: utf-8 -*-

import pandas
import tkinter as tk
import sys
import io


FONT = ("open sans", 14)
ENTRY_FONT = ("calibri", 12)
HEADER_FONT = ("open sans", 18)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dataframe = pandas.read_csv("Passiflora_Cultivars_0924.csv")

breeder_str_list = [str(string) for string in dataframe["Breeder"]]
name_str_list = [str(string) for string in dataframe["Cultivar Name"]]
female_str_list = [str(string) for string in dataframe["Female Parent"]]
male_str_list = [str(string) for string in dataframe["Male Parent"]]



def listbox_insert(row):

    list_box.insert(tk.END, f"'{row['Cultivar Name'].title()}'     "
                            f"{row['Female Parent'].title()}   ×   "
                            f"{row['Male Parent'].title()}      "
                            f"{row['Breeder'].title()}      "
                            f"{row['Year']}")


def reset():
    name_entry.delete(0, tk.END)
    female_entry.delete(0, tk.END)
    male_entry.delete(0, tk.END)
    breeder_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

    list_box.delete(1, tk.END)


def search():
    name = name_entry.get().lower()
    female = female_entry.get().lower()
    male = male_entry.get().lower()
    breeder = breeder_entry.get().lower()
    year = year_entry.get()

    if year:
        if len(year) == 4:
            for el in year:
                if not el.isnumeric():
                    list_box.insert(tk.END, "")
                    list_box.insert(tk.END, "Invalid year")
                    return
        else:
            list_box.insert(tk.END, "")
            list_box.insert(tk.END, "Invalid year")
            return

    cat_list = [cat for cat in [name, female, male, breeder, year] if cat]

    value_dict = {name: "Cultivar Name",
                  female: "Female Parent",
                  male: "Male Parent",
                  breeder: "Breeder",
                  year: "Year"
                  }

    if len(cat_list) == 1:

        if breeder:
            for breed in breeder_str_list:
                if cat_list[0] in breed:
                    found = True
                    new_df = dataframe[dataframe["Breeder"] == breed]

                    if new_df.empty:
                        list_box.insert(tk.END, "No data found")
                        return
                    else:
                        list_box.insert(tk.END, "")
                        for index, row in new_df.iterrows():
                            listbox_insert(row)

                        if found:
                            return
        else:
            category = value_dict[cat_list[0]]
            new_df = dataframe[dataframe[category] == cat_list[0]]
            if new_df.empty:
                list_box.insert(tk.END, "")
                list_box.insert(tk.END, "No data found")
                return
            else:
                for index, row in new_df.iterrows():
                    listbox_insert(row)

        list_box.insert(tk.END, "")

    elif len(cat_list) == 2:
        cat_1 = value_dict[cat_list[0]]
        cat_2 = value_dict[cat_list[1]]

        double_df = dataframe[(dataframe[cat_1] == cat_list[0]) &
                              (dataframe[cat_2] == cat_list[1])]
        if double_df.empty:
            list_box.insert(tk.END, "")
            list_box.insert(tk.END, "No data found")
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
            list_box.insert(tk.END, "")
            list_box.insert(tk.END, "No data found")
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

header_label = tk.Label(text=f"Passiflora Cultivars Database", font=HEADER_FONT, bg="white")
header_label.grid(row=0, column=1, columnspan=3, pady=25)

how_many_label = tk.Label(text=f"{len(dataframe)} Entries", font=("open sans", 13), bg="white")
how_many_label.grid(row=0, column=4)

date_label = tk.Label(text="09/2024", font=("open sans", 13), bg="white")
date_label.grid(row=0, column=0)

name_label = tk.Label(text="Cultivar Name", bg="white", font=FONT)
name_label.grid(row=2, column=0, padx=5)

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
name_entry.grid(row=3, column=0, padx=10, pady=15)

female_entry = tk.Entry(font=ENTRY_FONT)
female_entry.grid(row=3, column=1, padx=5, pady=15)

male_entry = tk.Entry(font=ENTRY_FONT)
male_entry.grid(row=3, column=2, padx=5, pady=15)

breeder_entry = tk.Entry(font=ENTRY_FONT)
breeder_entry.grid(row=3, column=3, padx=5, pady=15)

year_entry = tk.Entry(font=ENTRY_FONT)
year_entry.grid(row=3, column=4, padx=10, pady=15)

# Buttons

search_button = tk.Button(text="Search", command=search, font=FONT, bg="#BACD92")
search_button.grid(row=4, column=1, pady=8)

reset_button = tk.Button(text="Reset", command=reset, font=FONT, bg="#E1ACAC")
reset_button.grid(row=4, column=3, pady=8)

list_box = tk.Listbox(main_window, width=92, height=30, font=("open sans", 13), bg="#FFFBE6")
list_box.grid(row=5, column=0, pady=20, padx=20, columnspan=5)
list_box.insert(tk.END, "Cultivar Name         Female Parent          "
                        "Male Parent          Breeder         Year\n")

main_window.mainloop()
