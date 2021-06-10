html_colors = {
    "AliceBlue": "#FOF8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "00FFFF"
}

html_colors_keys = html_colors.keys()
html_colors_values = html_colors.values()
html_colors_items = html_colors.items()

print(html_colors_keys)
print(html_colors_values)
print(html_colors_items)

del html_colors["Aqua"]

print(html_colors_keys)
print(html_colors_values)
print(html_colors_items)

html_colors["Red"] = "#FF0000"

print(html_colors_keys)
print(html_colors_values)
print(html_colors_items)
