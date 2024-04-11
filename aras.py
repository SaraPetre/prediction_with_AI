from pyfiglet import Figlet
import matplotlib.pyplot as plt

# Skapa instans av Figlet och rendera texten
f_f = Figlet(font='slant')
rendered_text = f_f.renderText('Its all about AI and crypto now')

# Skapa en bild av utskriften
plt.text(0.5, 0.5, rendered_text, horizontalalignment='center', verticalalignment='center', fontsize=12, fontfamily='monospace')
plt.axis('off') # Ta bort axlar och ramar
output_file = './prediction_with_AI/figlet_output.png'
plt.savefig(output_file, bbox_inches='tight', pad_inches=0) # Spara som PNG-fil
plt.show()

print("Bilden sparades i:", output_file)
