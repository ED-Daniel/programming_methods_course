import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from nistrng import check_eligibility_all_battery, SP800_22R1A_BATTERY, run_all_battery


class CustomMersenneTwister:
    def __init__(self, seed=5489):
        self.N = 624
        self.M = 397
        self.MATRIX_A = 0x9908B0DF
        self.UPPER_MASK = 0x80000000
        self.LOWER_MASK = 0x7FFFFFFF
        self.mt = [0] * self.N
        self.mti = self.N + 1
        self.seed_mt(seed)

    def seed_mt(self, seed):
        self.mt[0] = seed & 0xFFFFFFFF
        for i in range(1, self.N):
            self.mt[i] = (
                1812433253 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i
            ) & 0xFFFFFFFF

    def random(self):
        if self.mti >= self.N:
            self.twist()

        y = self.mt[self.mti]
        self.mti += 1

        y ^= y >> 11
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= y >> 18

        return y / 0xFFFFFFFF

    def twist(self):
        for i in range(self.N):
            y = (self.mt[i] & self.UPPER_MASK) | (
                self.mt[(i + 1) % self.N] & self.LOWER_MASK
            )
            self.mt[i] = self.mt[(i + self.M) % self.N] ^ (y >> 1)
            if y % 2 != 0:
                self.mt[i] ^= self.MATRIX_A
        self.mti = 0


# Линейный конгруэнтный генератор (LCG)
class LCG:
    def __init__(self, seed=1, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.state = seed

    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m


# Генерация выборок
def generate_samples(
    generator, num_samples=20, sample_size=100, range_min=0, range_max=4999
):
    samples = []
    for _ in range(num_samples):
        sample = [
            int(generator.random() * (range_max - range_min + 1) + range_min)
            for _ in range(sample_size)
        ]
        samples.append(sample)
    return samples


# Статистика выборок
def calculate_statistics(samples):
    statistics = []
    for sample in samples:
        mean = np.mean(sample)
        std_dev = np.std(sample)
        coeff_var = std_dev / mean if mean != 0 else 0
        statistics.append((mean, std_dev, coeff_var))
    return statistics


# Проверка на равномерность распределения (Хи-квадрат)
def chi_square_test(samples, num_bins=10):
    test_results = []
    for sample in samples:
        observed_freq, _ = np.histogram(
            sample, bins=num_bins, range=(min(sample), max(sample))
        )
        expected_freq = [len(sample) / num_bins] * num_bins
        chi2, p = chisquare(observed_freq, expected_freq)
        test_results.append((chi2, p))
    return test_results


# Проверка времени генерации чисел
def benchmark(generator, sizes):
    times = []
    for size in sizes:
        start_time = time.time()
        [generator.random() for _ in range(size)]
        end_time = time.time()
        times.append(end_time - start_time)
    return times


# Вывод статистики
def print_statistics(generator_name, statistics, chi2_results):
    print(f"\nStatistics for {generator_name}:")
    for i, (mean, std_dev, coeff_var) in enumerate(statistics):
        print(
            f"Sample {i+1}: Mean={mean}, StdDev={std_dev}, CoeffVar={coeff_var}"
        )

    print(f"\nChi-Square Test Results for {generator_name}:")
    for i, (chi2, p) in enumerate(chi2_results):
        print(f"Sample {i+1}: Chi2={chi2}, p-value={p}")


# Сохранение статистики в файл
def save_statistics_to_file(
    filename, generator_name, statistics, chi2_results
):
    with open(filename, "w") as file:
        file.write(f"Statistics for {generator_name}:\n")
        for i, (mean, std_dev, coeff_var) in enumerate(statistics):
            file.write(
                f"Sample {i+1}: Mean={mean}, StdDev={std_dev}, CoeffVar={coeff_var}\n"
            )

        file.write(f"\nChi-Square Test Results for {generator_name}:\n")
        for i, (chi2, p) in enumerate(chi2_results):
            file.write(f"Sample {i+1}: Chi2={chi2}, p-value={p}\n")


# Проверка с помощью тестов NIST
def run_nist_tests(data):
    arr = np.array(data)
    eligible_battery: dict = check_eligibility_all_battery(arr, SP800_22R1A_BATTERY)

    print("Eligible test from NIST-SP800-22r1a:")
    for name in eligible_battery.keys():
        print("\t" + name)

    results = run_all_battery(arr, eligible_battery, False)

    print("Test results:")
    for result, elapsed_time in results:
        if result.passed:
            print("\tPASSED - score: " + str(np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
        else:
            print("\tFAILED - score: " + str(np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")


# Основная функция
def main():
    # Создаем генераторы
    lcg = LCG(seed=12345)
    custom_mt = CustomMersenneTwister(seed=12345)

    # Генерация выборок
    lcg_samples = generate_samples(lcg)
    custom_mt_samples = generate_samples(custom_mt)

    # Рассчет статистики
    lcg_statistics = calculate_statistics(lcg_samples)
    custom_mt_statistics = calculate_statistics(custom_mt_samples)

    # Проверка на равномерность
    lcg_chi2 = chi_square_test(lcg_samples)
    custom_mt_chi2 = chi_square_test(custom_mt_samples)

    # Вывод и сохранение статистики
    print_statistics("LCG", lcg_statistics, lcg_chi2)
    print_statistics(
        "Custom Mersenne Twister", custom_mt_statistics, custom_mt_chi2
    )

    save_statistics_to_file(
        "lcg_statistics.txt", "LCG", lcg_statistics, lcg_chi2
    )
    save_statistics_to_file(
        "custom_mt_statistics.txt",
        "Custom Mersenne Twister",
        custom_mt_statistics,
        custom_mt_chi2,
    )

    # Проверка времени генерации чисел
    sizes = [1000, 10000, 100000, 1000000]
    lcg_times = benchmark(lcg, sizes)
    custom_mt_times = benchmark(custom_mt, sizes)
    np_times = benchmark(np.random, sizes)

    print("NIST TEST FOR 10 000")
    run_nist_tests([round(lcg.random() * 100) for _ in range(10000)])
    run_nist_tests([round(custom_mt.random() * 100) for _ in range(10000)])

    print("NIST TEST FOR 100 000")
    run_nist_tests([round(lcg.random() * 100) for _ in range(100000)])
    run_nist_tests([round(custom_mt.random() * 100) for _ in range(100000)])

    # Построение графиков
    plt.figure()
    plt.plot(sizes, lcg_times, label="LCG")
    plt.plot(sizes, custom_mt_times, label="Custom Mersenne Twister")
    plt.plot(sizes, np_times, label="NumPy Random")
    plt.xlabel("Size of Samples")
    plt.ylabel("Generation Time (seconds)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
