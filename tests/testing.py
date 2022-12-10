import unittest
import matplotlib.pyplot as plt
import numpy as np
from replica.processes import BrownianMotion, GBM, Vasicek, OUProcess, CIRProcess, CEVProcess


def test_sample(self):
    sample = self.process.sample(self.n)
    times = self.process.times
    self.assertEqual(len(times), len(self.grid_times))
    for (t1, t2) in zip(times, self.grid_times):
        self.assertEqual(t1, t2)
    plt.plot(times, sample)
    plt.show()


def test_sample_at(self):
    sample = self.process.sample_at(self.times_given)
    times = self.process.times
    for (t1, t2) in zip(times, self.times_given):
        self.assertEqual(t1, t2)
    self.assertEqual(len(times), len(sample))
    plt.plot(times, sample)
    plt.show()


class TestProcesses(unittest.TestCase):

    def setUp(self) -> None:
        self.N = 100
        self.n = 100
        self.T = 1.0
        self.times_given = np.linspace(0, 1.0, 100, endpoint=True)
        self.grid_times = np.linspace(0, self.T, self.n)

    def test_BM(self):
        process = BrownianMotion()
        process.plot(n=100, N=3)
        process.draw(n=100, N=200)
        process.draw(n=100, N=200, envelope=True)
        process.draw(n=100, N=200, marginal=False)
        process.draw(n=100, N=200, marginal=False, envelope=True)


    def test_GBM(self):
        process = GBM(drift=1.0, volatility=0.5)
        process.plot(n=100, N=3)
        process.draw(n=100, N=200)
        process.draw(n=100, N=200, envelope=True)
        process.draw(n=100, N=200, marginal=False)
        process.draw(n=100, N=200, marginal=False, envelope=True)

    def test_Vasicek(self):
        process = Vasicek(theta=1.5, mu=1.0, sigma=0.6, initial=4.0)
        process.plot(n=100, N=3)
        process.draw(n=100, N=200)
        process.draw(n=100, N=200, envelope=True)
        process.draw(n=100, N=200, marginal=False)
        process.draw(n=100, N=200, marginal=False, envelope=True)

    def test_OU(self):
        process = OUProcess(theta=1.5, sigma=0.6, initial=4.0)
        process.plot(n=100, N=3)
        process.draw(n=100, N=200)
        process.draw(n=100, N=200, envelope=True)
        process.draw(n=100, N=200, marginal=False)
        process.draw(n=100, N=200, marginal=False, envelope=True)


    def test_CIR(self):
        process = CIRProcess(T=self.T, theta=0.06, mu=0.01, sigma=0.009)
        process.plot(n=100, N=3)
        process.draw(n=100, N=200)
        process.draw(n=100, N=200, marginal=True)
        process.draw(n=100, N=200, marginal=True, envelope=True)
        process.draw(n=100, N=200, envelope=True)

    def test_CIRProcess_params(self):
        with self.assertRaises(ValueError):
            self.process = CIRProcess(T=self.T, theta=-0.06, mu=0.01, sigma=0.009)
        with self.assertRaises(ValueError):
            self.process = CIRProcess(T=self.T, theta=1.0, mu=1.0, sigma=3.0)

    def test_CEV(self):
        process = CEVProcess(gamma=0.5, mu=1.50, sigma=0.6, initial=1.0)
        process.plot(n=100, N=3)
        process.draw(n=100, N=200)
        process.draw(n=100, N=200, marginal=True)
        process.draw(n=100, N=200, marginal=True, envelope=True)
        process.draw(n=100, N=200, envelope=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
