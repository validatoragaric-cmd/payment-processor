import os
import logging
import yaml
from payment_processor import PaymentProcessor

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('log.txt')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    config = load_config()
    processor = PaymentProcessor(config)

    try:
        processor.process_payments()
    except Exception as e:
        logger.error(f'Error processing payments: {str(e)}')
        raise

if __name__ == '__main__':
    main()