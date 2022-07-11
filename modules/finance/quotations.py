from config import config

key = '7df3ee8c'
endpoint = 'finance/quotations'

response = config.request(endpoint=endpoint, key=key)
