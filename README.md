Detta repo innehåller arbete som jag utfört i en utbildning på IT-högskolan. Utbildningen heter "Pythonprogrammering för AI-utveckling" 
Länk till beskrivning av kursen "https://www.ithsdistans.se/pluginfile.php/84214/mod_resource/content/1/Pythonprogrammering%20f%C3%B6r%20AI-utveckling%2030p.pdf"

Som en del av utbildningen ska ett eget projekt väljas och drivas. Jag lägger en länk till beskrivningen av första steget "https://www.ithsdistans.se/pluginfile.php/86333/mod_resource/content/1/Det%20egna%20projektet%20Steg%201.pdf". 

Projektet lämnas sedan in genom ett github-repo där all kod och dokumentations ska finnas. Mitt projekt finns således i detta repo. Jag har också valt att lägga in en laboration i repot. 

Följande delar/filer kan hittas i projektet: 
* .gitignore (ignorerbara filer(mappar))
* API_call.py (OBS! Denna kan inte köras igen då API:et har ändrade begränsningar)
* Project_step_1.ipynb (I denna finns första steget i projektet som också är en inlämning)
* README.md (denna fil)
* aras.py (sparar ned bilden nedan, figlet_output.png)
* figlet_output.png
* requirements.txt (innehåller dom installationer som krävs för att köra koden)
* src/ (source till alla filer. Se nedan för utförlig info)
    * LAG/ (Här är material (kod,csv-filer)för arbete med tekniken LAG)
     * 'crypto_AI.ipynb' är arbetsboken
    * LSTM (Material för arbete enligt LSTM)
     * csv/ (innehåller csv-filer)
     * AI_LSTM_Neutral_Network.ipynb är arbetsboken
     * ITHS_mission_1_game/ (en laboration som lämnades in i utbildningen)

    Jag har även valt att ha kvar övrigt material för att ha allt samlat i ett repo. tex så finns:
     * spam_mail/ (ett litet test-projekt)
     * additional_material (diverse filer där jag har lekt runt för att hitta en väg frammåt)
     * Crypto (innehåller också en hel del testmaterial)



Som mitt projekt valde jag att undersöka möjligheten att bygga en model som kan förutsäga börspriser. I mitt fall krypto (Ethereum). 

![](figlet_output.png)


OBSERVERA att det är följande filer som är själva arbetsfilerna för mitt projekt:
 * 'crypto_AI.ipynb'
 *  'AI_LSTM_Neutral_Network.ipynb'

# Installation
Med fördel starta en virtuell miljö i ditt system. Då jag kör WSL har jag använt följande kommandon:

```bash
python3 -m venv aras_venv
source aras_venv/bin/activate
deactivate(avaktivera virtuellt envirement)
```
där aras_venv är mitt namn på min venv(virtuell miljö)

Beroende på vilket system du kör tex ren windows behöver du använda modifieringar av ovan kommandon.

Kör fil 'requirements.txt' med nedanstående kommando i terminalen så installeras dom bibliotek som krävs för koden. 

```bash
pip install -r requirements.txt
```


Jag kör **Python3.9** på min dator. Kör du en tidigare version kan det ge problem i koden! 