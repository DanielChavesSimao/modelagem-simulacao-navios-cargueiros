# Trabalho de modelagem e simulação

## Descrição
### Modelagem
Navios cargueiros com 3 intervalos de tempo (chegada, carregamento e pagamento) seguindo a distribuição gamma de densidade de probabilidades.

A implementação de modo custom da modelagem gamma está com problemas mas a implementação do numpy parece funcionar de acordo.

### Simulação
Usando simpy temos dois cais como resource e os usuários são os navios criados, com tempos gerados randomicamente seguindo a modelagem.


### Animação
Por ora o desenvolvimento da animação que seria feita utilizando matplotlib e/ou manim foi apenas iniciado e não concluído.


## Instalação
Requisitos: python3, matplotlib, numpy, [manim](https://docs.manim.community/en/stable/installation.html)

```
pip3 install matplotlib numpy
```

```bash
# Gerar animação via manim
manim -qlp main.py NaviosCargueiros
```

```bash
# Executar a modelagem e simulação
python main.py
```
