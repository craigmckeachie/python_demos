html_colors = {
    "AliceBlue": "#FOF8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "00FFFF"
}

print(html_colors["AliceBlue"])
# print(html_colors["AAA"]) # KeyError
print(html_colors.get("AAA"))
print(html_colors.get("AliceBlue"))
print(html_colors.get("AAA", "#000000"))
print(html_colors)
