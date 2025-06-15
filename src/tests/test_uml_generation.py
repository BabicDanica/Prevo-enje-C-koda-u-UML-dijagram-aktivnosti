import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from generated.SimpleCSharpLexer import SimpleCSharpLexer
from generated.SimpleCSharpParser import SimpleCSharpParser
from uml_generator import UMLGenerator

class TestUMLGeneration(unittest.TestCase):
    def test_complex_class(self):
        code = """
        namespace ComplexNamespace.SubNamespace {
            public class ComplexClass {
                private int id;
                protected string name;
                public bool isActive;

                public ComplexClass(int id, string name) {
                    this.id = id;
                    this.name = name;
                    this.isActive = true;
                }

                public void Activate() {
                    isActive = true;
                }

                private void Deactivate() {
                    isActive = false;
                }
            }

            internal class Helper {
                public static void Log(string message) { }
            }
        }
        """

        input_stream = InputStream(code)
        lexer = SimpleCSharpLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = SimpleCSharpParser(tokens)
        tree = parser.compilationUnit()

        walker = ParseTreeWalker()
        uml_generator = UMLGenerator()
        walker.walk(uml_generator, tree)
        
        uml_output = uml_generator.generate_plantuml()
        
        # Provera osnovnih stvari
        self.assertIn("namespace ComplexNamespace.SubNamespace", uml_output)
        self.assertIn("class ComplexClass", uml_output)
        self.assertIn("private int id", uml_output)
        self.assertIn("protected string name", uml_output)
        self.assertIn("public bool isActive", uml_output)
        self.assertIn("public void Activate()", uml_output)
        self.assertIn("private void Deactivate()", uml_output)
        self.assertIn("ComplexClass(int id, string name)", uml_output)
        self.assertIn("class Helper", uml_output)
        self.assertIn("public static void Log(string message)", uml_output)

if __name__ == '__main__':
    unittest.main()
