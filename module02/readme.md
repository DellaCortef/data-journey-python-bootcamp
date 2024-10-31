# module02 - TypeError, Type Check, Type Conversion, try-except and if
The objective of the module is to present strategies on how we can prevent errors from happening.We will look at some simple error handling and error workaround practices.

We will review what we studied in module01 about variables.

And finally, we'll talk about flows. What is the behavior like within **Python**.

### Topics:
Python supports several simple data types such as:

- **Integers (`int`)**: Represent whole numbers.
- **Floating Point (`float`)**: Represent real numbers.
- **Strings (`str`)**: Represent sequences of characters.
- **Booleans (`bool`)**: Represent true (`True`) or false (`False`) values.

#### 1. Integers (`int`)

* **Methods and operations:**
    1. `+` (addition)
    2. `-` (subtraction)
    3. `*` (multiplication)
    4. `//` (integer division)
    5. `%` (modulo - remainder of division)

#### 2. Floating Point Numbers (`float`)

* **Methods and operations:**
    1. `+` (addition)
    2. `-` (subtraction)
    3. `*` (multiplication)
    4. `/` (division)
    5. `**` (empowerment)

#### 3. Strings (`str`)

* **Methods and operations:**
    1. `.upper()` (converts to uppercase)
    2. `.lower()` (converts to lowercase)
    3. `.strip()` (removes leading and trailing whitespace)
    4. `.split(sep)` (splits the string into a list, using `sep` as delimiter)
    5. `+` (string concatenation)

#### 4. Booleans (`bool`)

* **Logical operations:**
    1. `and` (logical And)
    2. `or` (logical OR)
    3. `not` (NOT logical)
    4. `==` (equality)
    5. `!=` (difference)



# TypeError, Type Check e Type Conversion em Python
Python é uma linguagem de programação dinâmica, mas fortemente tipada, o que significa que não é necessário declarar tipos de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: TypeError, verificação de tipo (type check), e conversão de tipo (type conversion).

## TypeError

Um `TypeError` ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

### Exemplo de TypeError

Um exemplo clássico é tentar utilizar a função `len()` com um inteiro, o que resulta em `TypeError`, pois `len()` espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.

```python
# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
```

O código acima tenta obter o comprimento de um inteiro, o que não faz sentido, resultando na mensagem de erro: "object of type 'int' has no len()".
