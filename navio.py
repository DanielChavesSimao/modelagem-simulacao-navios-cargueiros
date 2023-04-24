from random import random

from manim import *


class Navio:
    def __init__(self, nome, env, cai_p, cai_g):
        self.nome = nome
        self.env = env
        self.cai_p = cai_p
        self.cai_g = cai_g
        self.tempo_chegada = 0.
        self.tempo_carregamento = 0.
        self.tempo_pagamento = 0.
        self.dot = Dot()

    def chegada(self):
        """
        Define o comportamento de chegada do navio
        :return:
        """
        # while True:
        # Gera o tempo de intervalo entre chegadas
        yield self.env.timeout(self.tempo_chegada)
        # self.dot.move_to([np.random.uniform(-10, 10), np.random.uniform(-10, 10), 0])
        # self.env.scene.play(Create(self.dot))
        print(self.nome, "chegou ao porto em", self.env.now)

        # Cria o processo de carregamento
        self.env.process(self.carregamento())

    def carregamento(self):
        """
        Define o comportamento de carregamento do navio
        :return:
        """
        with self.cai_p.request() as req:
            # Aguarda até conseguir acesso ao cais
            yield req

            # Gera o tempo de carregamento
            print(self.nome, "começou a carregar em", self.env.now)
            yield self.env.timeout(self.tempo_carregamento)
            print(self.nome, "terminou de carregar em", self.env.now)

            # Cria o processo de pagamento
            self.env.process(self.pagamento())

    def pagamento(self):
        """
        Define o comportamento de pagamento do navio
        :return:
        """
        with self.cai_g.request() as req:
            # Aguarda até conseguir acesso ao cais de pagamento
            yield req

            # Gera o tempo de pagamento
            print(self.nome, "começou a pagar em ", self.env.now)
            yield self.env.timeout(self.tempo_pagamento)

            # Navio deixa o porto
            print(self.nome, "deixou o porto em", self.env.now)
