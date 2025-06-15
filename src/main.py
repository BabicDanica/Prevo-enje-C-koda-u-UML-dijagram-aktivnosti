import os
import sys
from antlr4 import *

# Dodajemo nadređeni direktorijum u sys.path da bismo mogli importovati naše module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from generated.SimpleCSharpLexer import SimpleCSharpLexer
from generated.SimpleCSharpParser import SimpleCSharpParser
from semantic_analyzer import SemanticAnalyzer
from listener import ActivityDiagramListener as ActivityDiagramGenerator
from plantuml_runner import generate_diagram_from_file


def main():
    # Provera da li je korisnik prosledio putanju do ulaznog fajla
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    # Čitamo ulazni fajl kao tok karaktera
    input_stream = FileStream(input_path, encoding='utf-8')
    
    # Kreiramo lexer koji deli tok na tokene
    lexer = SimpleCSharpLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # Kreiramo parser koji parsira tokene i pravi sintaksno stablo
    parser = SimpleCSharpParser(tokens)
    tree = parser.compilationUnit()

    # Semantička analiza
    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()

    # Prolaz kroz sintaksno stablo radi semantičke analize (provera tipova, definicija itd)
    walker.walk(semantic_analyzer, tree)

    # Ako postoje semantičke greške, prikazujemo ih i završavamo program
    if semantic_analyzer.has_errors():
        print("Semantičke greške pronađene:")
        for err in semantic_analyzer.get_errors():
            print(" -", err)
        sys.exit(1)

    # Generisanje dijagrama
    activity_generator = ActivityDiagramGenerator()
    walker.walk(activity_generator, tree)

    # Dobijamo generisane UML dijagrame po metodama
    diagrams = activity_generator.get_activity_diagrams()

    # Pripremamo izlazni direktorijum i ime fajla bez ekstenzije
    filename = os.path.basename(input_path)
    base_filename = os.path.splitext(filename)[0]
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Za svaki metod generišemo PlantUML fajl i pozivamo PlantUML da napravi dijagram
    for method_name, lines in diagrams.items():
        output_file = os.path.join(output_dir, f"{base_filename}_{method_name}_activity.puml")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Generated diagram: {output_file}")

        # Poziv spoljnog alata PlantUML da generiše dijagram iz fajla
        generate_diagram_from_file(output_file)
        #(poziva plantuml.jar preko subprocess)

if __name__ == '__main__':
    main()
