#Ovaj skript služi da uzme PlantUML kod (tekstualni opis dijagrama) i pomoću PlantUML alata (Java aplikacije)
#  transformiše taj kod u grafički format (kao što su PNG, SVG, itd.).
#tj koraci:
#1.Uzima PlantUML kod (tekstualni opis dijagrama).
#2.Pokreće PlantUML JAR koristeći Java da generiše sliku dijagrama (npr. PNG fajl).
#3.Snima tu sliku na disk.
#pre ovoga proverava da li je java dostupna sistemu i da li postoji plantuml.fajl, koje koristi za generisanje 
# dijagrama u zeljenom formatu
import subprocess
import sys
import os
import shutil

# Putanja do plantuml.jar
PLANTUML_JAR_PATH = 'plantuml.jar'


def check_environment():
    """
    Proverava da li je Java instalirana i dostupna (da je u PATH),
    i da li postoji plantuml.jar fajl na zadatoj putanji.
    Vraća True ako je sve u redu, False ako nešto nedostaje.
    """
    if shutil.which("java") is None:
        print("Greška: java nije instaliran ili nije u PATH promenljivoj.")
        return False
    if not os.path.exists(PLANTUML_JAR_PATH):
        print(f"Greška: fajl {PLANTUML_JAR_PATH} ne postoji.")
        return False
    return True


def generate_diagram_from_file(input_puml_path, output_format='png', output_path=None):
    """
    Generiše dijagram iz .puml fajla pozivanjem PlantUML preko java procesa.
    - input_puml_path: putanja do .puml fajla sa PlantUML kodom
    - output_format: željeni izlazni format (png, svg, itd.), default 'png'
    - output_path: gde će se sačuvati generisani fajl, ako nije zadato, koristi se isto ime kao input sa promenjenom ekstenzijom

    Pokreće komandu: java -jar plantuml.jar -t<format> <input_puml_path>
    """
    if not os.path.exists(input_puml_path):
        print(f"Fajl {input_puml_path} ne postoji.")
        return False

    if output_path is None:
        base, _ = os.path.splitext(input_puml_path)
        output_path = f"{base}.{output_format}"

    # Komanda za generisanje dijagrama
    cmd = ['java', '-jar', PLANTUML_JAR_PATH, f'-t{output_format}', input_puml_path]

    try:
        # Pokretanje procesa i čekanje da završi
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"Dijagram je generisan i sačuvan u {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        # Ako java ili PlantUML prijave grešku, štampa je
        print("Greška pri generisanju dijagrama:")
        print(e.stderr.decode())
        return False


def generate_diagram_from_text(plantuml_text, output_path='diagram.png'):
    """
    Generiše dijagram iz PlantUML teksta (stringa) koristeći standardni ulaz.
    PlantUML prima tekst preko pipe-a, i ispisuje sliku na standardni izlaz.
    Snima izlaz u fajl output_path.

    Komanda: java -jar plantuml.jar -tpng -pipe
    """
    cmd = ['java', '-jar', PLANTUML_JAR_PATH, '-tpng', '-pipe']

    try:
        # Otvara podproces sa stdin, stdout, stderr kao cevi
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Šalje PlantUML tekst u stdin i čeka rezultat
        stdout_data, stderr_data = proc.communicate(plantuml_text.encode('utf-8'))
        if proc.returncode != 0:
            print("Greška pri generisanju dijagrama:")
            print(stderr_data.decode())
            return False
        # Snima rezultat (binarni PNG) u fajl
        with open(output_path, 'wb') as f:
            f.write(stdout_data)
        print(f"Dijagram je generisan i sačuvan u {output_path}")
        return True
    except Exception as e:
        print("Greška:", e)
        return False


if __name__ == '__main__':
    # Proveri okruženje pre svega
    if not check_environment():
        sys.exit(1)

    # Jednostavan komandno-linijski interfejs za testiranje
    if len(sys.argv) < 2:
        print("Koristi: python plantuml_runner.py [puml_file | -text 'plantuml_text']")
        sys.exit(1)

    if sys.argv[1] == '-text':
        if len(sys.argv) < 3:
            print("Nije unet PlantUML tekst.")
            sys.exit(1)
        # Ako se koristi -text opcija, spoji sve argumente nakon -text u jedan string
        plantuml_text = " ".join(sys.argv[2:])
        generate_diagram_from_text(plantuml_text)
    else:
        # Ako nije -text, tretiraj prvi argument kao putanju do .puml fajla
        input_file = sys.argv[1]
        generate_diagram_from_file(input_file)
