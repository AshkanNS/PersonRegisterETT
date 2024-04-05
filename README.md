Webbapplikation byggd med Flask som möjliggör för användare att se en lista över personer registrerade i systemet samt visa detaljerad information för varje individ.
Starta igång
För att komma igång med PersonRegister, följ dessa steg:

Innan du installerar, se till att du har följande installerat:
- Python 3
- pip
- virtualenv
- 
Installation
1. Klona projektets repository till din lokala maskin:
```bash
git clone https://github.com/AshkanNS/PersonRegisterETT.git
cd PersonRegisterETT

python3 -m venv venv
source venv/bin/activate  För Unix eller MacOS
venv\Scripts\activate  För Windows

pip install -r requirements.txt
flask run
