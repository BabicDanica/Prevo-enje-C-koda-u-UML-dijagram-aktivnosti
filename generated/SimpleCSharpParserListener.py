# Generated from grammars/SimpleCSharpParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleCSharpParser import SimpleCSharpParser
else:
    from SimpleCSharpParser import SimpleCSharpParser

# This class defines a complete listener for a parse tree produced by SimpleCSharpParser.
class SimpleCSharpParserListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleCSharpParser#compilationUnit.
    def enterCompilationUnit(self, ctx:SimpleCSharpParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#compilationUnit.
    def exitCompilationUnit(self, ctx:SimpleCSharpParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#usingDirective.
    def enterUsingDirective(self, ctx:SimpleCSharpParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#usingDirective.
    def exitUsingDirective(self, ctx:SimpleCSharpParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#namespaceDecl.
    def enterNamespaceDecl(self, ctx:SimpleCSharpParser.NamespaceDeclContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#namespaceDecl.
    def exitNamespaceDecl(self, ctx:SimpleCSharpParser.NamespaceDeclContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#classDecl.
    def enterClassDecl(self, ctx:SimpleCSharpParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#classDecl.
    def exitClassDecl(self, ctx:SimpleCSharpParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#accessModifier.
    def enterAccessModifier(self, ctx:SimpleCSharpParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#accessModifier.
    def exitAccessModifier(self, ctx:SimpleCSharpParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#classMember.
    def enterClassMember(self, ctx:SimpleCSharpParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#classMember.
    def exitClassMember(self, ctx:SimpleCSharpParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#constructorDecl.
    def enterConstructorDecl(self, ctx:SimpleCSharpParser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#constructorDecl.
    def exitConstructorDecl(self, ctx:SimpleCSharpParser.ConstructorDeclContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#methodDecl.
    def enterMethodDecl(self, ctx:SimpleCSharpParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#methodDecl.
    def exitMethodDecl(self, ctx:SimpleCSharpParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#parameterList.
    def enterParameterList(self, ctx:SimpleCSharpParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#parameterList.
    def exitParameterList(self, ctx:SimpleCSharpParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#parameter.
    def enterParameter(self, ctx:SimpleCSharpParser.ParameterContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#parameter.
    def exitParameter(self, ctx:SimpleCSharpParser.ParameterContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#varDecl.
    def enterVarDecl(self, ctx:SimpleCSharpParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#varDecl.
    def exitVarDecl(self, ctx:SimpleCSharpParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#type.
    def enterType(self, ctx:SimpleCSharpParser.TypeContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#type.
    def exitType(self, ctx:SimpleCSharpParser.TypeContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#statement.
    def enterStatement(self, ctx:SimpleCSharpParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#statement.
    def exitStatement(self, ctx:SimpleCSharpParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#block.
    def enterBlock(self, ctx:SimpleCSharpParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#block.
    def exitBlock(self, ctx:SimpleCSharpParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#breakStatement.
    def enterBreakStatement(self, ctx:SimpleCSharpParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#breakStatement.
    def exitBreakStatement(self, ctx:SimpleCSharpParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SimpleCSharpParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SimpleCSharpParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleCSharpParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleCSharpParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#forStatement.
    def enterForStatement(self, ctx:SimpleCSharpParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#forStatement.
    def exitForStatement(self, ctx:SimpleCSharpParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#varInit.
    def enterVarInit(self, ctx:SimpleCSharpParser.VarInitContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#varInit.
    def exitVarInit(self, ctx:SimpleCSharpParser.VarInitContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#exprInit.
    def enterExprInit(self, ctx:SimpleCSharpParser.ExprInitContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#exprInit.
    def exitExprInit(self, ctx:SimpleCSharpParser.ExprInitContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleCSharpParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleCSharpParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:SimpleCSharpParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:SimpleCSharpParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#switchStatement.
    def enterSwitchStatement(self, ctx:SimpleCSharpParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#switchStatement.
    def exitSwitchStatement(self, ctx:SimpleCSharpParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#switchBlock.
    def enterSwitchBlock(self, ctx:SimpleCSharpParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#switchBlock.
    def exitSwitchBlock(self, ctx:SimpleCSharpParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#switchSection.
    def enterSwitchSection(self, ctx:SimpleCSharpParser.SwitchSectionContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#switchSection.
    def exitSwitchSection(self, ctx:SimpleCSharpParser.SwitchSectionContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#switchLabel.
    def enterSwitchLabel(self, ctx:SimpleCSharpParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#switchLabel.
    def exitSwitchLabel(self, ctx:SimpleCSharpParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#tryCatchStatement.
    def enterTryCatchStatement(self, ctx:SimpleCSharpParser.TryCatchStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#tryCatchStatement.
    def exitTryCatchStatement(self, ctx:SimpleCSharpParser.TryCatchStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#catchClause.
    def enterCatchClause(self, ctx:SimpleCSharpParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#catchClause.
    def exitCatchClause(self, ctx:SimpleCSharpParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#finallyClause.
    def enterFinallyClause(self, ctx:SimpleCSharpParser.FinallyClauseContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#finallyClause.
    def exitFinallyClause(self, ctx:SimpleCSharpParser.FinallyClauseContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#returnStatement.
    def enterReturnStatement(self, ctx:SimpleCSharpParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#returnStatement.
    def exitReturnStatement(self, ctx:SimpleCSharpParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#expression.
    def enterExpression(self, ctx:SimpleCSharpParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#expression.
    def exitExpression(self, ctx:SimpleCSharpParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#assignmentExpr.
    def enterAssignmentExpr(self, ctx:SimpleCSharpParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#assignmentExpr.
    def exitAssignmentExpr(self, ctx:SimpleCSharpParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#logicExpr.
    def enterLogicExpr(self, ctx:SimpleCSharpParser.LogicExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#logicExpr.
    def exitLogicExpr(self, ctx:SimpleCSharpParser.LogicExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#equalityExpr.
    def enterEqualityExpr(self, ctx:SimpleCSharpParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#equalityExpr.
    def exitEqualityExpr(self, ctx:SimpleCSharpParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#relationalExpr.
    def enterRelationalExpr(self, ctx:SimpleCSharpParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#relationalExpr.
    def exitRelationalExpr(self, ctx:SimpleCSharpParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:SimpleCSharpParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:SimpleCSharpParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#multExpr.
    def enterMultExpr(self, ctx:SimpleCSharpParser.MultExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#multExpr.
    def exitMultExpr(self, ctx:SimpleCSharpParser.MultExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#unaryExpr.
    def enterUnaryExpr(self, ctx:SimpleCSharpParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#unaryExpr.
    def exitUnaryExpr(self, ctx:SimpleCSharpParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#postfixExpr.
    def enterPostfixExpr(self, ctx:SimpleCSharpParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#postfixExpr.
    def exitPostfixExpr(self, ctx:SimpleCSharpParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:SimpleCSharpParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:SimpleCSharpParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#literal.
    def enterLiteral(self, ctx:SimpleCSharpParser.LiteralContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#literal.
    def exitLiteral(self, ctx:SimpleCSharpParser.LiteralContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#constantExpression.
    def enterConstantExpression(self, ctx:SimpleCSharpParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#constantExpression.
    def exitConstantExpression(self, ctx:SimpleCSharpParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCSharpParser#argumentList.
    def enterArgumentList(self, ctx:SimpleCSharpParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by SimpleCSharpParser#argumentList.
    def exitArgumentList(self, ctx:SimpleCSharpParser.ArgumentListContext):
        pass



del SimpleCSharpParser