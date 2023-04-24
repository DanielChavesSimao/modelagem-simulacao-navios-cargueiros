import pandas
import simpy
from scipy.stats import gamma, kstest
from cais import Cais
from my_gamma import MyGamma
from navio import Navio
from manim import *


class Simulacao(simpy.Environment):

    def __init__(self, scene, num_navios=170):
        super().__init__()
        self.num_navios = num_navios
        self.navios = []
        self.empiric_data = pandas.read_csv('dados_empiricos.csv')
        self.gamma_models = [MyGamma(**gamma_data, mode='np') for gamma_data in self.my_gamma_fit()]
        # self.gamma_models = [MyGamma(**gamma_data, mode='custom') for gamma_data in self.my_gamma_fit()]
        self.scene = scene
        self.cais_p = Cais(self, capacity=1)
        self.cais_g = Cais(self, capacity=1)
        self.criar_navios()

    def plot_cummulative_hist_in_axes(self, axs):
        """
        Plota o histograma cumulativo junto da dist.gamma e compara com rngs gerados por numpy.
        :param axs:
        :return:
        """
        for gamma_model, ax in zip(self.gamma_models, axs):
            ax.hist(gamma_model.data, bins='auto', density=True, histtype='step', cumulative=True,
                    label='Dados empiricos')
            ax.hist(np.random.default_rng().gamma(gamma_model.shape, gamma_model.scale,
                                                  2000) + gamma_model.loc, bins='auto',
                    density=True,
                    histtype='step',
                    cumulative=True, label='NumPy gen')
            ax.hist(MyGamma(gamma_model.shape, gamma_model.loc, gamma_model.scale).generate(2000),
                    bins='auto', density=True, histtype='step',
                    cumulative=True, label='Teste')
            x = np.linspace(min(gamma_model.data), max(gamma_model.data), len(gamma_model.data))
            ax.plot(x, gamma.cdf(x, a=gamma_model.shape, loc=gamma_model.loc, scale=gamma_model.scale),
                    label='Gamma dist')
            ax.legend(loc='right')

    def my_gamma_fit(self):
        """
        le o csv e retorna os dados, shape, location e scale de cada coluna
        :return:
        """
        model_data_list = list()
        for col in self.empiric_data.columns:
            dados_empiricos = list(self.empiric_data[col])
            parametros_empiricos = gamma.fit(dados_empiricos)
            kstest_resultado_empirico = kstest(dados_empiricos, "gamma", parametros_empiricos)
            shape, location, scale = parametros_empiricos
            print(f"{kstest_resultado_empirico=}")
            model_data_list.append({
                'data': dados_empiricos,
                'shape': shape,
                'loc': location,
                'scale': scale
            })

        return model_data_list

    def criar_navios(self):
        for i in range(self.num_navios):
            self.navios.append(Navio(f"Navio {i}", self, self.cais_p, self.cais_g))
            self.navios[i].tempo_chegada = self.gamma_models[0].get_one()
            self.navios[i].tempo_carregamento = self.gamma_models[1].get_one()
            self.navios[i].tempo_pagamento = self.gamma_models[2].get_one()
            self.navios[i].dot = Dot()
            self.process(self.navios[i].chegada())

        grupo = VGroup(*[navio.dot for navio in self.navios]).set_x(0).arrange(buff=1.0)
        self.scene.add(grupo)
