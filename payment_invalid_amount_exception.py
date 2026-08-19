class InvalidPaymentAmountError(Exception):
    pass


class Payment:
    def pay(self, amount):
        if amount <= 0:
            raise InvalidPaymentAmountError("Payment amount must be greater than zero.")
        return f"Payment of {amount} processed successfully."


try:
    payment = Payment()
    print(payment.pay(-100))
except InvalidPaymentAmountError as error:
    print(f"InvalidPaymentAmountError: {error}")
