/* Advent of Code 2020 Day 18 math with new rules
 * I took the code from bison examples and changed it
 * to fit the required functionality
 *
 * Ralph Ganszky
 */

%require "3.2"
%language "c++"

%{
#include <cctype>
#include <iostream>
#include <string>

int64_t yylex();
%}

%define api.value.type variant
%define api.token.constructor

%nterm <int64_t> exp;
%nterm <int64_t> line;
%nterm <int64_t> lines;
%token <int64_t> NUM;
%token           PLUS;
%token           TIMES;
%token           OPEN;
%token           CLOSE;
%token           NEW_LINE;

%left TIMES
%left PLUS

%code {
    namespace yy {
        auto yylex() -> parser::symbol_type {
            while (!std::cin.eof()) {
                char c = std::cin.peek();
                if (std::isdigit(c)) {
                    int64_t val;
                    std::cin >> val;
                    return parser::make_NUM(val);
                } else if (std::isspace(c)) {
                    std::cin.get(c);
                    if (c == '\n')
                        return parser::make_NEW_LINE();
                } else {
                    std::cin.get(c);
                    if (c == '+')
                        return parser::make_PLUS();
                    else if (c == '*')
                        return parser::make_TIMES();
                    else if (c == '(')
                        return parser::make_OPEN();
                    else if (c == ')')
                        return parser::make_CLOSE();
                    else
                        return c;
                }
            }
            return parser::make_YYEOF();
        }
    }
}

%% // The grammar rules

result:
    lines               { std::cout << $1 << '\n'; }
;

lines:
    line                { $$ = $1; }
|   lines line          { $$ = $1 + $2; }
;

line:
    exp NEW_LINE        { $$ = $1; }
|   exp YYEOF           { $$ = $1; }
;

exp:
    NUM                 { $$ = $1; }
|   exp PLUS exp        { $$ = $1 + $3; }
|   exp TIMES exp       { $$ = $1 * $3; }
|   OPEN exp CLOSE      { $$ = $2; }
;

%%

namespace yy {
    auto parser::error(const std::string& msg) -> void {
        std::cerr << msg << '\n';
    }
}

int
main ()
{
  yy::parser parse;
  // parse.set_debug_level(1);
  return parse();
}
