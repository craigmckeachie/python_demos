html_colors = {
    "AliceBlue": "#FOF8FF",
    "AntiqueWhite": "#FAEBD7"

}

# html_colors["Aqua"] = "#00FFFF"
# "Aqua": "00FFFF"

print(html_colors.setdefault("Aqua", "#00FFFF"))  # adds to list if not there
print("Aqua" in html_colors)

print(html_colors)

# del html_colors["Aqua"]
# print(html_colors)
# print("Aqua" not in html_colors)

# print(html_colors.pop("Aqua"))
# # doesn't add the thing to list just gives default
# print(html_colors.pop("Red", "#ff0000"))
# print(html_colors)
# print(html_colors.popitem())
# print(html_colors)

# pop remove item based on key, pop item removes last item

print(len(html_colors))
html_colors.clear()

print(len(html_colors))
print(html_colors)



