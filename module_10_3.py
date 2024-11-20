import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            suma = random.randint(50, 500)  # Случайное число от 50 до 500
            self.balance += suma
            print(f"Пополнение: {suma}. Баланс: {self.balance}")


            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            suma = random.randint(50, 500)
            print(f"Запрос на {suma}")


            if suma <= self.balance:
                self.balance -= suma
                print(f"Снятие: {suma}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")

                self.lock.acquire()

            time.sleep(0.001)



bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')