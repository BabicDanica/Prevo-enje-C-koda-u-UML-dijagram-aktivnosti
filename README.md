# C# Activity Diagram Generator

## Opis projekta

Ovaj projekat implementira prevodilac koji iz C# izvornog koda generiše UML dijagrame aktivnosti koristeći ANTLR za analizu koda i PlantUML za vizualizaciju. Cilj je automatizovati proces kreiranja dijagrama toka izvršenja programa kako bi se olakšalo razumevanje i dokumentacija softverskih sistema.

Prevodilac prepoznaje osnovne kontrolne strukture (grananja, petlje, povratne vrednosti) i prevodi ih u odgovarajuće PlantUML konstrukcije za dijagrame aktivnosti.

---

## Ključne funkcionalnosti

- Parsiranje C# koda pomoću ANTLR4 gramatike.
- Generisanje apstraktnog sintaksnog stabla (AST).
- Traversiranje AST-a radi prepoznavanja kontrolnih struktura (if, else-if, else, for, while, do-while).
- Generisanje PlantUML koda za aktivnosti, početne i završne tačke, grananja i petlje.
- Pokretanje PlantUML alata iz Pythona za automatsko kreiranje grafičkog dijagrama u PNG ili SVG formatu.
- Podrška za višestruke metode i generisanje zasebnih dijagrama po metodi.

---

## Tehnologije

- **ANTLR 4 (verzija 4.13.0)** – alat za generisanje parsera na osnovu definisane gramatike.
- **Python 3 (preporučeno 3.9+)** – za implementaciju logike parsiranja, generisanja PlantUML koda i automatizaciju poziva PlantUML-a.
- **PlantUML** – alat za generisanje UML dijagrama iz tekstualnog opisa.
- **Java Runtime Environment (JRE)** – neophodan za izvršavanje PlantUML `.jar` fajla.

---

## Korišćeni JAR fajlovi

- **antlr-4.13.0-complete.jar**  
  Kompletniji alat za generisanje parsera i lexer-a na osnovu definisanih gramatika. Koristi se za generisanje Python parsera iz `.g4` fajlova koji analiziraju C# kod.

- **plantuml.jar**  
  Java aplikacija koja prima PlantUML tekstualni fajl i generiše odgovarajuće UML dijagrame u grafičkom formatu (PNG, SVG itd.). Projekat poziva ovaj `.jar` za automatsku konverziju generisanog koda u vizuelne dijagrame.

---

## Pokretanje projekta

Pokrenite glavnu skriptu sa putanjom do ulaznog C# fajla i foldera za izlazne dijagrame:

```bash
python3 src/main.py input/simple1.cs output/

project_root/
│
├── grammars/                          # ANTLR definicije gramatike za C# (.g4 fajlovi)
│   ├── SimpleCSharpLexer.g4
│   └── SimpleCSharpParser.g4
│
├── generated/                        # Automatski generisani Python parser i lexer fajlovi
│   ├── SimpleCSharpLexer.py
│   └── SimpleCSharpParser.py
│
├── input/                           # Ulazni C# izvori za analizu i testiranje
│   ├── simple1.cs
│   ├── simple2.cs
│   ├── complex1.cs
│   └── complex2.cs
│
├── output/                          # Izlazni fajlovi: PlantUML skripte i generisani dijagrami
│   ├── simple1.puml
│   ├── simple1.png
│   └── ...
│
├── src/                            # Python skripte za analizu, generisanje i integraciju
│   ├── main.py                     # Glavna skripta koja pokreće ceo proces
│   ├── listener.py                 # ANTLR listener za parsiranje i semantičku analizu
│   ├── semantic_analyzer.py        # Moduli za semantičku analizu i proveru koda
│   ├── uml_generator.py            # Generisanje PlantUML koda iz apstraktnog sintaksnog stabla
│   └── plantuml_runner.py          # Skripta za pozivanje PlantUML alata i kreiranje dijagrama
│

