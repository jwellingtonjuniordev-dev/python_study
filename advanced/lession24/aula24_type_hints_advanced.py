"""
Até agora você já usou anotações como:

def add(a: int, b: int) -> int:
    return a + b

Mas isso é apenas a ponta do iceberg.

O módulo typing torna o código mais legível, facilita o autocompletar da IDE, ajuda ferramentas como mypy e é amplamente utilizado por frameworks como FastAPI, Pydantic e Django.

O que são Type Hints?

Type Hints são anotações de tipo.

Eles não impedem que o código rode com outro tipo (por padrão), mas servem para:

documentar o código;
ajudar a IDE;
detectar erros antes da execução;
facilitar a manutenção.

Exemplo:

def greet(name: str) -> str:
    return f"Hello, {name}!"

Aqui estamos dizendo:

name deve ser uma str;
a função retorna uma str.

1. Optional
O que é?

Significa:

"Esse valor pode ser daquele tipo ou None."

Na prática:

Optional[str]

é o mesmo que:

str | None

(em Python 3.10+)

Exemplo:

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "John"

    return None

2. Union
O que é?

Permite aceitar mais de um tipo.

Exemplo:

from typing import Union

def square(value: Union[int, float]) -> float:
    return value * value

Hoje também podemos escrever:

def square(value: int | float) -> float:
    return value * value

3. Any
O que é?

Aceita qualquer tipo.

from typing import Any

def show(value: Any):
    print(value)

Pode receber:

show(10)
show("Python")
show(True)
show([1,2,3])

⚠ Use com moderação.

Quando usamos Any, perdemos boa parte dos benefícios dos Type Hints.

4. List, Dict e Tuple

Você já conhece listas e dicionários.

Agora podemos informar o tipo dos elementos.

Exemplo:

from typing import List

names: List[str] = [
    "John",
    "Mary",
    "Alice"
]

Ou, em Python moderno:

names: list[str]

Dicionário:

products: dict[str, float]

Exemplo:

products = {
    "Laptop": 1200,
    "Mouse": 25
}

Tupla:

coordinates: tuple[int, int]

5. Callable
O que é?

Representa uma função.

Exemplo:

from typing import Callable

def calculate(
    operation: Callable[[int, int], int]
):

    print(operation(10,5))

Uso:

def add(a, b):
    return a + b

calculate(add)

Muito usado em callbacks.

6. Literal

Permite aceitar apenas valores específicos.

Exemplo:

from typing import Literal

def payment(
    method: Literal[
        "pix",
        "card",
        "cash"
    ]
):
    ...

Agora:

payment("pix")

✔ válido.

Mas:

payment("bitcoin")

A IDE já avisa que está incorreto.

7. Final

Indica que uma variável não deveria mudar.

from typing import Final

PI: Final = 3.14159

É como uma constante.

Onde isso aparece no mundo real?

FastAPI:

@app.get("/users/{id}")
def get_user(id: int):

Pydantic:

class User(BaseModel):

    name: str
    age: int

SQLAlchemy:

id: Mapped[int]
name: Mapped[str]

Tudo isso depende dos conceitos que estamos estudando agora.

"""