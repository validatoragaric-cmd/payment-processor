"""
Payment Processor

A simple payment processor that handles transactions and payment gateways.

Usage
-----

1. Initialize the `PaymentProcessor` class with your payment gateway API keys.
2. Use the `process_payment` method to handle transactions.

Dependencies
------------

* `requests` for API calls
* `json` for data serialization

"""

import os
import json
import requests

class PaymentProcessor:
    def __init__(self, api_keys):
        """
        Initialize the PaymentProcessor class with API keys.

        :param api_keys: A dictionary of API keys for different payment gateways.
        """
        self.api_keys = api_keys

    def process_payment(self, amount, payment_gateway):
        """
        Process a payment using a specific payment gateway.

        :param amount: The amount to be paid.
        :param payment_gateway: The payment gateway to use.
        :return: A dictionary with the transaction details.
        """
        if payment_gateway not in self.api_keys:
            raise ValueError("Invalid payment gateway")

        api_key = self.api_keys[payment_gateway]
        payload = {"amount": amount, "payment_gateway": payment_gateway}
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.post("https://api.example.com/transactions", json=payload, headers=headers)
        response.raise_for_status()

        return response.json()